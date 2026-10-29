/*
 * Project ad landing pages: hero slideshow, the lead popup, project-type routing, the photo
 * viewer, the residences slideshow, the private line, the viewing pass and scroll reveals.
 * The location map is landing-location.js. Form validation and sending come from site.js and validation.js.
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

  /* ---------- Hero slideshow ---------- */

  function initHero() {
    var slides = $all(".jl-hero__slide");
    var dots = $all(".jl-hero__dots li");
    if (slides.length < 2 || reduceMotion) return;
    var current = 0;
    setInterval(function () {
      slides[current].classList.remove("is-active");
      if (dots[current]) dots[current].classList.remove("is-active");
      current = (current + 1) % slides.length;
      slides[current].classList.add("is-active");
      if (dots[current]) dots[current].classList.add("is-active");
    }, 6000);
  }

  /* ---------- Lead forms ---------- */

  // Commercial leads are filed against the commercial project, so they reach the right sales team.
  function routeProject(form) {
    var interest = $("[data-jl-interest]", form);
    var project = $("[data-jl-project]", form);
    if (!interest || !project) return;
    var commercial = form.dataset.commercialProject;
    project.value = interest.value === "commercial" && commercial ? commercial : form.dataset.residentialProject;
  }

  function initForms() {
    $all("[data-jl-form]").forEach(function (form) {
      var interest = $("[data-jl-interest]", form);
      if (interest) {
        interest.addEventListener("change", function () {
          routeProject(form);
        });
      }
      // Runs before site.js sends the form, so the project and request are always current.
      form.addEventListener("submit", function () {
        routeProject(form);
      }, true);
    });
  }

  function initDialog() {
    var dialog = $("[data-jl-dialog]");
    if (!dialog) return;
    var title = $("[data-jl-dialog-title]", dialog);

    function open(label, preset) {
      title.textContent = label;
      // The popup shows the next of the three form styles each time (landing-forms.js).
      var form = window.LandingForms.prepare(label, preset);
      if (!dialog.open) dialog.showModal();
      var first = window.LandingForms.firstControl(form);
      if (first) first.focus();
    }

    document.addEventListener("click", function (event) {
      var trigger = event.target.closest("[data-jl-open]");
      if (!trigger) return;
      event.preventDefault();
      var preset = trigger.dataset.jlUnitPreset || (trigger.dataset.jlInterestPreset === "commercial" ? "retail" : "");
      open(trigger.dataset.jlOpen, preset);
    });

    // The site's floating "Enquire" button opens this page's short form instead of the general one.
    $all(".floating-actions [data-enquiry-open]").forEach(function (button) {
      button.removeAttribute("data-enquiry-open");
      button.setAttribute("data-jl-open", "Request a callback");
    });

    $all("[data-jl-close]").forEach(function (button) {
      button.addEventListener("click", function () {
        button.closest("dialog").close();
      });
    });
    $all("dialog.jl-dialog, dialog.jl-viewer").forEach(function (box) {
      box.addEventListener("click", function (event) {
        if (event.target === box) box.close();
      });
    });

    // Automatic offer 4 seconds after every page load or refresh. Never while the visitor is
    // typing in a form or viewing a photo, and never again once they have sent their details.
    var SENT_KEY = "jacob-lead-sent";
    function sent() {
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
        // Private browsing: the offer may show again on the next page load.
      }
    }
    document.addEventListener("landing:sent", markSent);
    $all("[data-jl-form] [data-form-status]").forEach(function (status) {
      new MutationObserver(function () {
        if (status.classList.contains("is-success")) markSent();
      }).observe(status, { attributes: true, attributeFilter: ["class"] });
    });
    setTimeout(function () {
      if (sent() || dialog.open || document.querySelector("dialog[open]")) return;
      var active = document.activeElement;
      if (active && active.closest && active.closest("form")) return;
      open("Unlock the brochure & price list");
    }, 4000);
  }

  /* ---------- Photo viewer ---------- */

  function initViewer() {
    var viewer = $("[data-jl-viewer]");
    if (!viewer) return;
    var image = $("[data-jl-viewer-image]", viewer);
    var caption = $("[data-jl-viewer-caption]", viewer);
    $all("[data-jl-photo]").forEach(function (button) {
      button.addEventListener("click", function () {
        image.src = button.dataset.jlPhoto;
        image.alt = button.dataset.caption + ", artistic impression";
        caption.textContent = button.dataset.caption;
        viewer.showModal();
      });
    });
  }

  /* ---------- Residences slideshow ---------- */

  function initResidenceShow() {
    var show = $("[data-jl-res-show]");
    if (!show) return;
    var slides = $all(".jl-residences__slides img", show);
    var thumbs = $all(".jl-residences__thumbs button", show);
    var caption = $("[data-jl-res-caption]", show);
    var index = $("[data-jl-res-index]", show);
    if (slides.length < 2) return;
    var current = 0;
    var timer = null;

    function go(next) {
      slides[current].classList.remove("is-active");
      if (thumbs[current]) {
        thumbs[current].classList.remove("is-active");
        thumbs[current].setAttribute("aria-pressed", "false");
      }
      current = (next + slides.length) % slides.length;
      slides[current].classList.add("is-active");
      if (thumbs[current]) {
        thumbs[current].classList.add("is-active");
        thumbs[current].setAttribute("aria-pressed", "true");
      }
      if (caption) caption.textContent = slides[current].dataset.caption || "";
      if (index) index.textContent = String(current + 1).padStart(2, "0");
    }

    function play() {
      if (reduceMotion) return;
      clearInterval(timer);
      timer = setInterval(function () {
        go(current + 1);
      }, 4500);
    }

    thumbs.forEach(function (thumb, position) {
      thumb.addEventListener("click", function () {
        go(position);
        play();
      });
    });
    show.addEventListener("pointerenter", function () {
      clearInterval(timer);
    });
    show.addEventListener("pointerleave", play);
    play();
  }

  /* ---------- The private line: three steps that compose a letter, then a normal lead form ---------- */

  function initPrivateLine() {
    var stage = $("[data-jl-private]");
    if (!stage) return;
    var form = $("form", stage);
    var steps = $all("[data-jl-pl-step]", form);
    var dots = $all(".jl-private__progress li", form);
    var letter = $("[data-jl-letter]", stage);
    var letterName = $("[data-jl-letter-name]", letter);
    var letterChoice = $("[data-jl-letter-choice]", letter);
    var letterTime = $("[data-jl-letter-time]", letter);
    var picked = { choice: null, slot: null };
    var current = 0;

    var date = $("[data-jl-letter-date]", letter);
    if (date) {
      date.textContent = new Date().toLocaleDateString("en-IN", { day: "numeric", month: "long", year: "numeric" });
    }

    // A word of the letter is rewritten with a short ink effect.
    function write(element, text) {
      if (!element || element.textContent === text) return;
      element.textContent = text;
      element.classList.toggle("is-blank", text === element.dataset.blank);
      element.classList.remove("is-writing");
      void element.offsetWidth;
      element.classList.add("is-writing");
    }

    function show(next) {
      steps[current].hidden = true;
      current = next;
      steps[current].hidden = false;
      dots.forEach(function (dot, position) {
        dot.classList.toggle("is-active", position <= current);
      });
      var first = $("[aria-pressed='true'], button, input", steps[current]);
      if (current === 2) first = $("input[name=name]", form);
      if (first) first.focus({ preventScroll: true });
    }

    function pick(buttons, button) {
      buttons.forEach(function (other) {
        other.setAttribute("aria-pressed", other === button ? "true" : "false");
      });
      var error = $("[data-jl-pl-error]", button.closest("[data-jl-pl-step]"));
      if (error) error.hidden = true;
    }

    letterTime.dataset.blank = letterTime.textContent;
    letterChoice.dataset.blank = letterChoice.textContent;

    var choices = $all("[data-jl-pl-choice]", form);
    choices.forEach(function (button) {
      button.addEventListener("click", function () {
        pick(choices, button);
        picked.choice = button;
        write(letterChoice, button.dataset.letter);
        setTimeout(function () {
          if (current === 0) show(1);
        }, 450);
      });
    });

    var slots = $all("[data-jl-pl-slot]", form);
    slots.forEach(function (button) {
      button.addEventListener("click", function () {
        pick(slots, button);
        picked.slot = button;
        $("[data-jl-pl-call-time]", form).value = button.dataset.jlPlSlot;
        write(letterTime, button.dataset.letter);
      });
    });

    function ready(step) {
      if (step === 0) return Boolean(picked.choice);
      if (step === 1) return Boolean(picked.slot);
      return true;
    }

    $all("[data-jl-pl-next]", form).forEach(function (button) {
      button.addEventListener("click", function () {
        if (!ready(current)) {
          $("[data-jl-pl-error]", steps[current]).hidden = false;
          return;
        }
        show(current + 1);
      });
    });
    $all("[data-jl-pl-back]", form).forEach(function (button) {
      button.addEventListener("click", function () {
        show(current - 1);
      });
    });

    var name = $("[data-jl-pl-name]", form);
    name.addEventListener("input", function () {
      var first = name.value.trim().split(/\s+/)[0];
      letterName.textContent = first || letterName.dataset.empty;
    });

    // Runs before site.js sends the form: the sales team gets the choices in the lead's message.
    form.addEventListener("submit", function () {
      if (!picked.choice) return;
      $("[data-jl-pl-message]", form).value = [
        form.dataset.request,
        "Wants: " + picked.choice.dataset.jlPlChoice,
        "Good time to talk: " + (picked.slot ? picked.slot.dataset.label : ""),
      ].join("\n");
    }, true);

    var status = $("[data-form-status]", form);
    new MutationObserver(function () {
      if (!status.classList.contains("is-success")) return;
      stage.classList.add("is-sealed");
    }).observe(status, { attributes: true, attributeFilter: ["class"] });
  }

  /* ---------- Private site visit pass: day tiles for the next two weeks, a time, then the lead form ---------- */

  function initViewingPass() {
    var pass = $("[data-jl-pass]");
    if (!pass) return;
    var dateInput = $("[data-jl-pass-date]", pass);
    var timeInput = $("[data-jl-pass-time]", pass);
    var dayList = $("[data-jl-pass-days]", pass);
    var timeLabel = "";

    function clearError(input) {
      input.setAttribute("aria-invalid", "false");
      var error = document.getElementById(input.dataset.errorId);
      if (error) error.hidden = true;
    }

    function choose(buttons, button) {
      buttons.forEach(function (other) {
        other.setAttribute("aria-pressed", other === button ? "true" : "false");
      });
    }

    var number = $("[data-jl-pass-no]", pass);
    if (number) number.textContent = "JC-" + String(Math.floor(1000 + Math.random() * 9000));

    // Tomorrow onwards, fourteen days. The value is the local date, as the server expects (YYYY-MM-DD).
    var days = [];
    for (var offset = 1; offset <= 14; offset += 1) {
      var date = new Date();
      date.setDate(date.getDate() + offset);
      var iso = [date.getFullYear(), String(date.getMonth() + 1).padStart(2, "0"), String(date.getDate()).padStart(2, "0")].join("-");
      var day = document.createElement("button");
      day.type = "button";
      day.className = "jl-pass__day";
      day.setAttribute("aria-pressed", "false");
      day.dataset.date = iso;
      day.setAttribute("aria-label", date.toLocaleDateString("en-IN", { weekday: "long", day: "numeric", month: "long" }));
      day.innerHTML =
        "<small>" + date.toLocaleDateString("en-IN", { weekday: "short" }) + "</small>" +
        "<strong>" + date.getDate() + "</strong>" +
        "<small>" + date.toLocaleDateString("en-IN", { month: "short" }) + "</small>";
      dayList.appendChild(day);
      days.push(day);
    }
    days.forEach(function (day) {
      day.addEventListener("click", function () {
        choose(days, day);
        dateInput.value = day.dataset.date;
        clearError(dateInput);
      });
    });

    var slots = $all("[data-jl-pass-slot]", pass);
    slots.forEach(function (slot) {
      slot.addEventListener("click", function () {
        choose(slots, slot);
        timeInput.value = slot.dataset.jlPassSlot;
        timeLabel = slot.dataset.label;
        clearError(timeInput);
      });
    });

    // Runs before site.js sends the form: the sales team sees the visit time in the lead's message.
    pass.addEventListener("submit", function () {
      $("[data-jl-pass-message]", pass).value = [pass.dataset.request, timeLabel ? "Visit time: " + timeLabel : ""]
        .filter(Boolean)
        .join("\n");
    }, true);

    var status = $("[data-form-status]", pass);
    new MutationObserver(function () {
      if (!status.classList.contains("is-success")) return;
      pass.classList.add("is-confirmed");
      choose(days, null);
      choose(slots, null);
    }).observe(status, { attributes: true, attributeFilter: ["class"] });
  }

  /* ---------- Scroll reveals ---------- */

  function initReveals() {
    var items = $all(".jl-reveal");
    if (reduceMotion || !("IntersectionObserver" in window)) return;
    items.forEach(function (item) {
      item.style.opacity = "0";
      item.style.transform = "translateY(30px)";
      item.style.transition = "opacity 900ms ease, transform 1100ms cubic-bezier(0.16, 1, 0.3, 1)";
    });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.style.opacity = "";
        entry.target.style.transform = "";
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
    initViewer();
    initResidenceShow();
    initPrivateLine();
    initViewingPass();
    initReveals();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
