/*
 * Project ad landing pages: hero slideshow, the lead popup, project-type routing, the photo
 * viewer and scroll reveals. Form validation and sending come from site.js and validation.js.
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
    initReveals();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
