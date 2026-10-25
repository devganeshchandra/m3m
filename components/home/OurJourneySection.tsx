"use client";

import { useState } from "react";

const principles = [
  {
    title: "Trust, built into every step",
    description:
      "Clear communication and considered guidance help people make confident decisions at every stage of their property journey.",
  },
  {
    title: "Design that earns its place",
    description:
      "Architecture, amenities and everyday functionality are brought together to make each address feel purposeful and enduring.",
  },
  {
    title: "A long view of growth",
    description:
      "From new neighbourhoods in Noida to established destinations across the region, each development contributes to a wider urban story.",
  },
  {
    title: "Places for people",
    description:
      "Homes and destinations matter most when they support the routines, connections and ambitions of the people who use them.",
  },
];

export function OurJourneySection() {
  const [activePrinciple, setActivePrinciple] = useState(0);
  const selectedPrinciple = principles[activePrinciple];

  return (
    <section
      aria-labelledby="about-title"
      className="journey-section"
      id="about"
    >
      <div className="journey-section__inner">
        <div className="journey-section__intro">
          <p className="section-label journey-section__label">
            <span className="section-label__rule" />
            Our Journey
          </p>
          <h2 id="about-title">
            A track record.
            <br />
            <em>A way of thinking.</em>
          </h2>
          <p className="journey-section__summary">
            Since 2010, M3M India has grown around a clear belief: lasting
            places begin with trust, thoughtful design and a commitment to
            people. That belief continues to shape our growing collection of
            residential and commercial addresses in Noida.
          </p>
        </div>

        <div className="journey-section__content">
          <div className="journey-values" role="group" aria-label="Our values">
            {principles.map((principle, index) => (
              <button
                aria-pressed={activePrinciple === index}
                className={`journey-values__item${activePrinciple === index ? " is-active" : ""}`}
                id={`journey-value-${index}`}
                key={principle.title}
                onClick={() => setActivePrinciple(index)}
                type="button"
              >
                <span>{String(index + 1).padStart(2, "0")}</span>
                <strong>{principle.title}</strong>
                <span aria-hidden="true">↗</span>
              </button>
            ))}
          </div>

          <div
            aria-labelledby={`journey-value-${activePrinciple}`}
            className="journey-value-panel"
            id="journey-value-panel"
            aria-live="polite"
            tabIndex={0}
          >
            <span className="journey-value-panel__mark" aria-hidden="true">
              0{activePrinciple + 1}
            </span>
            <h3>{selectedPrinciple.title}</h3>
            <p>{selectedPrinciple.description}</p>
            <a
              href="https://m3mindia.com/our-story"
              rel="noreferrer"
              target="_blank"
            >
              Read more about M3M India
              <span aria-hidden="true">↗</span>
            </a>
          </div>
        </div>

        <div className="journey-stats" aria-label="M3M India at a glance">
          <div>
            <strong>2010</strong>
            <span>Founded</span>
          </div>
          <div>
            <strong>66</strong>
            <span>Projects in the portfolio</span>
          </div>
          <div>
            <strong>43</strong>
            <span>Projects completed</span>
          </div>
          <p>
            Company figures as stated on the{" "}
            <a
              href="https://m3mindia.com/our-story"
              rel="noreferrer"
              target="_blank"
            >
              M3M India website
            </a>
            .
          </p>
        </div>
      </div>
    </section>
  );
}
