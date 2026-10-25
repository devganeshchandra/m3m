"use client";

import { useEffect, useRef, useState, type FormEvent } from "react";
import { ArrowIcon } from "@/components/ui/ArrowIcon";
import {
  initialValues,
  validateEmail,
  validateField,
  validateName,
  validatePhone,
  type EnquiryErrors,
  type EnquiryValues,
} from "@/components/enquiry/enquiryValidation";

export function EnquiryExperience() {
  const [open, setOpen] = useState(false);
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState<EnquiryErrors>({});
  const [status, setStatus] = useState("");
  const dialogRef = useRef<HTMLDialogElement>(null);
  const formRef = useRef<HTMLFormElement>(null);

  useEffect(() => {
    const handleOpen = () => {
      setValues(initialValues);
      setErrors({});
      setStatus("");
      setOpen(true);
    };

    window.addEventListener("m3m:open-enquiry", handleOpen);
    return () => {
      window.removeEventListener("m3m:open-enquiry", handleOpen);
    };
  }, []);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;

    if (open && !dialog.open) {
      dialog.showModal();
    } else if (!open && dialog.open) {
      dialog.close();
    }
  }, [open]);

  const closeDialog = () => setOpen(false);

  const updateField = <K extends keyof EnquiryValues>(
    field: K,
    value: EnquiryValues[K],
  ) => {
    const updatedValues = { ...values, [field]: value };
    setValues(updatedValues);
    setErrors((current) => ({
      ...current,
      [field]: validateField(field, updatedValues),
    }));
    setStatus("");
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const nextErrors = (
      Object.keys(values) as (keyof EnquiryValues)[]
    ).reduce<EnquiryErrors>((fieldErrors, field) => {
      const error = validateField(field, values);
      if (error) fieldErrors[field] = error;
      return fieldErrors;
    }, {});

    setErrors(nextErrors);
    setStatus("");

    const firstInvalidField = Object.keys(nextErrors)[0];
    if (firstInvalidField) {
      formRef.current
        ?.querySelector<HTMLElement>(`[name="${firstInvalidField}"]`)
        ?.focus();
      return;
    }

    setStatus(
      "Your details passed validation, but online enquiries are not connected yet. Your information has not been sent. Please call or WhatsApp our team for now.",
    );
  };

  return (
    <dialog
      aria-labelledby="enquiry-title"
      className="enquiry-dialog"
      onClick={(event) => {
        if (event.target === dialogRef.current) closeDialog();
      }}
      onClose={() => setOpen(false)}
      ref={dialogRef}
    >
      <div className="enquiry-dialog__layout">
        <aside className="enquiry-dialog__aside">
          <div className="enquiry-dialog__image-copy">
            <p className="eyebrow">M3M India · Private consultation</p>
            <p className="enquiry-dialog__aside-title">A considered address.</p>
            <p className="enquiry-dialog__assurance">
              Begin with a conversation. Explore at your own pace.
            </p>
          </div>
        </aside>

        <section className="enquiry-dialog__content">
          <button
            aria-label="Close enquiry form"
            className="enquiry-dialog__close"
            onClick={closeDialog}
            type="button"
          >
            <span aria-hidden="true">&times;</span>
          </button>
          <h2 className="enquiry-dialog__title" id="enquiry-title">
            Enquire now
          </h2>
          <p className="enquiry-dialog__intro">
            Share your details and preferred call time to begin a conversation
            about M3M residences.
          </p>
          <ul className="enquiry-dialog__benefits">
            <li>Personal project guidance</li>
            <li>Choose a convenient call window</li>
          </ul>
          <p className="enquiry-dialog__availability" role="note">
            Enquiry delivery is not connected yet. This preview does not send or
            save your details; call or WhatsApp our team below to reach us now.
          </p>

          <form
            className="enquiry-form"
            noValidate
            onSubmit={handleSubmit}
            ref={formRef}
          >
            <label className="enquiry-field">
              <span className="enquiry-field__label">Full name</span>
              <input
                aria-describedby={
                  errors.name ? "enquiry-name-error" : "enquiry-name-hint"
                }
                aria-invalid={Boolean(errors.name)}
                autoComplete="name"
                maxLength={80}
                name="name"
                onBlur={() =>
                  setErrors((current) => ({
                    ...current,
                    name: validateName(values.name),
                  }))
                }
                onChange={(event) => updateField("name", event.target.value)}
                placeholder="Full name"
                required
                value={values.name}
              />
              <span className="enquiry-field__hint" id="enquiry-name-hint">
                Please use your name as it appears in conversation.
              </span>
              {errors.name && (
                <span className="enquiry-field__error" id="enquiry-name-error">
                  {errors.name}
                </span>
              )}
            </label>

            <div className="enquiry-form__row">
              <label className="enquiry-field">
                <span className="enquiry-field__label">Mobile / WhatsApp</span>
                <input
                  aria-describedby={
                    errors.phone ? "enquiry-phone-error" : "enquiry-phone-hint"
                  }
                  aria-invalid={Boolean(errors.phone)}
                  autoComplete="tel"
                  inputMode="tel"
                  maxLength={25}
                  name="phone"
                  onBlur={() =>
                    setErrors((current) => ({
                      ...current,
                      phone: validatePhone(values.phone),
                    }))
                  }
                  onChange={(event) => updateField("phone", event.target.value)}
                  placeholder="Mobile number"
                  required
                  type="tel"
                  value={values.phone}
                />
                <span className="enquiry-field__hint" id="enquiry-phone-hint">
                  Enter 10 digits for India, or add +country code if calling
                  internationally.
                </span>
                {errors.phone && (
                  <span
                    className="enquiry-field__error"
                    id="enquiry-phone-error"
                  >
                    {errors.phone}
                  </span>
                )}
              </label>

              <label className="enquiry-field">
                <span className="enquiry-field__label">
                  Preferred call time
                </span>
                <select
                  aria-describedby={
                    errors.callTime ? "enquiry-time-error" : "enquiry-time-hint"
                  }
                  aria-invalid={Boolean(errors.callTime)}
                  name="callTime"
                  onBlur={() =>
                    setErrors((current) => ({
                      ...current,
                      callTime: validateField("callTime", values),
                    }))
                  }
                  onChange={(event) =>
                    updateField("callTime", event.target.value)
                  }
                  required
                  value={values.callTime}
                >
                  <option value="">Choose a convenient window</option>
                  <option value="morning">Morning · 9:00 AM–12:00 PM</option>
                  <option value="afternoon">Afternoon · 12:00–3:00 PM</option>
                  <option value="evening">Evening · 3:00–6:00 PM</option>
                  <option value="flexible">I’m flexible</option>
                </select>
                <span className="enquiry-field__hint" id="enquiry-time-hint">
                  Time windows are in your local time; our team will confirm
                  availability.
                </span>
                {errors.callTime && (
                  <span
                    className="enquiry-field__error"
                    id="enquiry-time-error"
                  >
                    {errors.callTime}
                  </span>
                )}
              </label>
            </div>

            <label className="enquiry-field">
              <span className="enquiry-field__label">Email address</span>
              <input
                aria-describedby={
                  errors.email ? "enquiry-email-error" : "enquiry-email-hint"
                }
                aria-invalid={Boolean(errors.email)}
                autoComplete="email"
                maxLength={254}
                name="email"
                onBlur={() =>
                  setErrors((current) => ({
                    ...current,
                    email: validateEmail(values.email),
                  }))
                }
                onChange={(event) => updateField("email", event.target.value)}
                placeholder="Email address"
                required
                type="email"
                value={values.email}
              />
              <span className="enquiry-field__hint" id="enquiry-email-hint">
                We’ll use this only to follow up on your enquiry.
              </span>
              {errors.email && (
                <span className="enquiry-field__error" id="enquiry-email-error">
                  {errors.email}
                </span>
              )}
            </label>

            <label className="enquiry-consent">
              <input
                aria-describedby={
                  errors.consent ? "enquiry-consent-error" : undefined
                }
                aria-invalid={Boolean(errors.consent)}
                checked={values.consent}
                name="consent"
                onChange={(event) =>
                  updateField("consent", event.target.checked)
                }
                required
                type="checkbox"
              />
              <span>
                I agree to be contacted by M3M India about this enquiry. My
                details will not be used for unrelated marketing.
              </span>
            </label>
            {errors.consent && (
              <span className="enquiry-field__error" id="enquiry-consent-error">
                {errors.consent}
              </span>
            )}

            <div
              aria-live="polite"
              className="enquiry-form__status"
              role="status"
            >
              {status && <p>{status}</p>}
            </div>
            <button className="enquiry-form__submit" type="submit">
              Request a private call / virtual tour
              <ArrowIcon />
            </button>
          </form>

          <div className="enquiry-dialog__contact">
            <span>For immediate assistance</span>
            <a href="tel:18001233333">Call 1800 123 3333</a>
            <a
              href="https://wa.me/919311995812"
              rel="noreferrer"
              target="_blank"
            >
              WhatsApp our team
            </a>
          </div>
        </section>
      </div>
    </dialog>
  );
}
