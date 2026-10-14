(function () {
  var cards = document.querySelectorAll(".card");
  var buttons = document.querySelectorAll("[data-filter]");
  var empty = document.getElementById("filter-empty");
  if (!buttons.length || !cards.length) return;

  function apply(flag) {
    var active = !flag || flag === "all" ? "all" : flag;
    cards.forEach(function (card) {
      var flags = (card.getAttribute("data-flags") || "")
        .split(",")
        .map(function (item) { return item.trim(); })
        .filter(Boolean);
      card.hidden = active !== "all" && flags.indexOf(active) === -1;
    });
    document.querySelectorAll("[data-group-section]").forEach(function (section) {
      section.hidden = !section.querySelector(".card:not([hidden])");
    });
    buttons.forEach(function (button) {
      button.setAttribute("aria-pressed", button.getAttribute("data-filter") === active ? "true" : "false");
    });
    if (empty) empty.hidden = active === "all" || !!document.querySelector(".card:not([hidden])");
  }

  apply(new URLSearchParams(window.location.search).get("flag"));

  buttons.forEach(function (button) {
    button.addEventListener("click", function (event) {
      event.preventDefault();
      var flag = button.getAttribute("data-filter");
      var url = new URL(window.location.href);
      if (!flag || flag === "all") url.searchParams.delete("flag");
      else url.searchParams.set("flag", flag);
      url.hash = "";
      window.history.replaceState(null, "", url);
      apply(flag);
    });
  });
})();
