/*
 * Location sections on project landing pages (Jacob & Co., The Cullinan): drive times that count up
 * and fill their rings when scrolled into view, and places that show their route on a Google map.
 *
 *   [data-lm-stage data-origin]  the section; data-origin is where routes start (as typed in Google Maps)
 *   [data-lm-map]                the map iframe; its src is the starting map
 *   [data-lm-place]              a place button; the value is the destination (empty: a close map of the area)
 *   [data-lm-route]              the line naming the route on show; the button's data-label fills it
 *   [data-lm-mode]               optional: switches the stage's "is-day" class (the page styles the map)
 *   [data-lm-view]               optional: tabs that switch the stage's data-view (e.g. live map / plan)
 *   [data-lm-list]               the list of places; gets "is-in" when seen, and [data-lm-count] numbers count up
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

  function mapUrl(params) {
    return "https://www.google.com/maps?" + params + "&output=embed";
  }

  function initStage(stage) {
    var map = $("[data-lm-map]", stage);
    var route = $("[data-lm-route]", stage);
    var places = $all("[data-lm-place]", stage);
    var origin = stage.dataset.origin;
    var home = map.getAttribute("src");

    function setView(view) {
      stage.dataset.view = view;
      $all("[data-lm-view]", stage).forEach(function (tab) {
        tab.setAttribute("aria-pressed", tab.dataset.lmView === view ? "true" : "false");
      });
    }

    places.forEach(function (place) {
      place.addEventListener("click", function () {
        var on = place.getAttribute("aria-pressed") !== "true";
        places.forEach(function (other) {
          other.setAttribute("aria-pressed", "false");
        });
        place.setAttribute("aria-pressed", on ? "true" : "false");
        stage.classList.add("is-loading");
        var destination = place.dataset.lmPlace;
        var routeUrl = destination
          ? mapUrl("saddr=" + encodeURIComponent(origin) + "&daddr=" + encodeURIComponent(destination))
          : mapUrl("q=" + encodeURIComponent(origin) + "&z=15");
        map.src = on ? routeUrl : home;
        if (route) route.textContent = on ? origin.split(",")[0] + "  →  " + place.dataset.label : origin;
        if (stage.dataset.view && stage.dataset.view !== "live") setView("live");
      });
    });
    map.addEventListener("load", function () {
      stage.classList.remove("is-loading");
    });

    var mode = $("[data-lm-mode]", stage);
    if (mode) {
      mode.addEventListener("click", function () {
        var day = mode.getAttribute("aria-pressed") !== "true";
        mode.setAttribute("aria-pressed", day ? "true" : "false");
        stage.classList.toggle("is-day", day);
      });
    }

    $all("[data-lm-view]", stage).forEach(function (tab) {
      tab.addEventListener("click", function () {
        setView(tab.dataset.lmView);
      });
    });

    // The minutes count up and the rings fill once the list comes into view.
    var list = $("[data-lm-list]", stage);
    if (!list) return;
    if (reduceMotion || !("IntersectionObserver" in window)) {
      list.classList.add("is-in");
      return;
    }
    var counters = $all("[data-lm-count]", list);
    counters.forEach(function (counter) {
      counter.textContent = "0";
    });
    new IntersectionObserver(function (entries, observer) {
      if (!entries[0].isIntersecting) return;
      observer.disconnect();
      list.classList.add("is-in");
      var start = performance.now();
      (function tick(now) {
        var progress = Math.min(1, (now - start) / 1400);
        var eased = 1 - Math.pow(1 - progress, 3);
        counters.forEach(function (counter) {
          var target = parseFloat(counter.dataset.lmCount) || 0;
          counter.textContent = progress < 1 ? String(Math.round(target * eased)) : counter.dataset.lmCount;
        });
        if (progress < 1) requestAnimationFrame(tick);
      })(start);
    }, { threshold: 0.35 }).observe(list);
  }

  function init() {
    $all("[data-lm-stage]").forEach(initStage);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
