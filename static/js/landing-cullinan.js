/*
 * M3M The Cullinan landing page: the two-step lead form, the lead popup, the room tour,
 * amenity filters, the slider and scroll reveals. Validation and sending come from site.js.
 */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(selector, scope) {
    return (scope || document).querySelector(selector);
  }

  function $all(selector, scope) {
    return Array.prototype.slice.call((scope || document).querySelectorAll(selector));
  }

  /* ---------- Two-step form ---------- */

  // The unit choice sets the project type, the project the lead is filed against (commercial
  // choices go to The Cullinan Avenue) and the note the sales team reads, then opens step 2.
  // Each choice carries its label and project type (data-label, data-interest) from the admin.
  function applyUnit(form, radio) {
    var interest = $("[data-cl-interest]", form);
    var project = $("[data-cl-project]", form);
    var message = $("[data-cl-message]", form);
    var value = radio.value;
    var commercial = radio.dataset.interest === "commercial";
    interest.value = value ? (commercial ? "commercial" : "residential") : "";
    project.value = commercial ? form.dataset.commercialProject : form.dataset.residentialProject;
    message.value = [message.dataset.request, value ? "Interested in: " + radio.dataset.label : ""]
      .filter(Boolean)
      .join("\n");
    if (value) {
      var error = document.getElementById(interest.dataset.errorId);
      if (error) error.hidden = true;
      form.classList.add("is-step-two");
    }
  }

  function initForms() {
    $all("[data-cl-form]").forEach(function (form) {
      var message = $("[data-cl-message]", form);
      message.value = message.dataset.request;
      $all("[data-cl-unit]", form).forEach(function (radio) {
        radio.addEventListener("change", function () {
          applyUnit(form, radio);
          var first = $("[data-cl-step-two] input", form);
          if (first && !form.closest("dialog")) first.focus({ preventScroll: true });
        });
      });
      // After a successful send site.js clears the fields; return the form to step 1.
      var status = $("[data-form-status]", form);
      new MutationObserver(function () {
        if (!status.classList.contains("is-success")) return;
        $all("[data-cl-unit]", form).forEach(function (radio) {
          radio.checked = false;
        });
      }).observe(status, { attributes: true, attributeFilter: ["class"] });
    });
  }

  /* ---------- Lead popup ---------- */

  function initDialog() {
    var dialog = $("[data-cl-dialog]");
    if (!dialog) return;
    var title = $("[data-cl-dialog-title]", dialog);

    function open(label, preset) {
      title.textContent = label;
      // The popup shows the next of the three form styles each time (landing-forms.js).
      var form = window.LandingForms.prepare(label, preset);
      if (!dialog.open) dialog.showModal();
      var first = window.LandingForms.firstControl(form);
      if (first) first.focus();
    }

    document.addEventListener("click", function (event) {
      var trigger = event.target.closest("[data-cl-open]");
      if (!trigger) return;
      event.preventDefault();
      open(trigger.dataset.clOpen, trigger.dataset.clUnitPreset);
    });

    // The site's floating "Enquire" button opens this page's form instead of the general one.
    $all(".floating-actions [data-enquiry-open]").forEach(function (button) {
      button.removeAttribute("data-enquiry-open");
      button.setAttribute("data-cl-open", "Request a callback");
    });

    $("[data-cl-close]", dialog).addEventListener("click", function () {
      dialog.close();
    });

    // Four seconds after every page open or refresh, offer the price list. It waits if the
    // visitor is already filling in a form, and stops once they have sent their details.
    var SENT_KEY = "cullinan-lead-sent";
    function seen() {
      try {
        return Boolean(sessionStorage.getItem(SENT_KEY));
      } catch (error) {
        return false;
      }
    }
    function markSent() {
      try {
        sessionStorage.setItem(SENT_KEY, "1");
      } catch (error) {
        // Private browsing: the popup may show again on the next page load.
      }
    }
    document.addEventListener("landing:sent", markSent);
    $all("[data-cl-form] [data-form-status]").forEach(function (item) {
      new MutationObserver(function () {
        if (item.classList.contains("is-success")) markSent();
      }).observe(item, { attributes: true, attributeFilter: ["class"] });
    });
    function autoOpen() {
      if (seen() || dialog.open) return;
      var active = document.activeElement;
      if (active && active.closest && active.closest("form")) return;
      open("Get the price list & floor plans");
    }
    setTimeout(autoOpen, 4000);
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) dialog.close();
    });
  }

  /* ---------- Room tour (tabs) ---------- */

  function initTour() {
    var stage = $("[data-cl-tour]");
    if (!stage) return;
    var tabs = $all('[role="tab"]', stage);

    function select(tab, focus) {
      tabs.forEach(function (item) {
        var on = item === tab;
        item.setAttribute("aria-selected", on ? "true" : "false");
        item.tabIndex = on ? 0 : -1;
        document.getElementById(item.getAttribute("aria-controls")).hidden = !on;
      });
      if (focus) tab.focus();
    }

    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () {
        select(tab);
      });
      tab.addEventListener("keydown", function (event) {
        var step = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[event.key];
        if (!step) return;
        event.preventDefault();
        select(tabs[(index + step + tabs.length) % tabs.length], true);
      });
    });
  }

  /* ---------- Amenities: filters and arrows ---------- */

  function initAmenities() {
    var strip = $("[data-cl-strip]");
    if (!strip) return;
    var cards = $all(".cl-strip__card", strip);
    var buttons = $all("[data-cl-filter]");
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        var group = button.dataset.clFilter;
        buttons.forEach(function (item) {
          item.setAttribute("aria-pressed", item === button ? "true" : "false");
        });
        cards.forEach(function (card) {
          card.hidden = group !== "all" && card.dataset.group !== group;
        });
        strip.scrollTo({ left: 0, behavior: reduceMotion ? "auto" : "smooth" });
      });
    });
    $all("[data-cl-strip-step]").forEach(function (button) {
      button.addEventListener("click", function () {
        var card = cards.filter(function (item) { return !item.hidden; })[0];
        var distance = card ? card.offsetWidth + 16 : 320;
        strip.scrollBy({ left: distance * Number(button.dataset.clStripStep), behavior: reduceMotion ? "auto" : "smooth" });
      });
    });
  }

  /* ---------- A closer look: slider ---------- */

  function initSlider() {
    var slider = $("[data-cl-slider]");
    if (!slider) return;
    var slides = $all(".cl-look__slide", slider);
    var thumbs = $all("[data-cl-slide]", slider);
    var caption = $("[data-cl-slide-caption]", slider);
    var count = $("[data-cl-slide-count]", slider);
    var current = 0;
    var timer = null;
    var pad = function (n) { return (n < 10 ? "0" : "") + n; };

    function show(index) {
      current = (index + slides.length) % slides.length;
      slides.forEach(function (slide, i) {
        slide.classList.toggle("is-active", i === current);
        slide.setAttribute("aria-hidden", i === current ? "false" : "true");
      });
      thumbs.forEach(function (thumb, i) {
        thumb.setAttribute("aria-pressed", i === current ? "true" : "false");
      });
      caption.textContent = thumbs[current].dataset.caption;
      count.textContent = pad(current + 1) + " / " + pad(slides.length);
    }

    function restart() {
      clearInterval(timer);
      if (!reduceMotion) timer = setInterval(function () { show(current + 1); }, 6000);
    }

    thumbs.forEach(function (thumb, i) {
      thumb.addEventListener("click", function () {
        show(i);
        restart();
      });
    });
    $all("[data-cl-slide-step]", slider).forEach(function (button) {
      button.addEventListener("click", function () {
        show(current + Number(button.dataset.clSlideStep));
        restart();
      });
    });
    restart();
  }

  /* ---------- Scroll reveals ---------- */

  function initReveals() {
    if (reduceMotion || !("IntersectionObserver" in window)) return;
    var items = $all(".cl-up");
    items.forEach(function (item) {
      item.classList.add("is-waiting");
    });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.remove("is-waiting");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    items.forEach(function (item) {
      observer.observe(item);
    });
  }

  function init() {
    initForms();
    initDialog();
    initTour();
    initAmenities();
    initSlider();
    initReveals();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
