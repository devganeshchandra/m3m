/*
 * Billionaire Block landing page: preloader, smooth scroll, reveals, pinned club gallery,
 * residence tabs, floor plan / brochure / gallery dialogs, and the enquiry forms.
 * Uses the GSAP, ScrollTrigger and Lenis copies in static/vendor. Every effect is skipped
 * when the visitor prefers reduced motion, and the page works without JavaScript.
 */
(function () {
  "use strict";

  var root = document.documentElement;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var motion = !reduceMotion && Boolean(window.gsap && window.ScrollTrigger);
  var lenis = null;
  var EASE = "expo.out";

  function $(selector, scope) {
    return (scope || document).querySelector(selector);
  }

  function $all(selector, scope) {
    return Array.prototype.slice.call((scope || document).querySelectorAll(selector));
  }

  if (motion) {
    root.classList.add("bb-motion");
    gsap.registerPlugin(ScrollTrigger);
  }

  /* ---------- Smooth scroll and in-page links ---------- */

  function initSmoothScroll() {
    if (!motion || !window.Lenis) return;
    lenis = new Lenis({ autoRaf: false, lerp: 0.075 });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(function (time) {
      lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);
  }

  function scrollToTarget(target) {
    var offset = -($("[data-bb-nav]").offsetHeight || 0);
    if (lenis) lenis.scrollTo(target, { offset: offset, duration: 1.6 });
    else window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY + offset, behavior: reduceMotion ? "auto" : "smooth" });
  }

  function initAnchors() {
    document.addEventListener("click", function (event) {
      var link = event.target.closest('a[href^="#"]');
      if (!link) return;
      var id = link.getAttribute("href").slice(1);
      var target = id ? document.getElementById(id) : null;
      if (!target) return;
      event.preventDefault();
      closeMenu();
      scrollToTarget(target);
    });
  }

  function pauseScroll(paused) {
    if (!lenis) return;
    if (paused) lenis.stop();
    else lenis.start();
  }

  /* ---------- Navigation ---------- */

  var nav = $("[data-bb-nav]");
  var menu = $("[data-bb-menu]");
  var toggle = $("[data-bb-menu-toggle]");

  function onScroll() {
    nav.classList.toggle("is-scrolled", window.scrollY > 40);
  }

  function closeMenu() {
    if (!menu || menu.hidden) return;
    menu.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
    nav.classList.remove("is-menu-open");
    pauseScroll(false);
  }

  function initNav() {
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    toggle.addEventListener("click", function () {
      var open = menu.hidden;
      menu.hidden = !open;
      toggle.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-menu-open", open);
      pauseScroll(open);
      if (open && motion) {
        gsap.from($all("a", menu), { y: 30, opacity: 0, stagger: 0.06, duration: 1, ease: EASE });
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeMenu();
    });
  }

  /* ---------- Preloader and hero ---------- */

  // Wraps each word in a mask for the rise-in effect. Words inside an inline element such as
  // <em> keep it, so a heading's gold italic phrase survives the split.
  function splitWords(element) {
    if (element.dataset.split) return $all(".bb-word > span", element);
    element.dataset.split = "true";
    // Each piece remembers whether a space came before it, so "layouts?" stays together.
    var pieces = [];
    var pendingSpace = false;
    Array.prototype.slice.call(element.childNodes).forEach(function (node) {
      var tag = node.nodeType === 1 ? node.tagName : null;
      var text = node.textContent;
      var pattern = /(\s*)(\S+)/g;
      var match;
      while ((match = pattern.exec(text))) {
        pieces.push({
          word: match[2],
          tag: tag,
          className: tag ? node.className : "",
          space: pieces.length > 0 && (pendingSpace || match[1].length > 0),
        });
        pendingSpace = false;
      }
      if (/\s$/.test(text)) pendingSpace = true;
    });
    element.setAttribute("aria-label", element.textContent.trim().replace(/\s+/g, " "));
    element.innerHTML = "";
    pieces.forEach(function (piece) {
      var outer = document.createElement("span");
      var inner = document.createElement("span");
      outer.className = "bb-word";
      outer.setAttribute("aria-hidden", "true");
      if (piece.tag) {
        var wrap = document.createElement(piece.tag);
        if (piece.className) wrap.className = piece.className;
        wrap.textContent = piece.word;
        inner.appendChild(wrap);
      } else {
        inner.textContent = piece.word;
      }
      outer.appendChild(inner);
      if (piece.space) element.appendChild(document.createTextNode(" "));
      element.appendChild(outer);
    });
    return $all(".bb-word > span", element);
  }

  function heroIntro() {
    if (!motion) return;
    var title = $("[data-bb-hero-title]");
    var words = splitWords(title);
    gsap.from(words, { yPercent: 110, duration: 1.8, stagger: 0.12, ease: EASE });
    gsap.from($all("[data-bb-hero-item]"), { y: 24, opacity: 0, duration: 1.6, stagger: 0.25, delay: 0.5, ease: EASE });
    gsap.from(".bb-hero__media", { scale: 1.12, duration: 3, ease: "power3.out" });
    // The hero media drifts slower than the page.
    gsap.to(".bb-hero__media", {
      yPercent: 18,
      ease: "none",
      scrollTrigger: { trigger: ".bb-hero", start: "top top", end: "bottom top", scrub: true },
    });
  }

  function initPreloader() {
    var preloader = $("[data-bb-preloader]");
    if (!preloader) return;
    if (!motion) {
      preloader.classList.add("is-done");
      return;
    }
    pauseScroll(true);
    var timeline = gsap.timeline({
      onComplete: function () {
        preloader.classList.add("is-done");
        pauseScroll(false);
        ScrollTrigger.refresh();
      },
    });
    timeline
      .to(".bb-preloader__frame", { strokeDashoffset: 0, duration: 1.4, ease: "power3.inOut" })
      .to(".bb-preloader__letters", { opacity: 1, duration: 0.8, ease: "power2.out" }, "-=0.6")
      .to(".bb-preloader__line", { scaleX: 1, duration: 0.9, ease: "power3.inOut" }, "-=0.5")
      .add(heroIntro, "+=0.1")
      .to(preloader, { yPercent: -100, duration: 1.2, ease: "power4.inOut" }, "<");
  }

  /* ---------- Scroll reveals ---------- */

  function initReveals() {
    if (!motion) return;

    $all("[data-bb-words], [data-bb-lines]").forEach(function (element) {
      var words = splitWords(element);
      var scrubbed = element.hasAttribute("data-bb-words");
      gsap.from(words, {
        yPercent: 110,
        opacity: scrubbed ? 0.2 : 1,
        duration: 1.4,
        stagger: scrubbed ? 0.08 : 0.04,
        ease: EASE,
        scrollTrigger: scrubbed
          ? { trigger: element, start: "top 85%", end: "bottom 55%", scrub: 1 }
          : { trigger: element, start: "top 88%" },
      });
    });

    ScrollTrigger.batch("[data-bb-fade]", {
      start: "top 90%",
      once: true,
      onEnter: function (batch) {
        // clearProps hands transform back to the CSS, so hover effects still work afterwards.
        gsap.to(batch, { opacity: 1, y: 0, duration: 1.4, stagger: 0.1, ease: EASE, clearProps: "transform" });
      },
    });

    $all("[data-bb-clip]").forEach(function (element) {
      gsap.to(element, {
        clipPath: "inset(0% 0 0 0)",
        duration: 1.8,
        ease: "power4.inOut",
        scrollTrigger: { trigger: element, start: "top 85%" },
      });
    });

    $all("[data-bb-parallax]").forEach(function (layer) {
      gsap.fromTo(layer, { yPercent: -8 }, {
        yPercent: 8,
        ease: "none",
        scrollTrigger: { trigger: layer.parentElement, start: "top bottom", end: "bottom top", scrub: true },
      });
    });
  }

  /* ---------- The research story: motion for every section ---------- */

  function initStoryMotion() {
    if (!motion) return;

    // Eyebrows: the gold rule draws in, then the label slides after it.
    $all(".bbx-eyebrow").forEach(function (eyebrow) {
      gsap.from(eyebrow, {
        x: -24,
        opacity: 0,
        duration: 1.1,
        ease: EASE,
        scrollTrigger: { trigger: eyebrow, start: "top 92%", onEnter: function () { eyebrow.classList.add("is-drawn"); } },
      });
    });

    // Paragraphs, notes and buttons rise in.
    ScrollTrigger.batch(".bbx-lead, .bbx-footnote, .bbx-mini, .bbx-callout, .bbx-section .bb-button, .bbx-brand .bb-button", {
      start: "top 92%",
      once: true,
      onEnter: function (batch) {
        gsap.from(batch, { y: 30, opacity: 0, duration: 1.1, stagger: 0.08, ease: EASE, clearProps: "transform,opacity" });
      },
    });

    // Lists, rows, chips and cards: staggered, each group as it scrolls into view.
    [
      ".bbx-facts > div", ".bbx-chips li", ".bbx-spec > div", ".bbx-community__card",
      ".bbx-ticks li", ".bbx-amenity", ".bbx-pending li", ".bbx-strategy__item",
      ".bbx-checks__figures > div", ".bbx-sources__grid li",
    ].forEach(function (selector) {
      ScrollTrigger.batch(selector, {
        start: "top 92%",
        once: true,
        onEnter: function (batch) {
          gsap.from(batch, {
            y: 40,
            opacity: 0,
            scale: 0.97,
            duration: 1.1,
            stagger: 0.09,
            ease: EASE,
            clearProps: "transform,opacity",
          });
        },
      });
    });

    // Location and route rows slide in from the side.
    ScrollTrigger.batch(".bbx-routes li, .bbx-checks__list li", {
      start: "top 92%",
      once: true,
      onEnter: function (batch) {
        gsap.from(batch, { x: 40, opacity: 0, duration: 1, stagger: 0.07, ease: EASE, clearProps: "transform,opacity" });
      },
    });

    // Images: a slow zoom-out while they cross the screen, so every photo feels alive.
    $all(".bbx-brand img, .bbx-community__card img, .bbx-towers img, .bbx-strategy__item img, .bbx-location img, .bbx-checks img, .bbx-amenity img").forEach(function (image) {
      gsap.fromTo(image, { scale: 1.18 }, {
        scale: 1,
        ease: "none",
        scrollTrigger: { trigger: image.parentElement, start: "top bottom", end: "bottom top", scrub: true },
      });
    });

    // The inset photo floats against the main one.
    var inset = $(".bbx-brand__inset");
    if (inset) {
      gsap.fromTo(inset, { yPercent: 18 }, {
        yPercent: -12,
        ease: "none",
        scrollTrigger: { trigger: ".bbx-brand", start: "top bottom", end: "bottom top", scrub: true },
      });
    }

    // The community letters and strategy numbers pop in.
    ScrollTrigger.batch(".bbx-community__letter, .bbx-strategy__number", {
      start: "top 90%",
      once: true,
      onEnter: function (batch) {
        gsap.from(batch, { scale: 0, rotate: -20, duration: 0.9, stagger: 0.12, ease: "back.out(2)", clearProps: "transform" });
      },
    });

    // Cards tilt gently towards the pointer on desktop.
    if (window.matchMedia("(pointer: fine)").matches) {
      $all(".bbx-amenity, .bbx-strategy__item, .bbx-community__card, .bbx-sources__grid a").forEach(function (card) {
        card.addEventListener("pointermove", function (event) {
          var box = card.getBoundingClientRect();
          var x = (event.clientX - box.left) / box.width - 0.5;
          var y = (event.clientY - box.top) / box.height - 0.5;
          gsap.to(card, { rotateY: x * 6, rotateX: -y * 6, transformPerspective: 900, duration: 0.6, ease: "power2.out" });
        });
        card.addEventListener("pointerleave", function () {
          gsap.to(card, { rotateY: 0, rotateX: 0, duration: 0.8, ease: "power3.out" });
        });
      });
    }
  }

  /* ---------- Count-up figures ---------- */

  function initCountUp() {
    $all("[data-count]").forEach(function (element) {
      var raw = element.dataset.count;
      var match = raw.match(/[\d,]+/);
      if (!match || !motion) return;
      var target = Number(match[0].replace(/,/g, ""));
      var before = raw.slice(0, match.index);
      var after = raw.slice(match.index + match[0].length);
      var isYear = target >= 1900 && target <= 2100 && match[0].indexOf(",") === -1;
      var grouping = match[0].indexOf(",") !== -1;
      var format = function (value) {
        var number = Math.round(value);
        return before + (grouping ? number.toLocaleString("en-IN") : String(number)) + after;
      };
      var state = { value: isYear ? target - 20 : 0 };
      element.textContent = format(state.value);
      gsap.to(state, {
        value: target,
        duration: 2.4,
        ease: "power3.out",
        scrollTrigger: { trigger: element, start: "top 90%", once: true },
        onUpdate: function () {
          element.textContent = format(state.value);
        },
        onComplete: function () {
          element.textContent = raw;
        },
      });
    });
  }

  /* ---------- The club: pinned horizontal scroll on large screens ---------- */

  function initClub() {
    var section = $("[data-bb-club]");
    if (!section || !motion) return;
    // The heading and the cards move together as one row, so the heading leaves first.
    var row = $(".bb-club__inner", section);
    var media = gsap.matchMedia();
    media.add("(min-width: 901px)", function () {
      var distance = function () {
        return Math.max(0, row.scrollWidth - window.innerWidth);
      };
      gsap.to(row, {
        x: function () {
          return -distance();
        },
        ease: "none",
        scrollTrigger: {
          trigger: section,
          start: "top top",
          end: function () {
            return "+=" + distance();
          },
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true,
          anticipatePin: 1,
        },
      });
    });
  }

  /* ---------- Residence tabs ---------- */

  function initTabs() {
    var list = $("[data-bb-tabs]");
    if (!list) return;
    var tabs = $all('[role="tab"]', list);

    function select(tab, focus) {
      tabs.forEach(function (item) {
        var on = item === tab;
        item.setAttribute("aria-selected", String(on));
        item.tabIndex = on ? 0 : -1;
        document.getElementById(item.getAttribute("aria-controls")).hidden = !on;
      });
      if (focus) tab.focus();
      if (motion) ScrollTrigger.refresh();
    }

    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () {
        select(tab, false);
      });
      tab.addEventListener("keydown", function (event) {
        var step = event.key === "ArrowRight" ? 1 : event.key === "ArrowLeft" ? -1 : 0;
        if (!step) return;
        event.preventDefault();
        select(tabs[(index + step + tabs.length) % tabs.length], true);
      });
    });
  }

  /* ---------- Dialogs: floor plan, brochure, gallery lightbox ---------- */

  function dialog(name) {
    return $('[data-bb-modal="' + name + '"]');
  }

  function openDialog(element) {
    if (!element.open) element.showModal();
    pauseScroll(true);
  }

  function initDialogs() {
    $all("dialog").forEach(function (element) {
      element.addEventListener("close", function () {
        pauseScroll(false);
      });
      element.addEventListener("click", function (event) {
        if (event.target === element) element.close();
      });
      $all("[data-bb-close]", element).forEach(function (button) {
        button.addEventListener("click", function () {
          element.close();
        });
      });
    });

    var plan = dialog("plan");
    document.addEventListener("click", function (event) {
      var trigger = event.target.closest("[data-bb-open]");
      if (!trigger) return;
      if (trigger.dataset.bbOpen === "brochure") {
        closeMenu();
        openDialog(dialog("brochure"));
        return;
      }
      var data = trigger.dataset;
      $("[data-plan-name]", plan).textContent = data.name;
      $("[data-plan-size]", plan).textContent = data.size;
      $("[data-plan-configuration]", plan).textContent = data.configuration;
      var image = $("[data-plan-image]", plan);
      image.hidden = !data.plan;
      $("[data-plan-placeholder]", plan).hidden = Boolean(data.plan);
      if (data.plan) {
        image.src = data.plan;
        image.alt = "Floor plan of " + data.name;
      }
      var features = $("[data-plan-features]", plan);
      features.innerHTML = "";
      data.features.split("\n").filter(Boolean).forEach(function (text) {
        var item = document.createElement("li");
        item.textContent = text;
        features.appendChild(item);
      });
      $("[data-plan-request]", plan).dataset.residence = data.name;
      openDialog(plan);
    });

    // “Request this floor plan” pre-selects the residence in the viewing form.
    $("[data-plan-request]", plan).addEventListener("click", function () {
      var select = $("[data-residence-select]");
      if (select) select.value = this.dataset.residence || "";
      plan.close();
    });

    initLightbox();
    initNews();
  }

  // News cards open their full story in one dialog, with previous/next.
  function initNews() {
    var box = dialog("news");
    var cards = $all("[data-bb-news]");
    if (!box || !cards.length) return;
    var body = $("[data-bb-news-body]", box);
    var current = 0;

    function show(index) {
      current = (index + cards.length) % cards.length;
      var template = $('[data-bb-news-template="' + current + '"]');
      body.innerHTML = "";
      body.appendChild(template.content.cloneNode(true));
      box.scrollTop = 0;
      if (motion) gsap.from(body.children, { y: 16, opacity: 0, stagger: 0.06, duration: 0.9, ease: EASE });
    }

    cards.forEach(function (card, index) {
      card.addEventListener("click", function () {
        show(index);
        openDialog(box);
      });
    });
    $all("[data-bb-news-step]", box).forEach(function (button) {
      button.hidden = cards.length < 2;
      button.addEventListener("click", function () {
        show(current + Number(button.dataset.bbNewsStep));
      });
    });
    box.addEventListener("keydown", function (event) {
      if (event.target.closest("a, button")) return;
      if (event.key === "ArrowRight") show(current + 1);
      if (event.key === "ArrowLeft") show(current - 1);
    });
  }

  function initLightbox() {
    var box = dialog("lightbox");
    var items = $all("[data-bb-lightbox]");
    if (!box || !items.length) return;
    var image = $("[data-lightbox-image]", box);
    var caption = $("[data-lightbox-caption]", box);
    var current = 0;

    function show(index) {
      current = (index + items.length) % items.length;
      var item = items[current];
      image.src = item.dataset.full;
      image.alt = $("img", item).alt;
      caption.textContent = item.dataset.caption + " · Artistic impression";
      if (motion) gsap.fromTo(image, { opacity: 0, scale: 1.02 }, { opacity: 1, scale: 1, duration: 0.9, ease: EASE });
    }

    items.forEach(function (item, index) {
      item.addEventListener("click", function () {
        show(index);
        openDialog(box);
      });
    });
    $all("[data-lightbox-step]", box).forEach(function (button) {
      button.addEventListener("click", function () {
        show(current + Number(button.dataset.lightboxStep));
      });
    });
    box.addEventListener("keydown", function (event) {
      if (event.key === "ArrowRight") show(current + 1);
      if (event.key === "ArrowLeft") show(current - 1);
    });

    var startX = null;
    box.addEventListener("touchstart", function (event) {
      startX = event.touches[0].clientX;
    }, { passive: true });
    box.addEventListener("touchend", function (event) {
      if (startX === null) return;
      var delta = event.changedTouches[0].clientX - startX;
      if (Math.abs(delta) > 50) show(current + (delta < 0 ? 1 : -1));
      startX = null;
    });
  }

  /* ---------- Cursor and magnetic buttons ---------- */

  function initCursor() {
    var cursor = $("[data-bb-cursor]");
    if (!cursor || !motion || !window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;
    var moveX = gsap.quickTo(cursor, "x", { duration: 0.5, ease: "power3.out" });
    var moveY = gsap.quickTo(cursor, "y", { duration: 0.5, ease: "power3.out" });
    window.addEventListener("pointermove", function (event) {
      cursor.classList.add("is-active");
      moveX(event.clientX);
      moveY(event.clientY);
    });
    document.addEventListener("pointerover", function (event) {
      cursor.classList.toggle("is-hover", Boolean(event.target.closest("a, button, summary, img, [data-bb-lightbox]")));
    });
    document.addEventListener("pointerleave", function () {
      cursor.classList.remove("is-active");
    });

    $all("[data-magnetic]").forEach(function (button) {
      var toX = gsap.quickTo(button, "x", { duration: 0.8, ease: "elastic.out(1, 0.4)" });
      var toY = gsap.quickTo(button, "y", { duration: 0.8, ease: "elastic.out(1, 0.4)" });
      button.addEventListener("pointermove", function (event) {
        var box = button.getBoundingClientRect();
        toX((event.clientX - box.left - box.width / 2) * 0.25);
        toY((event.clientY - box.top - box.height / 2) * 0.35);
      });
      button.addEventListener("pointerleave", function () {
        toX(0);
        toY(0);
      });
    });
  }

  /* ---------- Hero video ---------- */

  function initVideo() {
    var video = $("[data-bb-video]");
    if (!video) return;
    if (reduceMotion) {
      video.removeAttribute("autoplay");
      video.pause();
      return;
    }
    // Pause the video when it is off screen, to save battery and data.
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) video.play().catch(function () {});
          else video.pause();
        });
      }).observe(video);
    }
  }

  /* ---------- Forms ---------- */

  function today() {
    var now = new Date();
    now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
    return now.toISOString().slice(0, 10);
  }

  function fillTracking(form) {
    var params = new URLSearchParams(window.location.search);
    $all("[data-utm]", form).forEach(function (input) {
      input.value = params.get(input.name) || "";
    });
    var pageUrl = $("[data-page-url]", form);
    if (pageUrl) pageUrl.value = window.location.href;
  }

  function fullPhone(form) {
    var code = $("[data-country-code]", form).value;
    var local = $('[name="phone_local"]', form).value.replace(/[^\d]/g, "").replace(/^0+/, "");
    return local ? code + local : "";
  }

  function setError(control, message) {
    var id = control.getAttribute("aria-describedby");
    var slot = id ? document.getElementById(id) : null;
    control.setAttribute("aria-invalid", message ? "true" : "false");
    if (!slot) return;
    slot.textContent = message || "";
    slot.hidden = !message;
  }

  function check(control, form) {
    var v = window.M3MValidation;
    var value = control.value.trim();
    switch (control.dataset.check) {
      case "name":
        return v ? v.validateName(value) : value.length > 1 ? "" : "Please enter your name.";
      case "email":
        return v ? v.validateEmail(value) : /.+@.+\..+/.test(value) ? "" : "Please enter a valid email address.";
      case "phone":
        var phone = fullPhone(form);
        if (!phone) return "Please enter your phone number.";
        return v ? v.validatePhone(phone).replace("10-digit Indian mobile number, or include +country code for an international number", "valid phone number for the selected country") : "";
      case "date":
        return value && value < today() ? "Please choose today or a later date." : "";
      default:
        return "";
    }
  }

  function initForms() {
    $all("[data-min-today]").forEach(function (input) {
      input.min = today();
    });

    $all("[data-bb-form]").forEach(function (form) {
      var kind = form.dataset.bbForm;
      var panel = form.parentElement;
      var success = $("[data-bb-success]", panel);
      var status = $("[data-bb-status]", form);
      var button = $('button[type="submit"]', form);
      var controls = $all("[data-check]", form);

      controls.forEach(function (control) {
        control.addEventListener("blur", function () {
          if (control.value) setError(control, check(control, form));
        });
        control.addEventListener("input", function () {
          if (control.getAttribute("aria-invalid") === "true") setError(control, check(control, form));
        });
      });

      form.addEventListener("submit", function (event) {
        event.preventDefault();
        status.hidden = true;
        var firstInvalid = null;
        controls.forEach(function (control) {
          var message = check(control, form);
          setError(control, message);
          if (message && !firstInvalid) firstInvalid = control;
        });
        if (firstInvalid) {
          firstInvalid.focus();
          return;
        }

        fillTracking(form);
        $("[data-phone-full]", form).value = fullPhone(form);
        button.disabled = true;
        form.setAttribute("aria-busy", "true");

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
            if (!data.ok) {
              var errors = data.errors || {};
              Object.keys(errors).forEach(function (field) {
                var control = field === "phone" ? $('[name="phone_local"]', form) : $('[name="' + field + '"]', form);
                if (control) setError(control, errors[field]);
              });
              status.textContent = data.message || (Object.keys(errors).length
                ? "Please check the highlighted details."
                : "We couldn’t send your request. Please call or WhatsApp us.");
              status.hidden = false;
              return;
            }
            if (kind === "brochure") brochureReady(form);
            form.reset();
            form.hidden = true;
            success.hidden = false;
            success.focus();
            if (motion) gsap.from(success.children, { y: 20, opacity: 0, stagger: 0.12, duration: 1.2, ease: EASE });
          })
          .catch(function () {
            status.textContent = "We couldn’t reach our server. Please check your connection, or call or WhatsApp us.";
            status.hidden = false;
          })
          .finally(function () {
            button.disabled = false;
            form.removeAttribute("aria-busy");
          });
      });

      var again = $("[data-bb-reset]", panel);
      if (again) {
        again.addEventListener("click", function () {
          success.hidden = true;
          form.hidden = false;
          $("input:not([type=hidden])", form).focus();
        });
      }
    });
  }

  function brochureReady(form) {
    var url = form.dataset.brochure;
    var message = $("[data-brochure-message]", form.parentElement);
    if (url) {
      message.textContent = "Your download has started. A copy will also reach you on WhatsApp.";
      var link = document.createElement("a");
      link.href = url;
      link.download = "";
      document.body.appendChild(link);
      link.click();
      link.remove();
    } else {
      message.textContent = "Our team will send the brochure to you on WhatsApp shortly.";
    }
  }

  /* ---------- The plan: image carousel ---------- */

  // Cross-fades every few seconds; arrows, dots and swipe step through it. Autoplay pauses on
  // hover and keyboard focus, and never starts for visitors who prefer reduced motion.
  function initStoryCarousel() {
    var carousel = $("[data-bbx-carousel]");
    if (!carousel) return;
    var slides = $all(".bbx-carousel__slide", carousel);
    var dots = $all("[data-bbx-dot]", carousel);
    var current = 0;
    var timer = null;

    function show(index) {
      current = (index + slides.length) % slides.length;
      slides.forEach(function (slide, i) {
        slide.classList.toggle("is-active", i === current);
        slide.setAttribute("aria-hidden", i === current ? "false" : "true");
      });
      dots.forEach(function (dot, i) {
        dot.setAttribute("aria-pressed", i === current ? "true" : "false");
      });
    }

    function stop() {
      clearInterval(timer);
      timer = null;
    }

    function start() {
      if (reduceMotion || timer) return;
      timer = setInterval(function () {
        show(current + 1);
      }, 5500);
    }

    $all("[data-bbx-step]", carousel).forEach(function (button) {
      button.addEventListener("click", function () {
        show(current + Number(button.dataset.bbxStep));
      });
    });
    dots.forEach(function (dot) {
      dot.addEventListener("click", function () {
        show(Number(dot.dataset.bbxDot));
      });
    });

    var touchX = null;
    carousel.addEventListener("touchstart", function (event) {
      touchX = event.touches[0].clientX;
    }, { passive: true });
    carousel.addEventListener("touchend", function (event) {
      if (touchX === null) return;
      var distance = event.changedTouches[0].clientX - touchX;
      if (Math.abs(distance) > 40) show(current + (distance < 0 ? 1 : -1));
      touchX = null;
    });

    carousel.addEventListener("mouseenter", stop);
    carousel.addEventListener("mouseleave", start);
    carousel.addEventListener("focusin", stop);
    carousel.addEventListener("focusout", start);
    start();
  }

  /* ---------- Start ---------- */

  function init() {
    initSmoothScroll();
    initNav();
    initAnchors();
    initVideo();
    initTabs();
    initDialogs();
    initForms();
    initCursor();
    initReveals();
    initCountUp();
    initStoryMotion();
    initClub();
    initStoryCarousel();
    initPreloader();
    if (!motion) return;
    window.addEventListener("load", function () {
      ScrollTrigger.refresh();
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
