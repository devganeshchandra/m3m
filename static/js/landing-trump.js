/*
 * M3M Trump Tower Noida landing page: the hero slideshow, the 4 / 5 BHK buttons in every form,
 * the lead popup (buttons, 4 seconds after every page load, exit intent on desktop), the form
 * titles that ink in gold letter by letter, the private lift, the departures board clock, the
 * slide-in offer and scroll reveals. The board's routes come from landing-location.js.
 * Validation and sending come from site.js and validation.js.
 */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  // Set once the visitor has sent their details: the automatic offers then stop.
  var SENT_KEY = "trump-lead-sent";

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

  /* ---------- Form titles: each letter rises in, then gold ink runs through them ---------- */

  function letterize(element, text) {
    text = (text || element.textContent).trim();
    element.textContent = "";
    var copy = document.createElement("span");
    copy.className = "visually-hidden";
    copy.textContent = text;
    var letters = document.createElement("span");
    letters.className = "tt-letters";
    letters.setAttribute("aria-hidden", "true");
    var index = 0;
    text.split(/(\s+)/).forEach(function (part) {
      if (!part) return;
      if (/^\s+$/.test(part)) {
        letters.appendChild(document.createTextNode(" "));
        return;
      }
      var word = document.createElement("span");
      word.className = "tt-word";
      Array.from(part).forEach(function (letter) {
        var char = document.createElement("span");
        char.className = "tt-letter";
        char.style.setProperty("--i", index++);
        char.textContent = letter;
        word.appendChild(char);
      });
      letters.appendChild(word);
    });
    element.appendChild(copy);
    element.appendChild(letters);
  }

  function initLetters() {
    $all("[data-tt-letters]").forEach(function (element) {
      letterize(element);
    });
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
    var label = "";
    unit.value = value || "";
    $all("[data-tt-unit-choice]", form).forEach(function (button) {
      var chosen = button.dataset.ttUnitChoice === value;
      button.setAttribute("aria-pressed", chosen ? "true" : "false");
      if (chosen) label = button.dataset.label;
    });
    message.value = [message.dataset.request, value ? "Interested in: " + label : ""]
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
      letterize(title, label);
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

  /* ---------- The private lift: residence, floor, then details; the lift answers each choice ---------- */

  function initLift() {
    var stage = $("[data-tt-lift]");
    if (!stage) return;
    var form = $("[data-tt-lift-form]", stage);
    var steps = $all("[data-lift-step]", form);
    var lamps = $all(".tt-lift__buttons li", form);
    var unit = $("[data-lift-unit]", form);
    var message = $("[data-lift-message]", form);
    var needle = $("[data-lift-needle]", stage);
    var display = $("[data-lift-display]", stage);
    var unitDisplay = $("[data-lift-unit-display]", stage);
    var owner = $("[data-lift-owner]", stage);
    var welcome = $("[data-lift-welcome]", stage);
    var views = $all("[data-lift-view]", stage);
    var floors = $all("[data-lift-floor]", form);
    var marks = $all(".tt-elevator__marks li", stage);
    var current = 0;
    var unitLabel = "";
    var floorLabel = "";
    var sentName = "";
    var moving = null;

    function compose() {
      message.value = [
        message.dataset.request,
        unitLabel ? "Interested in: " + unitLabel : "",
        floorLabel ? "Floor preference: " + floorLabel : "",
      ].filter(Boolean).join("\n");
    }

    function show(index) {
      current = index;
      steps.forEach(function (step, i) {
        step.hidden = i !== index;
      });
      lamps.forEach(function (lamp, i) {
        lamp.classList.toggle("is-lit", i === index);
        lamp.classList.toggle("is-done", i < index);
      });
    }

    function chosen(step) {
      return Boolean($("[aria-pressed='true']", step)) || !$("[data-lift-unit-choice], [data-lift-floor]", step);
    }

    $all("[data-lift-unit-choice]", form).forEach(function (button) {
      button.addEventListener("click", function () {
        $all("[data-lift-unit-choice]", form).forEach(function (other) {
          other.setAttribute("aria-pressed", other === button ? "true" : "false");
        });
        unit.value = button.dataset.liftUnitChoice;
        unitLabel = button.dataset.label;
        unitDisplay.textContent = unitLabel;
        var error = document.getElementById(unit.dataset.errorId);
        if (error) error.hidden = true;
        compose();
      });
    });

    // A new floor: the doors close, the needle swings, the view changes and the doors open again.
    floors.forEach(function (button) {
      button.addEventListener("click", function () {
        var index = Number(button.dataset.liftFloor);
        floors.forEach(function (other) {
          other.setAttribute("aria-pressed", other === button ? "true" : "false");
        });
        floorLabel = button.dataset.label;
        compose();
        var angle = floors.length > 1 ? -75 + (index * 150) / (floors.length - 1) : 0;
        needle.style.setProperty("--angle", angle + "deg");
        marks.forEach(function (mark, i) {
          mark.classList.toggle("is-on", i === index);
        });
        display.textContent = button.dataset.word;
        clearTimeout(moving);
        stage.classList.remove("is-open");
        stage.classList.add("is-moving");
        moving = setTimeout(function () {
          views.forEach(function (view) {
            view.classList.toggle("is-active", view.dataset.liftView === String(index));
          });
          stage.classList.remove("is-moving");
          stage.classList.add("is-open");
        }, reduceMotion ? 0 : 900);
      });
    });

    $all("[data-lift-next]", form).forEach(function (button) {
      button.addEventListener("click", function () {
        var step = steps[current];
        var error = $("[data-lift-error]", step);
        if (!chosen(step)) {
          error.hidden = false;
          return;
        }
        error.hidden = true;
        show(current + 1);
        var first = $("input:not([type='hidden']), button[aria-pressed]", steps[current]);
        if (first) first.focus();
      });
    });
    $all("[data-lift-back]", form).forEach(function (button) {
      button.addEventListener("click", function () {
        show(Math.max(0, current - 1));
      });
    });

    var name = $("[data-lift-name]", form);
    name.addEventListener("input", function () {
      var value = name.value.trim();
      owner.textContent = value || owner.dataset.empty;
      owner.classList.toggle("is-blank", !value);
    });

    // After a successful send the lift arrives: the doors open on a welcome with the visitor's name.
    form.addEventListener("submit", function () {
      sentName = name.value.trim().split(/\s+/)[0];
    });
    var status = $("[data-form-status]", form);
    new MutationObserver(function () {
      if (!status.classList.contains("is-success")) return;
      welcome.textContent = sentName;
      stage.classList.add("is-open", "is-arrived");
      rememberSent();
    }).observe(status, { attributes: true, attributeFilter: ["class"] });

    show(0);
    compose();
  }

  /* ---------- Departures board: the clock above the destinations ---------- */

  function initClock() {
    var clock = $("[data-tt-clock]");
    if (!clock) return;
    function tick() {
      var now = new Date();
      clock.textContent = String(now.getHours()).padStart(2, "0") + ":" + String(now.getMinutes()).padStart(2, "0");
    }
    tick();
    setInterval(tick, 15000);
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
    initLetters();
    initHero();
    initForms();
    initDialog();
    initLift();
    initClock();
    initSlidein();
    initReveals();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
