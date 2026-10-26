/*
 * Header for project ad landing pages: the phone menu, a shadow once the page scrolls, and the
 * section link for the part of the page in view.
 */
(function () {
  "use strict";

  function init() {
    var nav = document.querySelector("[data-lnav]");
    if (!nav) return;
    var toggle = nav.querySelector("[data-lnav-toggle]");
    var links = Array.prototype.slice.call(nav.querySelectorAll(".lnav__links a"));

    function setOpen(open) {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    }

    toggle.addEventListener("click", function () {
      setOpen(!nav.classList.contains("is-open"));
    });
    links.forEach(function (link) {
      link.addEventListener("click", function () {
        setOpen(false);
      });
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setOpen(false);
    });

    window.addEventListener("scroll", function () {
      nav.classList.toggle("is-scrolled", window.scrollY > 10);
    }, { passive: true });

    if (!("IntersectionObserver" in window)) return;
    var byId = {};
    links.forEach(function (link) {
      var id = link.getAttribute("href").slice(1);
      var section = document.getElementById(id);
      if (section) byId[id] = link;
    });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (link) {
          link.classList.toggle("is-current", link === byId[entry.target.id]);
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(byId).forEach(function (id) {
      observer.observe(document.getElementById(id));
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
