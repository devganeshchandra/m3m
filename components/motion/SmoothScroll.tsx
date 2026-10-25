"use client";

import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "lenis";

export function SmoothScroll() {
  useEffect(() => {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    if (reduceMotion.matches) {
      const scrollToTop = () =>
        window.scrollTo({ top: 0, behavior: "instant" });
      window.addEventListener("m3m:scroll-to-top", scrollToTop);
      return () => window.removeEventListener("m3m:scroll-to-top", scrollToTop);
    }

    gsap.registerPlugin(ScrollTrigger);
    const lenis = new Lenis({ autoRaf: false, lerp: 0.08 });
    const scrollToTop = () =>
      lenis.scrollTo(0, { immediate: true, force: true });
    const updateScrollTrigger = () => ScrollTrigger.update();
    const updateLenis = (time: number) => lenis.raf(time * 1000);

    window.addEventListener("m3m:scroll-to-top", scrollToTop);
    lenis.on("scroll", updateScrollTrigger);
    gsap.ticker.add(updateLenis);
    gsap.ticker.lagSmoothing(0);

    return () => {
      window.removeEventListener("m3m:scroll-to-top", scrollToTop);
      lenis.off("scroll", updateScrollTrigger);
      gsap.ticker.remove(updateLenis);
      lenis.destroy();
      ScrollTrigger.getAll().forEach((trigger) => trigger.kill());
    };
  }, []);

  return null;
}
