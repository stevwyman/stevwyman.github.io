#!/usr/bin/env python3
"""Tests for README processing. These do not call the GitHub API."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_content as content


REF = content.RepoRef("stevwyman", "mediator", "main", "")


class RewriteTests(unittest.TestCase):
    def test_relative_image_uses_raw_github(self):
        url = content.rewrite_url("docs/arch.png", REF, prefer_raw=True)
        self.assertEqual(
            url,
            "https://raw.githubusercontent.com/stevwyman/mediator/main/docs/arch.png",
        )

    def test_relative_markdown_uses_blob(self):
        url = content.rewrite_url("docs/guide.md", REF, prefer_raw=False)
        self.assertEqual(
            url,
            "https://github.com/stevwyman/mediator/blob/main/docs/guide.md",
        )

    def test_app_route_stays_put(self):
        self.assertEqual(
            content.rewrite_url("/mediate/", REF, prefer_raw=False),
            "/mediate/",
        )

    def test_external_link_stays_put(self):
        url = "https://example.com/docs"
        self.assertEqual(content.rewrite_url(url, REF, prefer_raw=False), url)

    def test_javascript_url_is_removed(self):
        self.assertEqual(
            content.rewrite_url("javascript:alert(1)", REF, prefer_raw=False),
            "#",
        )

    def test_transform_keeps_code_fences_and_rewrites_prose(self):
        source = "See ![diagram](docs/arch.png).\n\n```md\n![diagram](docs/arch.png)\n```\n"
        _, body = content.prepare_document(source, REF, take_title=False)
        prose, fenced = body.split("```", 1)
        self.assertIn("raw.githubusercontent.com/stevwyman/mediator/main/docs/arch.png", prose)
        self.assertIn("![diagram](docs/arch.png)", fenced)

    def test_reference_image_is_rewritten(self):
        source = "![logo][logo]\n\n[logo]: images/logo.png\n"
        _, body = content.prepare_document(source, REF, take_title=False)
        self.assertIn(
            "https://raw.githubusercontent.com/stevwyman/mediator/main/images/logo.png",
            body,
        )

    def test_html_comment_is_removed_outside_code(self):
        source = "Hello\n<!-- secret -->\nThere\n\n```\n<!-- keep -->\n```\n"
        _, body = content.prepare_document(source, REF, take_title=False)
        self.assertNotIn("secret", body)
        self.assertIn("<!-- keep -->", body)

    def test_script_tag_is_removed_outside_code(self):
        source = "Before\n<script>alert(1)</script>\nAfter\n\n```html\n<script>alert(1)</script>\n```\n"
        _, body = content.prepare_document(source, REF, take_title=False)
        prose = body.split("```", 1)[0]
        self.assertNotIn("<script>", prose)
        self.assertIn("<script>alert(1)</script>", body)

    def test_shortcode_delimiters_cannot_reach_hugo(self):
        source = "```\n{{< figure src=\"x\" >}}\n```\n"
        _, body = content.prepare_document(source, REF, take_title=False)
        self.assertNotIn("{{<", body)
        self.assertIn("{{ <", body)

    def test_title_comes_from_the_first_heading(self):
        title, body = content.extract_title("# Mediator\n\nLets two parties check a deal.\n")
        self.assertEqual(title, "Mediator")
        self.assertTrue(body.lstrip().startswith("Lets two parties"))

    def test_second_level_heading_is_not_a_title(self):
        source = "## Usage\n\nDo the thing\n"
        title, body = content.extract_title(source)
        self.assertEqual(title, "")
        self.assertEqual(body, source)

    def test_emphasis_is_removed_from_the_title(self):
        title, _body = content.extract_title("# **Game theory**\n\nNotes.\n")
        self.assertEqual(title, "Game theory")


class SelectionTests(unittest.TestCase):
    def test_private_repos_are_never_published(self):
        reason = content.skip_reason(
            {"name": "secret", "private": True, "fork": False, "visibility": "private"},
            owner="stevwyman",
            source_repo="stevwyman",
            include_forks=False,
        )
        self.assertEqual(reason, "private")

    def test_profile_and_pages_repos_are_skipped(self):
        self.assertEqual(
            content.skip_reason(
                {"name": "stevwyman", "private": False, "fork": False},
                owner="stevwyman",
                source_repo="stevwyman",
                include_forks=False,
            ),
            "site",
        )
        self.assertEqual(
            content.skip_reason(
                {"name": "stevwyman.github.io", "private": False, "fork": False},
                owner="stevwyman",
                source_repo="stevwyman",
                include_forks=False,
            ),
            "site",
        )

    def test_forks_are_skipped_unless_requested(self):
        repo = {"name": "taxonomy", "private": False, "fork": True}
        self.assertEqual(
            content.skip_reason(repo, owner="stevwyman", source_repo="stevwyman", include_forks=False),
            "fork",
        )
        self.assertIsNone(
            content.skip_reason(repo, owner="stevwyman", source_repo="stevwyman", include_forks=True)
        )

    def test_humanize_keeps_internal_capitals(self):
        self.assertEqual(content.humanize("finra_bonds"), "Finra Bonds")
        self.assertEqual(content.humanize("genTree"), "genTree")


if __name__ == "__main__":
    unittest.main()
