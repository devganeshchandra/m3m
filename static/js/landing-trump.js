/*
 * M3M Trump Tower Noida landing page: the hero slideshow, the 4 / 5 BHK buttons in every form,
 * the lead popup (buttons, 4 seconds after every page load, exit intent on desktop), the
 * slide-in offer, the FAQ and scroll reveals.
 * Validation and sending come from site.js and validation.js.
 */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  // Set once the visitor has sent their details: the automatic offers then stop.
  var SENT_KEY = "trump-lead-sent";
  var UNIT_LABELS = { "4bhk": "4 BHK", "5bhk": "5 BHK" };

  function $(selector, scope) {
    return (scope || document).querySelector(selector);
  }

  function $all(selector, scope) {
    return Array.prototype.slice.call((scope || document).querySelectorAll(selector));
  }

  var shownThisLoad = false;

  function sent() {
    try {
      return Boolean(sessionStorage.getItem(SENT_KEY));
    } catch (error) {
      return false;
    }
  }

  function rememberSent() {
    try {
      sessionStorage.setItem(SENT_KEY, "1");
    } catch (error) {
      // Private browsing: the offers may show again on the next page load.
    }
  }

  /* ---------- Hero slideshow ---------- */

  function initHero() {
    var hero = $("[data-tt-hero]");
    if (!hero) return;
    var slides = $all(".tt-hero__slide", hero);
    var dots = $all("[data-tt-slide]", hero);
    var caption = $("[data-tt-slide-caption]", hero);
    var current = 0;
    var timer = null;

    function show(index) {
      current = (index + slides.length) % slides.length;
      slides.forEach(function (slide, i) {
        slide.classList.toggle("is-active", i === current);
      });
      dots.forEach(function (dot, i) {
        dot.setAttribute("aria-pressed", i === current ? "true" : "false");
      });
      caption.textContent = dots[current].dataset.caption;
    }

    function restart() {
      clearInterval(timer);
      if (!reduceMotion && slides.length > 1) {
        timer = setInterval(function () {
          show(current + 1);
        }, 5500);
      }
    }

    dots.forEach(function (dot, i) {
      dot.addEventListener("click", function () {
        show(i);
        restart();
      });
    });
    restart();
  }

  /* ---------- Forms: the 4 / 5 BHK buttons fill a hidden field and the sales note ---------- */

  function setUnit(form, value) {
    var unit = $("[data-tt-unit]", form);
    var message = $("[data-tt-message]", form);
    unit.value = value || "";
    $all("[data-tt-unit-choice]", form).forEach(function (button) {
      button.setAttribute("aria-pressed", button.dataset.ttUnitChoice === value ? "true" : "false");
    });
    message.value = [message.dataset.request, value ? "Interested in: " + UNIT_LABELS[value] : ""]
      .filter(Boolean)
      .join("\n");
    if (value) {
      var error = document.getElementById(unit.dataset.errorId);
      if (error) error.hidden = true;
    }
  }

  function initForms() {
    document.addEventListener("landing:sent", function () {
      rememberSent();
      var slide = $("[data-tt-slidein]");
      if (slide) slide.hidden = true;
    });
    $all("[data-tt-form]").forEach(function (form) {
      setUnit(form, "");
      $all("[data-tt-unit-choice]", form).forEach(function (button) {
        button.addEventListener("click", function () {
          setUnit(form, button.dataset.ttUnitChoice);
        });
      });
      // After a successful send site.js clears the fields; clear the residence buttons too, and
      // stop the automatic offers for the rest of the visit.
      var status = $("[data-form-status]", form);
      new MutationObserver(function () {
        if (!status.classList.contains("is-success")) return;
        setUnit(form, "");
        rememberSent();
        var slide = $("[data-tt-slidein]");
        if (slide) slide.hidden = true;
      }).observe(status, { attributes: true, attributeFilter: ["class"] });
    });
  }

  /* ---------- Lead popup ---------- */

  function initDialog() {
    var dialog = $("[data-tt-dialog]");
    if (!dialog) return;
    var title = $("[data-tt-dialog-title]", dialog);

    function open(label, preset) {
      title.textContent = label;
      // The popup shows the next of the three form styles each time (landing-forms.js).
      var form = window.LandingForms.prepare(label, preset);
      if (!dialog.open) dialog.showModal();
      var first = window.LandingForms.firstControl(form);
      if (first) first.focus();
    }

    document.addEventListener("click", function (event) {
      var trigger = event.target.closest("[data-tt-open]");
      if (!trigger) return;
      event.preventDefault();
      open(trigger.dataset.ttOpen, trigger.dataset.ttUnitPreset);
    });

    // The site's floating "Enquire" button opens this page's form instead of the general one.
    $all(".floating-actions [data-enquiry-open]").forEach(function (button) {
      button.removeAttribute("data-enquiry-open");
      button.setAttribute("data-tt-open", "Request a callback");
    });

    $("[data-tt-close]", dialog).addEventListener("click", function () {
      dialog.close();
    });
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) dialog.close();
    });

    // Automatic offers: 4 seconds after every page load or refresh, and once more when the pointer
    // leaves the top of the window on desktop. Never while the visitor is typing in a form, and
    // never again once they have sent their details.
    function auto(label) {
      if (sent() || dialog.open) return;
      var active = document.activeElement;
      if (active && active.closest && active.closest("form")) return;
      open(label);
    }

    setTimeout(function () {
      auto("Get the price list");
      shownThisLoad = true;
    }, 4000);

    var exitShown = false;
    if (window.matchMedia("(pointer: fine)").matches) {
      document.addEventListener("mouseout", function (event) {
        if (exitShown || !shownThisLoad || event.relatedTarget || event.clientY > 0) return;
        exitShown = true;
        auto("Before you go: get the price list");
      });
    }
  }

  /* ---------- Slide-in offer, once the visitor is half-way down the page ---------- */

  function initSlidein() {
    var card = $("[data-tt-slidein]");
    if (!card) return;
    var dismissed = false;
    $("[data-tt-slidein-close]", card).addEventListener("click", function () {
      dismissed = true;
      card.classList.remove("is-visible");
    });
    card.addEventListener("click", function (event) {
      if (event.target.closest("[data-tt-open]")) card.classList.remove("is-visible");
    });
    window.addEventListener("scroll", function () {
      if (dismissed || sent()) return;
      var depth = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;
      if (depth > 0.5) card.hidden = false;
      card.classList.toggle("is-visible", depth > 0.5 && depth < 0.93);
    }, { passive: true });
  }

  /* ---------- Scroll reveals ---------- */

  function initReveals() {
    if (reduceMotion || !("IntersectionObserver" in window)) return;
    var items = $all(".tt-up");
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
    initHero();
    initForms();
    initDialog();
    initSlidein();
    initReveals();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
