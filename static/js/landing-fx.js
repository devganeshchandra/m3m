/*
 * Interaction effects for project landing pages, coloured by each page's CSS (landing-fx.css):
 *   headings — words rise in when scrolled into view and ripple in a wave on hover
 *   cards    — tilt towards the pointer with a soft light that follows it
 *   buttons  — a gentle magnetic pull, a glow under the pointer and a ripple on click
 *   tabs     — a highlight that glides to the tab under the pointer or the selected one
 * Nothing runs for visitors who prefer reduced motion; hover effects need a fine pointer.
 */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(pointer: fine)").matches;

  var HEADINGS = ".jl-display, .jl-band__title, .cl-display, .tt-title, .tt-steps__title";
  var CARDS = [
    ".jl-amenity", ".jl-gallery__item", ".jl-plan__card", ".jl-pl-card", ".jl-pillars li",
    ".cl-config", ".cl-strip__card", ".cl-times li", ".cl-pillars li", ".cl-avenue__collage figure",
    ".tt-showcase", ".tt-room", ".tt-mosaic__tile",
  ].join(", ");
  var FLAT_CARDS = ".tt-faq__item, .cl-room, .jl-time";
  var BUTTONS = ".jl-button, .cl-button, .tt-btn, .lnav__cta, .pf-submit, .jl-form__submit, .cl-form__submit, .tt-form__submit";
  var TABS = [
    { list: ".lnav__links", item: "a", current: ".is-current" },
    { list: ".cl-tour__tabs", item: "button", current: "[aria-selected='true']" },
    { list: ".cl-filters", item: "button", current: "[aria-pressed='true']" },
    { list: ".tt-hero__dots", item: "button", current: "[aria-pressed='true']" },
  ];

  function $all(selector, scope) {
    return Array.prototype.slice.call((scope || document).querySelectorAll(selector));
  }

  /* ---------- Headings ---------- */

  // Wraps each word in a span, keeping inline elements such as <em> and the spaces between words.
  function splitWords(heading) {
    var index = 0;
    function wrapText(textNode) {
      var parts = textNode.textContent.split(/(\s+)/);
      var fragment = document.createDocumentFragment();
      parts.forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) {
          fragment.appendChild(document.createTextNode(part));
          return;
        }
        var word = document.createElement("span");
        word.className = "fx-w";
        word.style.setProperty("--i", index++);
        word.textContent = part;
        fragment.appendChild(word);
      });
      textNode.parentNode.replaceChild(fragment, textNode);
    }
    Array.prototype.slice.call(heading.childNodes).forEach(function (node) {
      if (node.nodeType === 3) {
        wrapText(node);
      } else if (node.nodeType === 1 && node.children.length === 0) {
        Array.prototype.slice.call(node.childNodes).forEach(wrapText);
      }
    });
  }

  function initHeadings() {
    var headings = $all(HEADINGS);
    headings.forEach(function (heading) {
      splitWords(heading);
      heading.classList.add("fx-heading");
    });
    if (!("IntersectionObserver" in window)) {
      headings.forEach(function (heading) { heading.classList.add("is-in"); });
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -10% 0px" });
    headings.forEach(function (heading) {
      observer.observe(heading);
      // Replay the wave on each new hover.
      heading.addEventListener("mouseenter", function () {
        heading.classList.remove("is-waving");
        void heading.offsetWidth;
        heading.classList.add("is-waving");
      });
    });
  }

  /* ---------- Cards ---------- */

  function trackPointer(element, event) {
    var box = element.getBoundingClientRect();
    var x = (event.clientX - box.left) / box.width;
    var y = (event.clientY - box.top) / box.height;
    element.style.setProperty("--mx", (x * 100).toFixed(1) + "%");
    element.style.setProperty("--my", (y * 100).toFixed(1) + "%");
    return { x: x - 0.5, y: y - 0.5 };
  }

  function initCards() {
    $all(CARDS + ", " + FLAT_CARDS).forEach(function (card) {
      var glow = document.createElement("span");
      glow.className = "fx-glow";
      glow.setAttribute("aria-hidden", "true");
      card.appendChild(glow);
      card.classList.add("fx-card");
      var tilt = !card.matches(FLAT_CARDS);
      card.addEventListener("pointermove", function (event) {
        var point = trackPointer(card, event);
        if (tilt) {
          card.style.transform = "perspective(900px) rotateX(" + (-point.y * 7).toFixed(2) + "deg) rotateY(" +
            (point.x * 7).toFixed(2) + "deg) translateY(-6px)";
        }
      });
      card.addEventListener("pointerleave", function () {
        card.style.transform = "";
      });
    });
  }

  /* ---------- Buttons ---------- */

  function initButtons() {
    $all(BUTTONS).forEach(function (button) {
      // Buttons with the site's own animation (site.js initFancyButton) keep it alone.
      if (button.hasAttribute("data-fancy-button")) return;
      button.classList.add("fx-btn");
      var glow = document.createElement("span");
      glow.className = "fx-btn__glow";
      glow.setAttribute("aria-hidden", "true");
      button.appendChild(glow);
      button.addEventListener("pointermove", function (event) {
        var point = trackPointer(button, event);
        button.style.transform = "translate(" + (point.x * 8).toFixed(1) + "px, " + (point.y * 6 - 2).toFixed(1) + "px)";
      });
      button.addEventListener("pointerleave", function () {
        button.style.transform = "";
      });
      button.addEventListener("click", function (event) {
        var box = button.getBoundingClientRect();
        var ripple = document.createElement("span");
        ripple.className = "fx-ripple";
        ripple.setAttribute("aria-hidden", "true");
        var size = Math.max(box.width, box.height) * 2;
        ripple.style.width = ripple.style.height = size + "px";
        ripple.style.left = (event.clientX ? event.clientX - box.left : box.width / 2) - size / 2 + "px";
        ripple.style.top = (event.clientY ? event.clientY - box.top : box.height / 2) - size / 2 + "px";
        button.appendChild(ripple);
        setTimeout(function () {
          ripple.remove();
        }, 700);
      });
    });
  }

  /* ---------- Tabs ---------- */

  function initTabs() {
    TABS.forEach(function (config) {
      $all(config.list).forEach(function (list) {
        var items = $all(config.item, list);
        if (!items.length) return;
        list.classList.add("fx-tabs");
        var pill = document.createElement("span");
        pill.className = "fx-pill";
        pill.setAttribute("aria-hidden", "true");
        list.insertBefore(pill, list.firstChild);

        function moveTo(item) {
          if (!item || item.offsetParent === null) {
            pill.style.opacity = "0";
            return;
          }
          // Measured from the list itself, so items nested in other elements line up too.
          var box = item.getBoundingClientRect();
          var area = list.getBoundingClientRect();
          var x = box.left - area.left - list.clientLeft + list.scrollLeft;
          var y = box.top - area.top - list.clientTop + list.scrollTop;
          pill.style.opacity = "1";
          pill.style.width = box.width + "px";
          pill.style.height = box.height + "px";
          pill.style.transform = "translate(" + x + "px, " + y + "px)";
        }

        function settle() {
          moveTo($all(config.current, list).filter(function (item) { return items.indexOf(item) !== -1; })[0]);
        }

        items.forEach(function (item) {
          item.addEventListener("mouseenter", function () { moveTo(item); });
          item.addEventListener("focus", function () { moveTo(item); });
        });
        list.addEventListener("mouseleave", settle);
        // Follow selection changes made by clicks, keyboard or scrolling.
        new MutationObserver(settle).observe(list, { subtree: true, attributes: true, attributeFilter: ["class", "aria-selected", "aria-pressed"] });
        window.addEventListener("resize", settle);
        settle();
      });
    });
  }

  function init() {
    if (reduceMotion) return;
    document.documentElement.classList.add("fx-ready");
    initHeadings();
    initTabs();
    if (!finePointer) return;
    initCards();
    initButtons();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
