/*
 * M3M The Cullinan landing page: the two-step lead form, the lead popup, the room tour,
 * "Cut your own Cullinan", amenity filters, the slider and scroll reveals. Validation and sending
 * come from site.js; the location map is landing-location.js.
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

    // Three seconds after every page open or refresh, offer the price list. It waits if the
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
    $all("[data-cl-form] [data-form-status], [data-cl-cert-form] [data-form-status]").forEach(function (item) {
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
    setTimeout(autoOpen, 3000);
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) dialog.close();
    });
  }

  /* ---------- Room tour (tabs) ---------- */

  // The rooms also step on by themselves every few seconds, a thin line filling under the tab,
  // until the visitor picks a room or points at the tour.
  function initTour() {
    var stage = $("[data-cl-tour]");
    if (!stage) return;
    var tabs = $all('[role="tab"]', stage);
    var timer = null;
    var current = 0;

    function select(tab, focus) {
      tabs.forEach(function (item, index) {
        var on = item === tab;
        if (on) current = index;
        item.setAttribute("aria-selected", on ? "true" : "false");
        item.tabIndex = on ? 0 : -1;
        document.getElementById(item.getAttribute("aria-controls")).hidden = !on;
      });
      if (focus) tab.focus();
    }

    function stop() {
      clearInterval(timer);
      timer = null;
      stage.classList.remove("is-playing");
    }

    function play() {
      if (reduceMotion || timer) return;
      stage.classList.add("is-playing");
      timer = setInterval(function () {
        select(tabs[(current + 1) % tabs.length]);
      }, 5000);
    }

    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting && !stage.dataset.picked) play();
        else stop();
      }, { threshold: 0.4 }).observe(stage);
    }
    stage.addEventListener("pointerenter", stop);
    stage.addEventListener("pointerleave", function () {
      if (!stage.dataset.picked) play();
    });

    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () {
        stage.dataset.picked = "1";
        stop();
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
    var indexLabel = $("[data-cl-slide-index]", slider);
    var progress = $("[data-cl-slide-progress]", slider);
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
      if (indexLabel) indexLabel.textContent = pad(current + 1);
      // Restart the caption's entrance and the progress bar.
      [caption, progress].forEach(function (element) {
        if (!element || reduceMotion) return;
        element.classList.remove("is-running");
        void element.offsetWidth;
        element.classList.add("is-running");
      });
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
    if (progress && !reduceMotion) progress.classList.add("is-running");
  }

  /* ---------- Cut your own Cullinan: four steps grade a certificate, then the lead form ---------- */

  function initCertificate() {
    var stage = $("[data-cl-cert]");
    if (!stage) return;
    var form = $("[data-cl-cert-form]", stage);
    var doc = $("[data-cert-doc]", stage);
    var steps = $all("[data-cert-step]", form);
    var dots = $all(".cl-cert__progress li", form);
    var picked = { carat: null, cut: null, slot: null };
    var current = 0;

    var number = $("[data-cert-no]", doc);
    if (number) number.textContent = "CL-" + String(Math.floor(10000 + Math.random() * 90000));

    // A grade is rewritten with a short shimmer; the diamond gains colour with each one.
    function grade(key, text) {
      var cell = $('[data-cert-grade="' + key + '"]', doc);
      cell.textContent = text;
      cell.classList.remove("is-blank", "is-writing");
      void cell.offsetWidth;
      cell.classList.add("is-writing");
      doc.dataset.graded = $all("[data-cert-grade]:not(.is-blank)", doc).length;
    }

    function show(next) {
      steps[current].hidden = true;
      current = next;
      steps[current].hidden = false;
      dots.forEach(function (dot, position) {
        dot.classList.toggle("is-active", position <= current);
      });
      var focus = current === 3
        ? $("[data-cert-name]", form)
        : $("[aria-pressed='true'], input:checked, button, input", steps[current]);
      if (focus) focus.focus({ preventScroll: true });
    }

    function hideError(step) {
      var error = $("[data-cert-error]", step);
      if (error) error.hidden = true;
    }

    function choose(buttons, button) {
      buttons.forEach(function (other) {
        other.setAttribute("aria-pressed", other === button ? "true" : "false");
      });
      hideError(button.closest("[data-cert-step]"));
    }

    function advanceFrom(step) {
      setTimeout(function () {
        if (current === step) show(step + 1);
      }, 450);
    }

    $all("[data-cert-carat]", form).forEach(function (radio) {
      radio.addEventListener("change", function () {
        picked.carat = radio;
        var commercial = radio.dataset.interest === "commercial";
        $("[data-cert-interest]", form).value = commercial ? "commercial" : "residential";
        $("[data-cert-project]", form).value = commercial ? form.dataset.commercialProject : form.dataset.residentialProject;
        hideError(steps[0]);
        grade("carat", radio.dataset.label);
        advanceFrom(0);
      });
    });

    var cuts = $all("[data-cert-cut]", form);
    cuts.forEach(function (button) {
      button.addEventListener("click", function () {
        choose(cuts, button);
        picked.cut = button.dataset.certCut;
        grade("cut", picked.cut);
        advanceFrom(1);
      });
    });

    var slots = $all("[data-cert-slot]", form);
    slots.forEach(function (button) {
      button.addEventListener("click", function () {
        choose(slots, button);
        picked.slot = button;
        $("[data-cert-time]", form).value = button.dataset.certSlot;
        grade("clarity", button.dataset.label);
        advanceFrom(2);
      });
    });

    function ready(step) {
      return [picked.carat, picked.cut, picked.slot][step] !== null;
    }
    $all("[data-cert-next]", form).forEach(function (button) {
      button.addEventListener("click", function () {
        if (!ready(current)) {
          $("[data-cert-error]", steps[current]).hidden = false;
          return;
        }
        show(current + 1);
      });
    });
    $all("[data-cert-back]", form).forEach(function (button) {
      button.addEventListener("click", function () {
        show(current - 1);
      });
    });

    var name = $("[data-cert-name]", form);
    var owner = $("[data-cert-owner]", doc);
    name.addEventListener("input", function () {
      var typed = name.value.trim();
      owner.textContent = typed || owner.dataset.empty;
      owner.classList.toggle("is-blank", !typed);
    });

    // Runs before site.js sends the form: the sales team reads the choices in the lead's message.
    form.addEventListener("submit", function () {
      $("[data-cert-message]", form).value = [
        form.dataset.request,
        picked.carat ? "Interested in: " + picked.carat.dataset.label : "",
        picked.cut ? "Wants: " + picked.cut : "",
        picked.slot ? "Good time to talk: " + picked.slot.dataset.label : "",
      ].filter(Boolean).join("\n");
    }, true);

    var status = $("[data-form-status]", form);
    new MutationObserver(function () {
      if (status.classList.contains("is-success")) stage.classList.add("is-certified");
    }).observe(status, { attributes: true, attributeFilter: ["class"] });
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
    initCertificate();
    initAmenities();
    initSlider();
    initReveals();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
