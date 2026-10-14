#!/usr/bin/env python3
"""Build Hugo content from this repository's README and public repository READMEs.

The profile README becomes the homepage. Every other public, non-fork repository
becomes a page under content/projects, with relative README links rewritten so
images and files still resolve after the site is published.
"""

from __future__ import annotations

import base64
import json
import os
import posixpath
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_README_CHARS = 400_000
FRONT_MATTER_KEYS = (
    "title",
    "description",
    "date",
    "repo_name",
    "repo_url",
    "homepage",
    "language",
    "stars",
    "topics",
    "archived",
)
IMAGE_EXTS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".avif",
    ".bmp",
    ".ico",
}
FILE_EXTS = IMAGE_EXTS | {
    ".md",
    ".markdown",
    ".txt",
    ".pdf",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".py",
    ".js",
    ".ts",
    ".css",
    ".html",
    ".xml",
    ".csv",
    ".zip",
    ".gz",
    ".mp4",
    ".webm",
    ".mp3",
    ".wav",
    ".woff",
    ".woff2",
}
FENCE_RE = re.compile(r"^ *(```|~~~)[^\n]*\n.*?^\s*\1\s*$", re.M | re.S)
INLINE_CODE_RE = re.compile(r"`+[^`]*`+")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
DANGEROUS_BLOCK_RE = re.compile(
    r"<\s*(script|iframe|object|embed|form|base)\b[^>]*>.*?<\s*/\s*\1\s*>",
    re.I | re.S,
)
DANGEROUS_TAG_RE = re.compile(
    r"<\s*/?\s*(script|iframe|object|embed|form|base)\b[^>]*>",
    re.I,
)
TAG_RE = re.compile(r"<[^>]+>", re.S)
EVENT_RE = re.compile(
    r"\s+on[a-z]+\s*=\s*(\"[^\"]*\"|'[^']*'|[^\s>]+)",
    re.I,
)
INLINE_LINK_RE = re.compile(
    r"(?P<img>!?)"
    r"\[(?P<label>[^\]]*)\]"
    r"\((?P<url><[^>\n]+>|[^)\s]+)(?P<title>\s+\"[^\"]*\")?\)"
)
REF_LINK_RE = re.compile(
    r"^[ ]{0,3}\[(?P<id>[^\]]+)\]:[ \t]+(?P<url>\S+)(?P<rest>.*)$",
    re.M,
)
HTML_ATTR_RE = re.compile(
    r"(?P<attr>\b(?:src|href))(?P<eq>\s*=\s*)(?P<q>[\"'])(?P<url>.*?)(?P=q)",
    re.I,
)
HEADING_RE = re.compile(r"^#\s+(.+?)\s*#*\s*$")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}T[\d:.]+Z")


@dataclass(frozen=True)
class RepoRef:
    owner: str
    name: str
    branch: str
    readme_dir: str = ""


def map_spans(text: str, pattern: re.Pattern[str], fn) -> str:
    parts: list[str] = []
    last = 0
    for match in pattern.finditer(text):
        parts.append(fn(text[last : match.start()]))
        parts.append(match.group(0))
        last = match.end()
    parts.append(fn(text[last:]))
    return "".join(parts)


def map_fences(text: str, fn) -> str:
    return map_spans(text, FENCE_RE, fn)


def map_inline_code(text: str, fn) -> str:
    return map_spans(text, INLINE_CODE_RE, fn)


def strip_events(tag: str) -> str:
    return EVENT_RE.sub("", tag)


def clean_prose(segment: str) -> str:
    segment = COMMENT_RE.sub("", segment)
    segment = DANGEROUS_BLOCK_RE.sub("", segment)
    segment = DANGEROUS_TAG_RE.sub("", segment)
    return TAG_RE.sub(lambda match: strip_events(match.group(0)), segment)


def strip_dangerous(text: str) -> str:
    return map_fences(text, lambda segment: map_inline_code(segment, clean_prose))


def is_external(url: str) -> bool:
    lowered = url.lower()
    if lowered.startswith(("#", "mailto:", "http://", "https://", "//", "data:", "tel:")):
        return True
    return bool(urlsplit(url).scheme)


def has_known_ext(path: str) -> bool:
    return posixpath.splitext(path)[1].lower() in FILE_EXTS


def is_image_path(path: str) -> bool:
    return posixpath.splitext(path)[1].lower() in IMAGE_EXTS


def github_url(ref: RepoRef, path: str, *, raw: bool) -> str:
    branch = quote(ref.branch, safe="/")
    quoted = quote(path, safe="/")
    if raw:
        return f"https://raw.githubusercontent.com/{ref.owner}/{ref.name}/{branch}/{quoted}"
    return f"https://github.com/{ref.owner}/{ref.name}/blob/{branch}/{quoted}"


def with_suffix(base: str, query: str, fragment: str) -> str:
    if query:
        base += "?" + query
    if fragment:
        base += "#" + fragment
    return base


def rewrite_url(url: str, ref: RepoRef, *, prefer_raw: bool) -> str:
    raw_url = url.strip()
    if not raw_url or raw_url.lower().startswith("javascript:") or is_external(raw_url):
        return "#" if raw_url.lower().startswith("javascript:") else url

    parts = urlsplit(raw_url)
    if not parts.path:
        return url

    rooted = parts.path.startswith("/")
    relative = parts.path.lstrip("/") if rooted else parts.path
    base_dir = "" if rooted else ref.readme_dir
    path = posixpath.normpath(posixpath.join(base_dir, relative))
    if path in {"", ".", ".."} or path.startswith("../"):
        return url
    if rooted and not has_known_ext(path):
        return url

    built = github_url(ref, path, raw=prefer_raw or is_image_path(path))
    return with_suffix(built, parts.query, parts.fragment)


def unwrap_url(url: str) -> str:
    if url.startswith("<") and url.endswith(">"):
        return url[1:-1]
    return url


def format_md_target(url: str) -> str:
    if any(char in url for char in " \t()"):
        return f"<{url}>"
    return url


def rewrite_markdown_links(segment: str, ref: RepoRef) -> str:
    def replace_inline(match: re.Match[str]) -> str:
        target = rewrite_url(
            unwrap_url(match.group("url")),
            ref,
            prefer_raw=match.group("img") == "!",
        )
        title = match.group("title") or ""
        return f"{match.group('img')}[{match.group('label')}]({format_md_target(target)}{title})"

    def replace_ref(match: re.Match[str]) -> str:
        target = rewrite_url(match.group("url"), ref, prefer_raw=False)
        return f"[{match.group('id')}]: {format_md_target(target)}{match.group('rest')}"

    def replace_attr(match: re.Match[str]) -> str:
        prefer_raw = match.group("attr").lower() == "src"
        target = rewrite_url(match.group("url"), ref, prefer_raw=prefer_raw)
        return f"{match.group('attr')}{match.group('eq')}{match.group('q')}{target}{match.group('q')}"

    segment = INLINE_LINK_RE.sub(replace_inline, segment)
    segment = REF_LINK_RE.sub(replace_ref, segment)
    return HTML_ATTR_RE.sub(replace_attr, segment)


def rewrite_links(text: str, ref: RepoRef) -> str:
    return map_fences(
        text,
        lambda segment: map_inline_code(
            segment, lambda prose: rewrite_markdown_links(prose, ref)
        ),
    )


def neutralize_shortcodes(text: str) -> str:
    return (
        text.replace("{{<", "{{ <")
        .replace("{{%", "{{ %")
        .replace(">}}", "> }}")
        .replace("%}}", "% }}")
    )


def clean_heading(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "")
    text = text.replace("**", "").replace("__", "")
    return re.sub(r"\s+", " ", text.strip("* ").strip())


def extract_title(body: str) -> tuple[str, str]:
    lines = body.split("\n")
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines):
        return "", body
    match = HEADING_RE.match(lines[index].strip())
    if not match:
        return "", body
    raw = match.group(1).strip()
    if raw.startswith("!") or "<" in raw or len(raw) > 100:
        return "", body
    title = clean_heading(raw)
    if not title:
        return "", body
    rest = "\n".join(lines[:index] + lines[index + 1 :])
    return title, rest


def prepare_document(text: str, ref: RepoRef, *, take_title: bool) -> tuple[str, str]:
    text = text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    text = strip_dangerous(text)
    title = ""
    if take_title:
        title, text = extract_title(text)
    text = rewrite_links(text, ref)
    text = neutralize_shortcodes(text).strip()
    return title, (text + "\n") if text else ""


def humanize(name: str) -> str:
    words = []
    for part in re.split(r"[-_]+", name):
        if not part:
            continue
        words.append(part.capitalize() if part.islower() else part)
    return " ".join(words) or name


def one_line(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def clip(text: str, limit: int = 220) -> str:
    text = one_line(text)
    if len(text) <= limit:
        return text
    cut = text[: limit - 1].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "…"


def plain_paragraph(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "")
    text = text.replace("**", "").replace("__", "")
    return one_line(text)


def first_paragraph(body: str) -> str:
    lines: list[str] = []
    started = False
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            if started:
                break
            continue
        if stripped.startswith(("#", "![", "[![", "|", "<", "---", "***", "```", "~~~")):
            if started:
                break
            continue
        started = True
        lines.append(stripped)
    return clip(plain_paragraph(" ".join(lines)))


def skip_reason(repo: dict, *, owner: str, source_repo: str, include_forks: bool) -> str | None:
    name = str(repo.get("name") or "")
    if repo.get("private") or repo.get("visibility") in {"private", "internal"}:
        return "private"
    if name in {source_repo, f"{owner}.github.io"}:
        return "site"
    if repo.get("fork") and not include_forks:
        return "fork"
    if (
        not name
        or name in {".", ".."}
        or "/" in name
        or "\\" in name
        or name.startswith(".")
    ):
        return "name"
    return None


def page_filename(name: str) -> str:
    if name in {"_index", "index"}:
        return f"repo-{name}.md"
    return f"{name}.md"


def yaml_value(key: str, value: object) -> str:
    if key == "date" and isinstance(value, str) and DATE_RE.fullmatch(value):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, list):
        items = ", ".join(json.dumps(str(item), ensure_ascii=False) for item in value)
        return f"[{items}]"
    return json.dumps(str(value), ensure_ascii=False)


def render_page(fields: dict, body: str) -> str:
    lines = ["---"]
    for key in FRONT_MATTER_KEYS:
        if key not in fields:
            continue
        value = fields[key]
        if value is None or value == "" or value == []:
            continue
        lines.append(f"{key}: {yaml_value(key, value)}")
    lines.append("---")
    lines.append("")
    text = body.strip()
    if text:
        lines.append(text)
    lines.append("")
    return "\n".join(lines)


def decode_readme(payload: dict) -> str:
    if payload.get("encoding") == "base64":
        raw = base64.b64decode(payload.get("content") or "")
        return raw.decode("utf-8", "replace")
    return str(payload.get("content") or "")


class GitHub:
    def __init__(self, token: str) -> None:
        self.token = token.strip()
        self.remaining = ""

    def get_json(self, url: str, *, allow_404: bool = False):
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "stevwyman-pages",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, headers=headers)
        delay = 1.5
        last_error: Exception | None = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    self.remaining = response.headers.get("X-RateLimit-Remaining", "")
                    return json.load(response)
            except urllib.error.HTTPError as error:
                last_error = error
                if error.code == 404 and allow_404:
                    return None
                if error.code in {500, 502, 503, 504} and attempt < 2:
                    time.sleep(delay)
                    delay *= 2
                    continue
                detail = error.read().decode("utf-8", "replace")[:400]
                remaining = error.headers.get("X-RateLimit-Remaining", "") if error.headers else ""
                raise SystemExit(
                    f"GitHub API {error.code} for {url} (rate limit remaining: {remaining}): {detail}"
                ) from error
            except urllib.error.URLError as error:
                last_error = error
                if attempt < 2:
                    time.sleep(delay)
                    delay *= 2
                    continue
                raise SystemExit(f"GitHub API request failed for {url}: {error}") from error
        raise SystemExit(f"GitHub API request failed for {url}: {last_error}")

    def list_repos(self, owner: str) -> list[dict]:
        repos: list[dict] = []
        for page in range(1, 21):
            url = (
                "https://api.github.com/users/"
                f"{quote(owner)}/repos?per_page=100&page={page}&sort=pushed&direction=desc"
            )
            batch = self.get_json(url)
            if not isinstance(batch, list):
                raise SystemExit("Unexpected GitHub response while listing repositories.")
            repos.extend(batch)
            if len(batch) < 100:
                break
        return repos

    def readme(self, owner: str, name: str) -> dict | None:
        url = f"https://api.github.com/repos/{quote(owner)}/{quote(name)}/readme"
        payload = self.get_json(url, allow_404=True)
        return payload if isinstance(payload, dict) else None


def repo_date(repo: dict) -> str:
    for key in ("pushed_at", "updated_at", "created_at"):
        value = str(repo.get(key) or "")
        if DATE_RE.fullmatch(value):
            return value
    return "1970-01-01T00:00:00Z"


def write_project(repo: dict, owner: str, github: GitHub, projects: Path) -> str:
    name = str(repo["name"])
    payload = github.readme(owner, name)
    branch = str(repo.get("default_branch") or "main")
    readme_dir = ""
    readme_body = ""
    status = "readme"
    if payload:
        readme_body = decode_readme(payload)
        readme_dir = posixpath.dirname(str(payload.get("path") or ""))
        if readme_dir == ".":
            readme_dir = ""
    else:
        status = "missing-readme"

    title, body = prepare_document(
        readme_body,
        RepoRef(owner, name, branch, readme_dir),
        take_title=True,
    )
    if not title:
        title = humanize(name)
    description = one_line(str(repo.get("description") or "")) or first_paragraph(body)
    if len(body) > MAX_README_CHARS:
        body = body[:MAX_README_CHARS].rstrip() + "\n\nThe rest of this README is on GitHub.\n"
    if not body.strip():
        body = f"{description}\n" if description else "This repository has no README yet.\n"

    homepage = str(repo.get("homepage") or "").strip()
    if not homepage.startswith(("http://", "https://")):
        homepage = ""
    topics = sorted({str(topic) for topic in (repo.get("topics") or []) if topic})[:8]
    fields: dict = {
        "title": title,
        "description": clip(description) if description else "",
        "date": repo_date(repo),
        "repo_name": name,
        "repo_url": repo.get("html_url") or f"https://github.com/{owner}/{name}",
        "homepage": homepage,
        "language": repo.get("language") or "",
        "stars": int(repo.get("stargazers_count") or 0),
        "topics": topics,
    }
    if repo.get("archived"):
        fields["archived"] = True

    destination = (projects / page_filename(name)).resolve()
    if destination.parent != projects.resolve():
        raise SystemExit(f"Refusing to write outside the projects directory: {name}")
    destination.write_text(render_page(fields, body), encoding="utf-8")
    return status


def build(root: Path | None = None) -> int:
    root = root or ROOT
    owner = os.environ.get("OWNER", "stevwyman").strip() or "stevwyman"
    source_repo = os.environ.get("SOURCE_REPO", owner).strip() or owner
    source_branch = os.environ.get("SOURCE_BRANCH", "main").strip() or "main"
    include_forks = os.environ.get("INCLUDE_FORKS", "").lower() in {"1", "true", "yes"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

    content = root / "content"
    projects = content / "projects"
    if projects.exists():
        shutil.rmtree(projects)
    projects.mkdir(parents=True)

    profile = root / "README.md"
    profile_text = profile.read_text(encoding="utf-8") if profile.exists() else ""
    _, home_body = prepare_document(
        profile_text,
        RepoRef(owner, source_repo, source_branch, ""),
        take_title=False,
    )
    if not home_body.strip():
        home_body = "Public projects from this GitHub account.\n"
    (content / "_index.md").write_text(
        render_page(
            {
                "title": "Stev Wyman",
                "description": "Public projects by Stev Wyman, rendered from each repository README.",
            },
            home_body,
        ),
        encoding="utf-8",
    )
    (projects / "_index.md").write_text(
        render_page(
            {"title": "Projects"},
            "A page for each public repository, built from its README.\n",
        ),
        encoding="utf-8",
    )

    github = GitHub(token)
    written = 0
    skipped_forks = 0
    missing = 0
    for repo in github.list_repos(owner):
        reason = skip_reason(
            repo,
            owner=owner,
            source_repo=source_repo,
            include_forks=include_forks,
        )
        if reason == "fork":
            skipped_forks += 1
            continue
        if reason:
            continue
        status = write_project(repo, owner, github, projects)
        written += 1
        if status == "missing-readme":
            missing += 1
        print(f"project {repo.get('name')}")

    print(
        f"Wrote {written} project pages"
        f" ({missing} without a README, {skipped_forks} forks skipped)."
    )
    if github.remaining:
        print(f"GitHub rate limit remaining: {github.remaining}")
    if written == 0:
        print("No public project pages were written.", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    return build()


if __name__ == "__main__":
    sys.exit(main())
