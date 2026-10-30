/*
 * “Find on this page” for the landing page edit screen (projects/admin.py LandingPageAdmin): type words you see
 * on the website and only the texts, pictures and list items containing them stay visible, with a count per tab
 * and a button to jump to each tab. “?find=words” in the address fills it in.
 */
(function () {
  "use strict";

  var GROUPS = [
    { id: "texts", label: "Texts" },
    { id: "images", label: "Pictures" },
    { id: "items", label: "Lists" },
  ];

  function rows(group) {
    var element = document.getElementById(group.id + "-group");
    if (!element) return [];
    if (group.id === "items") {
      return Array.prototype.filter.call(element.querySelectorAll("[id^='items-']"), function (item) {
        return /^items-\d+$/.test(item.id);
      });
    }
    // Each text or picture is its own <tbody>: a summary line, the editable row and a hidden delete row.
    return Array.prototype.filter.call(element.querySelectorAll("tbody.form-group"), function (body) {
      return body.querySelector("tr.form-row");
    });
  }

  // Everything a row says: its labels and the current value of each field.
  function words(row) {
    var parts = [row.textContent];
    row.querySelectorAll("input, textarea, select").forEach(function (field) {
      if (field.type === "hidden" || field.type === "file" || field.type === "checkbox") return;
      parts.push(field.tagName === "SELECT" && field.selectedIndex >= 0 ? field.options[field.selectedIndex].text : field.value);
    });
    return parts.join(" ").toLowerCase();
  }

  function tabLink(id) {
    return document.querySelector('a[href="#' + id + '"]');
  }

  function init() {
    var first = tabLink("texts");
    if (!first) return;

    // The summary line above each text and picture repeats its Section and Label columns: hide it.
    var style = document.createElement("style");
    style.textContent = "#texts-group tbody.form-group > tr:first-child, #images-group tbody.form-group > tr:first-child { display: none; }";
    document.head.appendChild(style);
    var nav = first.closest("nav, ul") || first.parentElement;

    var box = document.createElement("div");
    box.style.cssText = "display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:0 0 16px;padding:12px 14px;" +
      "border:1px solid rgba(163,128,63,.45);border-radius:10px;background:rgba(163,128,63,.07)";
    box.innerHTML =
      '<label for="landing-find" style="font-weight:700">Find on this page</label>' +
      '<input id="landing-find" type="search" autocomplete="off" placeholder="Type words you see on the website, e.g. RERA, WhatsApp, Amity, hero" ' +
      'style="flex:1 1 320px;min-width:220px;padding:8px 10px;border:1px solid rgba(120,110,95,.4);border-radius:8px;background:transparent;color:inherit">' +
      '<span data-find-result style="font-size:13px;opacity:.85"></span>';
    nav.parentElement.insertBefore(box, nav);

    var input = box.querySelector("input");
    var result = box.querySelector("[data-find-result]");
    var cache = GROUPS.map(function (group) {
      return { group: group, rows: rows(group).map(function (row) { return { row: row, text: null }; }) };
    });

    function run() {
      var terms = input.value.toLowerCase().split(/\s+/).filter(Boolean);
      result.innerHTML = "";
      if (!terms.length) {
        cache.forEach(function (entry) {
          entry.rows.forEach(function (item) { item.row.style.display = ""; });
        });
        return;
      }
      var best = null;
      cache.forEach(function (entry) {
        var found = 0;
        entry.rows.forEach(function (item) {
          item.text = words(item.row); // Values can change while editing, so read them each time.
          var match = terms.every(function (term) { return item.text.indexOf(term) !== -1; });
          item.row.style.display = match ? "" : "none";
          if (match) found += 1;
        });
        var button = document.createElement("button");
        button.type = "button";
        button.textContent = entry.group.label + ": " + found;
        button.style.cssText = "margin-right:6px;padding:3px 10px;border:1px solid rgba(120,110,95,.4);border-radius:999px;" +
          (found ? "font-weight:700;cursor:pointer" : "opacity:.5;cursor:default");
        button.disabled = !found;
        button.addEventListener("click", function () {
          var link = tabLink(entry.group.id);
          if (link) link.click();
        });
        result.appendChild(button);
        if (found && !best) best = entry.group.id;
      });
      if (!best) {
        result.appendChild(document.createTextNode("Nothing found. Try fewer or different words."));
        return;
      }
      // Jump to a tab with matches when the open tab has none.
      var open = cache.filter(function (entry) {
        var link = tabLink(entry.group.id);
        return link && link.classList.contains("active");
      })[0];
      var openHasMatches = open && open.rows.some(function (item) { return item.row.style.display !== "none"; });
      if (!openHasMatches) tabLink(best).click();
    }

    var timer;
    input.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(run, 150);
    });

    var preset = new URLSearchParams(window.location.search).get("find");
    if (preset) {
      input.value = preset;
      run();
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
