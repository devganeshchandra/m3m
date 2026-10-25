"use client";

import { useEffect, useState } from "react";

const bannerCount = 1;
const rotationInterval = 6500;

export function HeroBannerCarousel() {
  const [activeBanner, setActiveBanner] = useState(0);
  const [paused, setPaused] = useState(false);

  useEffect(() => {
    if (
      bannerCount < 2 ||
      paused ||
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    ) {
      return;
    }

    const interval = window.setInterval(() => {
      setActiveBanner((current) => (current + 1) % bannerCount);
    }, rotationInterval);

    return () => window.clearInterval(interval);
  }, [paused]);

  return (
    <div
      aria-label="M3M residences banners"
      aria-roledescription="carousel"
      className="hero-banner"
      role="region"
    >
      <div className="hero-banner__slides" aria-hidden="true">
        {Array.from({ length: bannerCount }, (_, index) => (
          <div
            className={`hero-banner__slide${activeBanner === index ? " is-active" : ""}`}
            key={index}
          />
        ))}
      </div>
      {bannerCount > 1 && (
        <div
          className="hero-banner__controls"
          role="group"
          aria-label="Banner controls"
        >
          <button
            aria-label={paused ? "Play banners" : "Pause banners"}
            className="hero-banner__toggle"
            onClick={() => setPaused((current) => !current)}
            type="button"
          >
            {paused ? "Play" : "Pause"}
          </button>
          <div
            className="hero-banner__pagination"
            role="group"
            aria-label="Choose a banner"
          >
            {Array.from({ length: bannerCount }, (_, index) => (
              <button
                aria-label={`Show banner ${index + 1} of ${bannerCount}`}
                aria-pressed={activeBanner === index}
                className="hero-banner__pagination-button"
                key={index}
                onClick={() => setActiveBanner(index)}
                type="button"
              >
                <span />
              </button>
            ))}
          </div>
          <span
            className="hero-banner__status"
            aria-live={paused ? "polite" : "off"}
          >
            Banner {activeBanner + 1} of {bannerCount}
          </span>
        </div>
      )}
    </div>
  );
}
