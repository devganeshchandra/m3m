/*
 * Popup forms on project landing pages (templates/projects/landing/_popup_forms.html): three
 * form styles shown in rotation, one per opening of the popup. Pages call
 * window.LandingForms.prepare(label, preset) when they open their popup. Validation and
 * sending come from site.js; a successful send dispatches "landing:sent" on the document.
 */
(function () {
  "use strict";

  var ORDER = ["a", "b", "c"];

  function $(selector, scope) {
    return (scope || document).querySelector(selector);
  }

  function $all(selector, scope) {
    return Array.prototype.slice.call((scope || document).querySelectorAll(selector));
  }

  var root = $("[data-pf]");
  var units = {};
  var nextIndex = 0;
  var request = "Requested: Project details";

  function unitList() {
    var data = $("[data-pf-units]");
    if (!data) return [];
    try {
      return JSON.parse(data.textContent).units;
    } catch (error) {
      return [];
    }
  }

  // Sets the residence on a form: hidden fields, the project the lead is filed against, the note
  // for the sales team and the selected state of the visible controls.
  function setUnit(form, value) {
    var unit = units[value];
    $("[data-pf-unit]", form).value = unit ? value : "";
    $("[data-pf-interest]", form).value = unit ? unit.interest : "";
    $("[data-pf-project]", form).value = unit ? unit.project : form.dataset.defaultProject;
    $("[data-pf-message]", form).value = [request, unit ? "Interested in: " + unit.label : ""].filter(Boolean).join("\n");
    $all("[data-pf-pick]", form).forEach(function (button) {
      button.setAttribute("aria-pressed", button.dataset.pfPick === value ? "true" : "false");
    });
    var select = $("[data-pf-select]", form);
    if (select) select.value = unit ? value : "";
    form.classList.toggle("is-picked", Boolean(unit));
    if (unit) {
      var error = document.getElementById($("[data-pf-unit]", form).dataset.errorId);
      if (error) error.hidden = true;
    }
  }

  function reset(form) {
    var status = $("[data-form-status]", form);
    status.textContent = "";
    status.classList.remove("is-success");
  }

  function prepare(label, preset) {
    if (!root) return null;
    var forms = $all("[data-pf-form]", root);
    var variant = ORDER[nextIndex % ORDER.length];
    nextIndex += 1;
    request = "Requested: " + label;
    var form = null;
    forms.forEach(function (item) {
      var on = item.dataset.pfVariant === variant;
      item.hidden = !on;
      if (on) form = item;
    });
    reset(form);
    setUnit(form, preset && units[preset] ? preset : $("[data-pf-unit]", form).value);
    return form;
  }

  // The control to focus when the popup opens. Before a residence is chosen that is the popup's
  // heading: focusing the first residence would outline it, and it would look already chosen.
  function firstControl(form) {
    if (!form) return null;
    if (form.classList.contains("is-picked") || form.dataset.pfVariant === "a") {
      return $("[name=name]", form);
    }
    var dialog = form.closest("dialog");
    var heading = dialog && $("h2", dialog);
    if (heading) heading.tabIndex = -1;
    return heading;
  }

  function init() {
    if (!root) return;
    unitList().forEach(function (unit) {
      units[unit.value] = unit;
    });
    nextIndex = Math.max(0, ORDER.indexOf(root.dataset.pfStart));

    $all("[data-pf-form]", root).forEach(function (form) {
      form.dataset.defaultProject = $("[data-pf-project]", form).value;
      setUnit(form, "");
      $all("[data-pf-pick]", form).forEach(function (button) {
        button.addEventListener("click", function () {
          setUnit(form, button.dataset.pfPick);
          var name = $("[name=name]", form);
          if (form.dataset.pfVariant === "b" && name) name.focus();
        });
      });
      var select = $("[data-pf-select]", form);
      if (select) {
        select.addEventListener("change", function () {
          setUnit(form, select.value);
        });
      }
      var status = $("[data-form-status]", form);
      new MutationObserver(function () {
        if (!status.classList.contains("is-success")) return;
        setUnit(form, "");
        document.dispatchEvent(new CustomEvent("landing:sent"));
      }).observe(status, { attributes: true, attributeFilter: ["class"] });
    });
  }

  window.LandingForms = { prepare: prepare, firstControl: firstControl };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
