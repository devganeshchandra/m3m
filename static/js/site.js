/*
 * M3M India site behaviour. Each block below replaces one of the old React
 * components; they share a few helpers and run once the DOM is ready.
 */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var lenis = null;

  function $(selector, root) {
    return (root || document).querySelector(selector);
  }

  function $all(selector, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(selector));
  }

  function pad2(number) {
    return String(number).padStart(2, "0");
  }

  /* ---------- Campaign tracking (UTM) for lead forms ---------- */

  function initTracking() {
    var keys = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"];
    var params = new URLSearchParams(window.location.search);
    var stored = {};
    try {
      stored = JSON.parse(sessionStorage.getItem("m3m-utm") || "{}");
    } catch (error) {
      stored = {};
    }
    if (keys.some(function (key) { return params.has(key); })) {
      stored = {};
      keys.forEach(function (key) {
        if (params.get(key)) stored[key] = params.get(key).slice(0, 120);
      });
      try {
        sessionStorage.setItem("m3m-utm", JSON.stringify(stored));
      } catch (error) {
        /* Storage unavailable: values still go with this page's forms. */
      }
    }
    $all("input[data-utm]").forEach(function (input) {
      input.value = stored[input.name] || "";
    });
    $all("input[data-page-url]").forEach(function (input) {
      input.value = window.location.href.slice(0, 1000);
    });
  }

  /* ---------- Header ---------- */

  function initHeader() {
    var header = $("[data-site-header]");
    if (!header) return;
    var logo = $(".wordmark__logo", header);
    var scrolled = null;

    function update() {
      var next = window.scrollY > 24;
      if (next === scrolled) return;
      scrolled = next;
      header.classList.toggle("site-header--scrolled", scrolled);
      logo.src = scrolled ? logo.dataset.logoTransparent : logo.dataset.logoColor;
      logo.classList.toggle("wordmark__logo--transparent", scrolled);
      logo.classList.toggle("wordmark__logo--color", !scrolled);
    }

    update();
    window.addEventListener("scroll", update, { passive: true });

    var homeLink = $("[data-home-link]");
    homeLink.addEventListener("click", function (event) {
      if (window.location.pathname !== "/") return;
      event.preventDefault();
      if (window.location.hash) {
        history.replaceState(history.state, "", window.location.pathname + window.location.search);
      }
      scrollToTop();
    });
  }

  /* ---------- Smooth scrolling (Lenis + GSAP ScrollTrigger) ---------- */

  function initSmoothScroll() {
    if (reduceMotion || !window.Lenis || !window.gsap) return;
    if (window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);
    lenis = new Lenis({ autoRaf: false, lerp: 0.08 });
    if (window.ScrollTrigger) lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(function (time) {
      lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);
  }

  function scrollToTop() {
    if (lenis) lenis.scrollTo(0, { immediate: true, force: true });
    else window.scrollTo({ top: 0, behavior: "instant" });
  }

  function initAnchorLinks() {
    document.addEventListener("click", function (event) {
      var link = event.target.closest('a[href^="/#"], a[href^="#"]');
      if (!link || event.defaultPrevented || event.metaKey || event.ctrlKey || event.shiftKey) return;
      var hash = link.getAttribute("href").replace(/^\//, "");
      if (link.getAttribute("href").charAt(0) === "/" && window.location.pathname !== "/") return;
      var target = hash.length > 1 ? document.getElementById(hash.slice(1)) : null;
      if (!target) return;
      event.preventDefault();
      history.pushState(history.state, "", hash);
      // Both Lenis and scrollIntoView respect the CSS scroll-margin-top.
      if (lenis) lenis.scrollTo(target);
      else target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth" });
    });

    // Arriving from another page (e.g. /#media): the browser jumps before the
    // page-enter animation finishes, so re-align once it has.
    var shell = $(".page-shell");
    var initialTarget = window.location.hash.length > 1 && document.getElementById(window.location.hash.slice(1));
    if (shell && initialTarget) {
      shell.addEventListener("animationend", function () {
        if (lenis) lenis.scrollTo(initialTarget, { immediate: true, force: true });
        else initialTarget.scrollIntoView();
      }, { once: true });
    }
  }

  function pauseScroll(paused) {
    if (!lenis) return;
    if (paused) lenis.stop();
    else lenis.start();
  }

  /* ---------- Custom cursor ---------- */

  function initCursor() {
    var cursor = $(".custom-cursor");
    if (!cursor || !window.matchMedia("(pointer: fine)").matches || reduceMotion) return;
    var label = cursor.firstElementChild;

    window.addEventListener(
      "pointermove",
      function (event) {
        cursor.style.setProperty("--cursor-x", event.clientX + "px");
        cursor.style.setProperty("--cursor-y", event.clientY + "px");
        cursor.dataset.visible = "true";
        var labelled = event.target instanceof Element ? event.target.closest("[data-cursor-label]") : null;
        var text = labelled ? labelled.dataset.cursorLabel : "";
        cursor.dataset.label = text;
        cursor.dataset.active = labelled ? "true" : "false";
        label.textContent = text;
      },
      { passive: true },
    );
    document.documentElement.addEventListener("pointerleave", function () {
      cursor.dataset.visible = "false";
    });
  }

  /* ---------- Form helpers ---------- */

  function errorElementFor(control) {
    return control.dataset.errorId ? document.getElementById(control.dataset.errorId) : null;
  }

  function setError(control, message) {
    var errorElement = errorElementFor(control);
    if (control.type !== "radio") {
      control.setAttribute("aria-invalid", message ? "true" : "false");
    }
    if (!errorElement) return;
    errorElement.textContent = message || "";
    errorElement.hidden = !message;
    var hintId = control.dataset.hintId;
    var describedBy = message ? errorElement.id : hintId;
    if (describedBy) control.setAttribute("aria-describedby", describedBy);
    else control.removeAttribute("aria-describedby");
  }

  function setGroupError(id, message) {
    var element = document.getElementById(id);
    if (!element) return;
    element.textContent = message || "";
    element.hidden = !message;
  }

  function setStatus(form, message, success) {
    var status = $("[data-form-status]", form);
    if (!status) return;
    status.classList.toggle("is-success", Boolean(success));
    status.textContent = "";
    if (!message) return;
    if (status.classList.contains("enquiry-form__status")) {
      var paragraph = document.createElement("p");
      paragraph.textContent = message;
      status.appendChild(paragraph);
    } else {
      status.textContent = message;
    }
  }

  function clearForm(form) {
    $all("[data-validate]", form).forEach(function (control) {
      setError(control, "");
    });
    $all(".guided-card__error", form).forEach(function (element) {
      element.textContent = "";
      element.hidden = true;
    });
    setStatus(form, "");
  }

  function validateControls(controls) {
    var firstInvalid = null;
    controls.forEach(function (control) {
      var message = M3MValidation.validateControl(control);
      setError(control, message);
      if (message && !firstInvalid) firstInvalid = control;
    });
    return firstInvalid;
  }

  function submitLead(form, onSuccess) {
    var button = $('button[type="submit"]', form);
    form.setAttribute("aria-busy", "true");
    button.disabled = true;
    setStatus(form, "");

    fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
      credentials: "same-origin",
    })
      .then(function (response) {
        return response.json().catch(function () {
          return { ok: false };
        });
      })
      .then(function (data) {
        if (data.ok) {
          onSuccess();
          setStatus(form, data.message, true);
          return;
        }
        var first = null;
        Object.keys(data.errors || {}).forEach(function (field) {
          var control = $('[name="' + field + '"]', form);
          if (control && control.dataset.validate) {
            setError(control, data.errors[field]);
            if (!first) first = control;
          }
        });
        if (first) first.focus();
        setStatus(
          form,
          data.message ||
            (first ? "" : "Something went wrong sending your details. Please call or WhatsApp our team."),
        );
      })
      .catch(function () {
        setStatus(form, "We couldn’t reach our server. Please check your connection, or call or WhatsApp our team.");
      })
      .finally(function () {
        form.removeAttribute("aria-busy");
        button.disabled = false;
      });
  }

  function resetLeadFields(form) {
    $all("[data-validate]", form).forEach(function (control) {
      if (control.type === "checkbox") control.checked = false;
      else control.value = "";
    });
  }

  /* ---------- Hero form and enquiry popup ---------- */

  function initLeadForm(form) {
    $all("[data-validate]", form).forEach(function (control) {
      if (control.hasAttribute("data-validate-on-submit")) return;
      var eventName = control.tagName === "SELECT" || control.type === "checkbox" ? "change" : "input";
      control.addEventListener(eventName, function () {
        setError(control, M3MValidation.validateControl(control));
        setStatus(form, "");
      });
      if (control.type !== "checkbox" && !control.hasAttribute("data-no-blur-validate")) {
        control.addEventListener("blur", function () {
          setError(control, M3MValidation.validateControl(control));
        });
      }
    });

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      setStatus(form, "");
      var firstInvalid = validateControls($all("[data-validate]", form));
      if (firstInvalid) {
        firstInvalid.focus();
        return;
      }
      submitLead(form, function () {
        resetLeadFields(form);
      });
    });
  }

  function initEnquiryDialog() {
    var dialog = $("[data-enquiry-dialog]");
    if (!dialog) return;
    var form = $("form", dialog);
    var projectInput = $("[data-enquiry-project]", dialog);
    var projectName = $("[data-enquiry-project-name]", dialog);
    dialog.setAttribute("data-lenis-prevent", "");

    document.addEventListener("click", function (event) {
      var trigger = event.target.closest("[data-enquiry-open]");
      if (!trigger) return;
      form.reset();
      initTracking();
      clearForm(form);
      projectInput.value = trigger.dataset.project || "";
      projectName.textContent = trigger.dataset.projectName || "M3M residences";
      if (!dialog.open) dialog.showModal();
      pauseScroll(true);
    });

    $("[data-enquiry-close]", dialog).addEventListener("click", function () {
      dialog.close();
    });
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) dialog.close();
    });
    dialog.addEventListener("close", function () {
      pauseScroll(false);
    });
  }

  /* ---------- Hero banner carousel ---------- */

  function initCarousel() {
    var carousel = $("[data-hero-carousel]");
    if (!carousel) return;
    var slides = $all(".hero-banner__slide", carousel);
    if (slides.length < 2) return;
    var dots = $all("[data-carousel-dot]", carousel);
    var toggle = $("[data-carousel-toggle]", carousel);
    var status = $("[data-carousel-status]", carousel);
    var active = 0;
    var paused = reduceMotion;
    var timer = null;

    function show(index) {
      active = index;
      slides.forEach(function (slide, i) {
        slide.classList.toggle("is-active", i === index);
      });
      dots.forEach(function (dot, i) {
        dot.setAttribute("aria-pressed", i === index ? "true" : "false");
      });
      status.textContent = "Banner " + (index + 1) + " of " + slides.length;
    }

    function schedule() {
      clearInterval(timer);
      if (paused) return;
      timer = setInterval(function () {
        show((active + 1) % slides.length);
      }, 6500);
    }

    function renderToggle() {
      toggle.textContent = paused ? "Play" : "Pause";
      toggle.setAttribute("aria-label", paused ? "Play banners" : "Pause banners");
      status.setAttribute("aria-live", paused ? "polite" : "off");
    }

    toggle.addEventListener("click", function () {
      paused = !paused;
      renderToggle();
      schedule();
    });
    dots.forEach(function (dot) {
      dot.addEventListener("click", function () {
        show(Number(dot.dataset.carouselDot));
      });
    });
    renderToggle();
    schedule();
  }

  /* ---------- Our Journey values ---------- */

  function initJourney() {
    var root = $("[data-journey]");
    if (!root) return;
    var items = $all("[data-journey-item]", root);
    var panel = $("[data-journey-panel]", root);

    items.forEach(function (item) {
      item.addEventListener("click", function () {
        var index = Number(item.dataset.journeyItem);
        items.forEach(function (other) {
          var selected = other === item;
          other.classList.toggle("is-active", selected);
          other.setAttribute("aria-pressed", selected ? "true" : "false");
        });
        panel.setAttribute("aria-labelledby", item.id);
        $("[data-journey-mark]", panel).textContent = "0" + (index + 1);
        $("[data-journey-title]", panel).textContent = item.dataset.title;
        $("[data-journey-description]", panel).textContent = item.dataset.description;
      });
    });
  }

  /* ---------- Press dialog ---------- */

  function initPress() {
    var dialog = $("[data-press-dialog]");
    if (!dialog) return;
    dialog.setAttribute("data-lenis-prevent", "");

    $all("[data-press-open]").forEach(function (card) {
      card.addEventListener("click", function () {
        var data = card.dataset;
        $("[data-press-meta]", dialog).textContent = data.source + " · " + data.date;
        $("[data-press-title]", dialog).textContent = data.title;
        $("[data-press-summary]", dialog).textContent = data.summary;
        $("[data-press-link]", dialog).href = data.url;
        $("[data-press-link-label]", dialog).textContent = "Read the full story on " + data.source;
        var logo = $("[data-press-logo]", dialog);
        logo.hidden = !data.logo;
        if (data.logo) {
          logo.src = data.logo;
          logo.alt = data.source;
        }
        dialog.showModal();
        pauseScroll(true);
      });
    });
    $("[data-press-close]", dialog).addEventListener("click", function () {
      dialog.close();
    });
    dialog.addEventListener("close", function () {
      pauseScroll(false);
    });
  }

  /* ---------- Personalised project discovery ---------- */

  function initGuided() {
    var form = $("[data-guided-form]");
    if (!form) return;

    var interestInputs = $all('input[name="interest"]', form);
    var projectInputs = $all('input[name="project"]', form);
    var residencyInputs = $all('input[name="residency"]', form);
    var contactControls = ["phone", "email", "consent"].map(function (name) {
      return $('[name="' + name + '"]', form);
    });
    var preview = $("[data-guided-preview]", form);
    var previewName = $("[data-guided-preview-name]", preview);
    var previewMeta = $("[data-guided-preview-meta]", preview);
    var emptyName = previewName.textContent;
    var emptyMeta = previewMeta.textContent;

    function checked(inputs) {
      return inputs.filter(function (input) { return input.checked; })[0] || null;
    }

    function markSelected(inputs) {
      inputs.forEach(function (input) {
        input.closest("label").classList.toggle("is-selected", input.checked);
      });
    }

    function interestsOf(input) {
      return input.dataset.interests.split(" ");
    }

    // Show only the projects that match the chosen direction (all of them before a choice).
    function filterProjects() {
      var interest = checked(interestInputs);
      var count = 0;
      projectInputs.forEach(function (input) {
        var show = !interest || interestsOf(input).indexOf(interest.value) !== -1;
        input.closest("label").hidden = !show;
        if (!show) input.checked = false;
        if (show) count += 1;
      });
      $("[data-guided-match-count]", form).textContent = count;
    }

    function renderPreview() {
      var project = checked(projectInputs);
      var link = $("[data-guided-preview-link]", preview);
      preview.classList.toggle("is-filled", Boolean(project));
      $("[data-guided-preview-empty]", preview).hidden = Boolean(project);
      $("[data-guided-preview-image]", preview).innerHTML = project ? project.dataset.imageHtml : "";
      link.hidden = !project;
      if (!project) {
        previewName.textContent = emptyName;
        previewMeta.textContent = emptyMeta;
        return;
      }
      var residency = checked(residencyInputs);
      previewName.textContent = project.dataset.name;
      previewMeta.textContent = [
        project.dataset.location,
        project.dataset.offering,
        residency ? (residency.value === "nri" ? "For an overseas buyer" : "For a buyer in India") : "",
      ].filter(Boolean).join(" · ");
      link.href = project.dataset.url;
    }

    function renderProgress() {
      var contactDone = contactControls[0].value.trim() && contactControls[1].value.trim();
      var done = [checked(interestInputs), checked(projectInputs), checked(residencyInputs), contactDone]
        .filter(Boolean).length;
      $("[data-guided-progress-count]", form).textContent = done;
      $("[data-guided-progress-bar]", form).style.width = (done / 4) * 100 + "%";
    }

    function update() {
      filterProjects();
      markSelected(interestInputs);
      markSelected(projectInputs);
      markSelected(residencyInputs);
      renderPreview();
      renderProgress();
    }

    interestInputs.forEach(function (input) {
      input.addEventListener("change", function () {
        setGroupError("guided-interest-error", "");
        setStatus(form, "");
        update();
      });
    });

    projectInputs.forEach(function (input) {
      input.addEventListener("change", function () {
        // Picking a project first also picks its direction.
        if (!checked(interestInputs)) {
          var match = interestInputs.filter(function (option) {
            return option.value === interestsOf(input)[0];
          })[0];
          if (match) match.checked = true;
          setGroupError("guided-interest-error", "");
        }
        setGroupError("guided-project-error", "");
        setStatus(form, "");
        update();
      });
    });

    residencyInputs.forEach(function (input) {
      input.addEventListener("change", function () {
        setGroupError("guided-residency-error", "");
        setStatus(form, "");
        update();
      });
    });

    contactControls.forEach(function (control) {
      control.addEventListener(control.type === "checkbox" ? "change" : "input", function () {
        setError(control, "");
        setStatus(form, "");
        renderProgress();
      });
    });

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      setStatus(form, "");
      var firstInvalid = null;
      var groups = [
        [interestInputs, "interest", "Choose what you’re looking for."],
        [projectInputs, "project", "Choose an address for your M3M edit."],
        [residencyInputs, "residency", "Choose where you’re based."],
      ];
      groups.forEach(function (group) {
        var missing = !checked(group[0]);
        setGroupError("guided-" + group[1] + "-error", missing ? group[2] : "");
        if (missing && !firstInvalid) {
          firstInvalid = group[0].filter(function (input) { return !input.closest("label").hidden; })[0];
        }
      });
      var invalidContact = validateControls(contactControls);
      firstInvalid = firstInvalid || invalidContact;
      if (firstInvalid) {
        firstInvalid.focus();
        return;
      }
      submitLead(form, function () {
        resetLeadFields(form);
        renderProgress();
      });
    });

    form.addEventListener("reset", function () {
      setTimeout(update);
    });

    update();
  }

  /* ---------- Menu pages ---------- */

  function setPressed(buttons, active) {
    buttons.forEach(function (button) {
      var on = button === active;
      button.classList.toggle("is-active", on);
      button.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  // Filter pills: `group` holds buttons with data-filter; `apply(value)` does the filtering.
  function initFilterGroup(group, apply) {
    if (!group) return;
    var buttons = $all("[data-filter]", group);
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        setPressed(buttons, button);
        apply(button.dataset.filter);
      });
    });
    $all("[data-filter-reset]").forEach(function (reset) {
      reset.addEventListener("click", function () {
        setPressed(buttons, buttons[0]);
        apply("all");
      });
    });
  }

  function initProjectFilter() {
    var group = $("[data-project-filter]");
    initFilterGroup(group, function (value) {
      $all("[data-collection]").forEach(function (section) {
        var cards = $all(".project-card", section);
        var shown = 0;
        cards.forEach(function (card) {
          var match = value === "all" || card.dataset.interests.split(" ").indexOf(value) !== -1;
          card.hidden = !match;
          if (match) shown += 1;
        });
        $all('[data-collection-count="' + section.id + '"]').forEach(function (count) {
          count.textContent = shown;
        });
        var empty = $("[data-filter-empty]", section);
        if (empty) empty.hidden = !(cards.length && shown === 0);
      });
    });
  }

  function initScrollspy() {
    var links = $all("[data-scrollspy-link]");
    if (!links.length || !("IntersectionObserver" in window)) return;
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var key = entry.target.dataset.scrollspySection;
          links.forEach(function (link) {
            link.classList.toggle("is-active", link.dataset.scrollspyLink === key);
          });
        });
      },
      { rootMargin: "-45% 0px -50% 0px" },
    );
    $all("[data-scrollspy-section]").forEach(function (section) {
      observer.observe(section);
    });
  }

  function initGallery() {
    var gallery = $("[data-gallery]");
    if (!gallery) return;
    var items = $all(".masonry__item", gallery);

    initFilterGroup($("[data-gallery-filter]"), function (value) {
      items.forEach(function (item) {
        item.hidden = value !== "all" && item.dataset.category !== value;
      });
    });

    var lightbox = $("[data-lightbox]");
    if (!lightbox) return;
    lightbox.setAttribute("data-lenis-prevent", "");
    var image = $("[data-lightbox-image]", lightbox);
    var current = 0;

    function visibleButtons() {
      return items
        .filter(function (item) { return !item.hidden; })
        .map(function (item) { return $("[data-lightbox-open]", item); });
    }

    function show(index) {
      var buttons = visibleButtons();
      if (!buttons.length) return;
      current = (index + buttons.length) % buttons.length;
      var data = buttons[current].dataset;
      image.src = data.src;
      image.alt = data.caption;
      $("[data-lightbox-caption]", lightbox).textContent = data.caption;
      $("[data-lightbox-category]", lightbox).textContent = data.categoryLabel;
      $("[data-lightbox-count]", lightbox).textContent = current + 1 + " / " + buttons.length;
    }

    gallery.addEventListener("click", function (event) {
      var button = event.target.closest("[data-lightbox-open]");
      if (!button) return;
      show(visibleButtons().indexOf(button));
      lightbox.showModal();
      pauseScroll(true);
    });
    $("[data-lightbox-prev]", lightbox).addEventListener("click", function () { show(current - 1); });
    $("[data-lightbox-next]", lightbox).addEventListener("click", function () { show(current + 1); });
    $("[data-lightbox-close]", lightbox).addEventListener("click", function () { lightbox.close(); });
    lightbox.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft") show(current - 1);
      if (event.key === "ArrowRight") show(current + 1);
    });
    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox) lightbox.close();
    });
    lightbox.addEventListener("close", function () {
      pauseScroll(false);
    });
  }

  function initInsightFilter() {
    var grid = $("[data-insight-grid]");
    if (!grid) return;
    var cards = $all(".insight-card", grid);
    var empty = $("[data-filter-empty]", grid.parentElement);
    initFilterGroup($("[data-insight-filter]"), function (value) {
      var shown = 0;
      cards.forEach(function (card) {
        card.hidden = value !== "all" && card.dataset.category !== value;
        if (!card.hidden) shown += 1;
      });
      if (empty) empty.hidden = shown > 0;
    });
  }

  function initVideos() {
    $all("[data-video-id]").forEach(function (player) {
      player.addEventListener("click", function () {
        var frame = document.createElement("iframe");
        frame.src = "https://www.youtube-nocookie.com/embed/" + player.dataset.videoId + "?autoplay=1&rel=0";
        frame.title = player.getAttribute("aria-label");
        frame.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
        frame.allowFullscreen = true;
        player.replaceChildren(frame);
        player.removeAttribute("aria-label");
      }, { once: true });
    });
  }

  function initCopyLink() {
    $all("[data-copy-link]").forEach(function (button) {
      button.addEventListener("click", function () {
        var done = function () {
          button.textContent = "✓";
          setTimeout(function () { button.textContent = "Link"; }, 2000);
        };
        if (navigator.clipboard) navigator.clipboard.writeText(window.location.href).then(done);
      });
    });
  }

  function initReveal() {
    if (reduceMotion || !("IntersectionObserver" in window)) return;
    var targets = $all(
      ".inner-page .project-card, .value-card, .timeline__item, .masonry__item, .story__collage, " +
        ".inner-page .insight-card, .article-page .insight-card, .feature-article, .contact-form-card, .faq__item, " +
        "[data-bbt-reveal]",
    );
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px" },
    );
    targets.forEach(function (target, index) {
      target.setAttribute("data-reveal", "");
      target.style.transitionDelay = (index % 3) * 90 + "ms";
      observer.observe(target);
    });
  }

  // Whole-number figures count up the first time they scroll into view.
  function initCountUp() {
    var figures = $all("[data-count-up]").filter(function (figure) {
      return /^\d+$/.test(figure.textContent.trim());
    });
    if (!figures.length || reduceMotion || !("IntersectionObserver" in window)) return;

    function run(figure) {
      var target = Number(figure.textContent.trim());
      // Years count over their last few years; other figures count from zero.
      var start = target >= 1900 ? target - 16 : 0;
      var began = null;
      function frame(time) {
        began = began || time;
        var progress = Math.min((time - began) / 1600, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        figure.textContent = String(Math.round(start + (target - start) * eased));
        if (progress < 1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        run(entry.target);
      });
    }, { threshold: 0.6 });
    figures.forEach(function (figure) {
      observer.observe(figure);
    });
  }

  function initTeaserVideo() {
    var video = $("[data-bbt-video]");
    if (!video) return;
    if (reduceMotion) {
      video.removeAttribute("autoplay");
      video.pause();
      return;
    }
    if (!("IntersectionObserver" in window)) return;
    new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) video.play().catch(function () {});
        else video.pause();
      });
    }).observe(video);
  }

  /* ---------- Start ---------- */

  function init() {
    initTracking();
    initSmoothScroll();
    initHeader();
    initAnchorLinks();
    initCursor();
    initCarousel();
    initJourney();
    initPress();
    initEnquiryDialog();
    $all("[data-lead-form]").forEach(function (form) {
      if (!form.hasAttribute("data-guided-form")) initLeadForm(form);
    });
    initGuided();
    initProjectFilter();
    initScrollspy();
    initGallery();
    initInsightFilter();
    initVideos();
    initCopyLink();
    initReveal();
    initCountUp();
    initTeaserVideo();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
