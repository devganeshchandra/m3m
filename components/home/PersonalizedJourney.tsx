"use client";

import Image from "next/image";
import Link from "next/link";
import { useId, useState, type FormEvent } from "react";
import {
  validateEmail,
  validatePhone,
} from "@/components/enquiry/enquiryValidation";
import { projects } from "@/components/projects/projectData";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

type Interest = "residential" | "commercial";
type Residency = "india" | "nri";
type FormErrors = Partial<
  Record<
    "interest" | "project" | "residency" | "phone" | "email" | "consent",
    string
  >
>;

const steps = [
  "Choose a direction",
  "Build your M3M edit",
  "Request your guide",
];

export function PersonalizedJourney() {
  const id = useId();
  const [step, setStep] = useState(0);
  const [interest, setInterest] = useState<Interest | "">("");
  const [selectedProjectSlug, setSelectedProjectSlug] = useState("");
  const [residency, setResidency] = useState<Residency | "">("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [consent, setConsent] = useState(false);
  const [errors, setErrors] = useState<FormErrors>({});
  const [status, setStatus] = useState("");

  const matchingProjects = interest
    ? projects.filter((project) => project.interests.includes(interest))
    : [];
  const selectedProject = projects.find(
    (project) => project.slug === selectedProjectSlug,
  );

  const goToNextStep = () => {
    const nextErrors: FormErrors = {};

    if (step === 0 && !interest) {
      nextErrors.interest = "Choose the direction that feels right for you.";
    }
    if (step === 1 && !selectedProject) {
      nextErrors.project = "Choose a project for your personal M3M edit.";
    }
    if (step === 1 && !residency) {
      nextErrors.residency = "Choose the option that best describes you.";
    }

    setErrors(nextErrors);
    setStatus("");

    const firstError = Object.keys(nextErrors)[0];
    if (firstError) {
      const target =
        firstError === "interest"
          ? `input[name="${id}-interest"]`
          : firstError === "project"
            ? `input[name="${id}-project"]`
            : `input[name="${id}-residency"]`;
      document.querySelector<HTMLInputElement>(target)?.focus();
      return;
    }

    setStep((current) => Math.min(current + 1, steps.length - 1));
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const nextErrors: FormErrors = {};
    const phoneError = validatePhone(phone);
    const emailError = validateEmail(email);

    if (phoneError) nextErrors.phone = phoneError;
    if (emailError) nextErrors.email = emailError;
    if (!consent) {
      nextErrors.consent =
        "Please confirm that we may contact you about this request.";
    }

    setErrors(nextErrors);
    setStatus("");

    const firstError = Object.keys(nextErrors)[0];
    if (firstError) {
      document.getElementById(`${id}-${firstError}`)?.focus();
      return;
    }

    setStatus(
      "This preview is not connected to lead delivery, so your request has not been sent or saved. Please call or WhatsApp our team to continue.",
    );
  };

  const updateInterest = (value: Interest) => {
    setInterest(value);
    setSelectedProjectSlug(
      projects.find((project) => project.interests.includes(value))?.slug ?? "",
    );
    setErrors((current) => ({
      ...current,
      interest: undefined,
      project: undefined,
    }));
    setStatus("");
  };

  const updateProject = (slug: string) => {
    setSelectedProjectSlug(slug);
    setErrors((current) => ({ ...current, project: undefined }));
    setStatus("");
  };

  const updateResidency = (value: Residency) => {
    setResidency(value);
    setErrors((current) => ({ ...current, residency: undefined }));
    setStatus("");
  };

  return (
    <section
      aria-labelledby={`${id}-title`}
      className="guided-section"
      id="personalised-guidance"
    >
      <div className="guided-section__inner">
        <div className="guided-section__header">
          <p className="section-label guided-section__label">
            <span className="section-label__rule" />
            Your M3M edit
          </p>
          <h2 id={`${id}-title`}>Explore projects that feel right.</h2>
          <p>
            Choose what you’re looking for to discover a shortlist of M3M
            addresses.
          </p>
        </div>

        <form
          aria-label="Build a personal M3M project shortlist"
          className="guided-card"
          noValidate
          onSubmit={handleSubmit}
        >
          <div
            aria-label={`Step ${step + 1} of ${steps.length}: ${steps[step]}`}
            className="guided-card__progress"
          >
            <div className="guided-card__progress-copy">
              <span>PROJECT DISCOVERY</span>
              <span>
                {String(step + 1).padStart(2, "0")} /{" "}
                {String(steps.length).padStart(2, "0")}
              </span>
            </div>
            <div aria-hidden="true" className="guided-card__progress-track">
              <span
                style={{ width: `${((step + 1) / steps.length) * 100}%` }}
              />
            </div>
          </div>

          <div aria-live="polite" className="guided-card__step-heading">
            <h3>{steps[step]}</h3>
          </div>

          {step === 0 && (
            <fieldset
              aria-describedby={
                errors.interest ? `${id}-interest-error` : undefined
              }
              aria-invalid={Boolean(errors.interest)}
              className="guided-options"
            >
              <legend className="visually-hidden">
                What are you exploring?
              </legend>
              <label
                className={`guided-option${interest === "residential" ? " is-selected" : ""}`}
              >
                <input
                  checked={interest === "residential"}
                  id={`${id}-residential`}
                  name={`${id}-interest`}
                  onChange={() => updateInterest("residential")}
                  type="radio"
                  value="residential"
                />
                <span className="guided-option__copy">
                  <span className="guided-option__title">Residential</span>
                  <span className="guided-option__detail">
                    Apartments, penthouses &amp; homes
                  </span>
                </span>
                <span className="guided-option__arrow">
                  <ArrowIcon />
                </span>
              </label>

              <label
                className={`guided-option${interest === "commercial" ? " is-selected" : ""}`}
              >
                <input
                  checked={interest === "commercial"}
                  id={`${id}-commercial`}
                  name={`${id}-interest`}
                  onChange={() => updateInterest("commercial")}
                  type="radio"
                  value="commercial"
                />
                <span className="guided-option__copy">
                  <span className="guided-option__title">Commercial</span>
                  <span className="guided-option__detail">
                    Retail, dining &amp; business spaces
                  </span>
                </span>
                <span className="guided-option__arrow">
                  <ArrowIcon />
                </span>
              </label>
              {errors.interest && (
                <span
                  className="guided-card__error"
                  id={`${id}-interest-error`}
                  role="alert"
                >
                  {errors.interest}
                </span>
              )}
            </fieldset>
          )}

          {step === 1 && (
            <div className="guided-match">
              <div className="guided-match__heading">
                <p>
                  {matchingProjects.length} ADDRESSES TO EXPLORE
                  <span aria-hidden="true"> · </span>
                  SELECT ONE FOR YOUR EDIT
                </p>
                <div
                  aria-describedby={
                    errors.project ? `${id}-project-error` : undefined
                  }
                  aria-invalid={Boolean(errors.project)}
                  aria-label="Choose a project"
                  className="guided-match__rail"
                  role="radiogroup"
                >
                  {matchingProjects.map((project) => (
                    <label
                      className={`guided-project-choice${selectedProjectSlug === project.slug ? " is-selected" : ""}`}
                      key={project.slug}
                    >
                      <input
                        checked={selectedProjectSlug === project.slug}
                        name={`${id}-project`}
                        onChange={() => updateProject(project.slug)}
                        type="radio"
                        value={project.slug}
                      />
                      <span className="guided-project-choice__image">
                        <Image alt="" fill sizes="180px" src={project.image} />
                        <span className="guided-project-choice__check">
                          <span aria-hidden="true">✓</span>
                        </span>
                      </span>
                      <span className="guided-project-choice__copy">
                        <span>{project.category}</span>
                        <strong>{project.name}</strong>
                        <span>{project.location}</span>
                      </span>
                    </label>
                  ))}
                </div>
                {errors.project && (
                  <span
                    className="guided-card__error"
                    id={`${id}-project-error`}
                    role="alert"
                  >
                    {errors.project}
                  </span>
                )}
              </div>

              {selectedProject && (
                <article className="guided-match__preview">
                  <div className="guided-match__preview-image">
                    <Image
                      alt={selectedProject.name}
                      fill
                      sizes="(max-width: 800px) 100vw, 220px"
                      src={selectedProject.image}
                    />
                    <span>YOUR CURRENT MATCH</span>
                  </div>
                  <div className="guided-match__preview-copy">
                    <p>{selectedProject.category}</p>
                    <h4>{selectedProject.name}</h4>
                    <span>{selectedProject.offering}</span>
                    <Link
                      href={`/projects/${selectedProject.slug}`}
                      rel="noreferrer"
                      target="_blank"
                    >
                      Explore project
                      <ArrowIcon />
                    </Link>
                  </div>
                </article>
              )}

              <fieldset
                aria-describedby={
                  errors.residency ? `${id}-residency-error` : undefined
                }
                aria-invalid={Boolean(errors.residency)}
                className="guided-residency"
              >
                <legend>And where are you based?</legend>
                <div className="guided-residency__options">
                  <label className={residency === "india" ? "is-selected" : ""}>
                    <input
                      checked={residency === "india"}
                      id={`${id}-india`}
                      name={`${id}-residency`}
                      onChange={() => updateResidency("india")}
                      type="radio"
                      value="india"
                    />
                    <span>India</span>
                  </label>
                  <label className={residency === "nri" ? "is-selected" : ""}>
                    <input
                      checked={residency === "nri"}
                      id={`${id}-nri`}
                      name={`${id}-residency`}
                      onChange={() => updateResidency("nri")}
                      type="radio"
                      value="nri"
                    />
                    <span>Overseas (NRI)</span>
                  </label>
                </div>
                {errors.residency && (
                  <span
                    className="guided-card__error"
                    id={`${id}-residency-error`}
                    role="alert"
                  >
                    {errors.residency}
                  </span>
                )}
              </fieldset>
            </div>
          )}

          {step === 2 && (
            <div className="guided-contact">
              {selectedProject && (
                <div className="guided-contact__match">
                  <span>YOUR SELECTED ADDRESS</span>
                  <strong>{selectedProject.name}</strong>
                  <span>
                    {selectedProject.location} ·{" "}
                    {residency === "nri" ? "Overseas (NRI)" : "Based in India"}
                  </span>
                </div>
              )}
              <p className="guided-contact__intro">
                Want a project guide or a personal conversation? Share the
                details below and our team can follow up about this address.
              </p>
              <label className="guided-contact__field">
                <span>Email address</span>
                <input
                  aria-describedby={
                    errors.email ? `${id}-email-error` : undefined
                  }
                  aria-invalid={Boolean(errors.email)}
                  autoComplete="email"
                  id={`${id}-email`}
                  maxLength={254}
                  name="email"
                  onChange={(event) => {
                    setEmail(event.target.value);
                    setErrors((current) => ({ ...current, email: undefined }));
                    setStatus("");
                  }}
                  placeholder="name@example.com"
                  required
                  type="email"
                  value={email}
                />
                {errors.email && (
                  <span
                    className="guided-card__error"
                    id={`${id}-email-error`}
                    role="alert"
                  >
                    {errors.email}
                  </span>
                )}
              </label>
              <label className="guided-contact__field">
                <span>Mobile / WhatsApp</span>
                <input
                  aria-describedby={
                    errors.phone ? `${id}-phone-error` : undefined
                  }
                  aria-invalid={Boolean(errors.phone)}
                  autoComplete="tel"
                  id={`${id}-phone`}
                  inputMode="tel"
                  maxLength={25}
                  name="phone"
                  onChange={(event) => {
                    setPhone(event.target.value);
                    setErrors((current) => ({ ...current, phone: undefined }));
                    setStatus("");
                  }}
                  placeholder="+91 00000 00000"
                  required
                  type="tel"
                  value={phone}
                />
                {errors.phone && (
                  <span
                    className="guided-card__error"
                    id={`${id}-phone-error`}
                    role="alert"
                  >
                    {errors.phone}
                  </span>
                )}
              </label>
              <label className="guided-contact__consent">
                <input
                  aria-describedby={
                    errors.consent ? `${id}-consent-error` : undefined
                  }
                  aria-invalid={Boolean(errors.consent)}
                  checked={consent}
                  id={`${id}-consent`}
                  name="consent"
                  onChange={(event) => {
                    setConsent(event.target.checked);
                    setErrors((current) => ({
                      ...current,
                      consent: undefined,
                    }));
                    setStatus("");
                  }}
                  required
                  type="checkbox"
                />
                <span>
                  M3M India may contact me about this selected project using the
                  details provided.
                </span>
              </label>
              {errors.consent && (
                <span
                  className="guided-card__error"
                  id={`${id}-consent-error`}
                  role="alert"
                >
                  {errors.consent}
                </span>
              )}
              <p className="guided-contact__privacy">
                Your information is for this enquiry only. It isn’t submitted
                until you choose to request a conversation.
              </p>
            </div>
          )}

          <div className="guided-card__actions">
            {step > 0 ? (
              <button
                className="guided-card__back"
                onClick={() => {
                  setStep((current) => Math.max(current - 1, 0));
                  setErrors({});
                  setStatus("");
                }}
                type="button"
              >
                <ArrowIcon />
                Back
              </button>
            ) : (
              <span className="guided-card__footnote">
                No account. No commitment. Just your own shortlist.
              </span>
            )}
            {step < steps.length - 1 ? (
              <button
                className="guided-card__continue"
                onClick={goToNextStep}
                type="button"
              >
                {step === 0 ? "Show my edit" : "Continue"}
                <ArrowIcon />
              </button>
            ) : (
              <button className="guided-card__continue" type="submit">
                Request a conversation
                <ArrowIcon />
              </button>
            )}
          </div>
          <p aria-live="polite" className="guided-card__status" role="status">
            {status}
          </p>
        </form>
      </div>
    </section>
  );
}
