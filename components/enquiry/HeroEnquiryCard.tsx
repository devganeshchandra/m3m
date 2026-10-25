"use client";

import { useId, useRef, useState, type FormEvent } from "react";
import {
  initialValues,
  validateEmail,
  validateField,
  validateName,
  validatePhone,
  type EnquiryErrors,
  type EnquiryValues,
} from "@/components/enquiry/enquiryValidation";

export function HeroEnquiryCard() {
  const id = useId();
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState<EnquiryErrors>({});
  const [status, setStatus] = useState("");
  const formRef = useRef<HTMLFormElement>(null);

  const fieldId = (field: keyof EnquiryValues) => `${id}-${field}`;
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
      "Online enquiries are not connected yet, so your details have not been sent or saved. Please call or WhatsApp our team for now.",
    );
  };

  return (
    <aside className="hero-enquiry" aria-labelledby={`${id}-title`}>
      <p className="hero-enquiry__eyebrow">A more personal conversation</p>
      <h2 className="hero-enquiry__title" id={`${id}-title`}>
        Enquire with us
      </h2>
      <p className="hero-enquiry__intro">
        Request a private call with our residences team.
      </p>

      <form
        className="hero-enquiry__form"
        noValidate
        onSubmit={handleSubmit}
        ref={formRef}
      >
        <label className="hero-enquiry__field">
          <span>Full name</span>
          <input
            aria-describedby={
              errors.name ? `${fieldId("name")}-error` : undefined
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
            placeholder="Your name"
            required
            value={values.name}
          />
          {errors.name && (
            <span
              className="hero-enquiry__error"
              id={`${fieldId("name")}-error`}
            >
              {errors.name}
            </span>
          )}
        </label>

        <div className="hero-enquiry__row">
          <label className="hero-enquiry__field">
            <span>Mobile / WhatsApp</span>
            <input
              aria-describedby={
                errors.phone ? `${fieldId("phone")}-error` : undefined
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
            {errors.phone && (
              <span
                className="hero-enquiry__error"
                id={`${fieldId("phone")}-error`}
              >
                {errors.phone}
              </span>
            )}
          </label>

          <label className="hero-enquiry__field">
            <span>Preferred call time</span>
            <select
              aria-describedby={
                errors.callTime ? `${fieldId("callTime")}-error` : undefined
              }
              aria-invalid={Boolean(errors.callTime)}
              name="callTime"
              onChange={(event) => updateField("callTime", event.target.value)}
              required
              value={values.callTime}
            >
              <option value="">Choose a window</option>
              <option value="morning">Morning · 9 AM–12 PM</option>
              <option value="afternoon">Afternoon · 12–3 PM</option>
              <option value="evening">Evening · 3–6 PM</option>
              <option value="flexible">I’m flexible</option>
            </select>
            {errors.callTime && (
              <span
                className="hero-enquiry__error"
                id={`${fieldId("callTime")}-error`}
              >
                {errors.callTime}
              </span>
            )}
          </label>
        </div>

        <label className="hero-enquiry__field">
          <span>Email address</span>
          <input
            aria-describedby={
              errors.email ? `${fieldId("email")}-error` : undefined
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
            placeholder="name@example.com"
            required
            type="email"
            value={values.email}
          />
          {errors.email && (
            <span
              className="hero-enquiry__error"
              id={`${fieldId("email")}-error`}
            >
              {errors.email}
            </span>
          )}
        </label>

        <label className="hero-enquiry__consent">
          <input
            aria-describedby={
              errors.consent ? `${fieldId("consent")}-error` : undefined
            }
            aria-invalid={Boolean(errors.consent)}
            checked={values.consent}
            name="consent"
            onChange={(event) => updateField("consent", event.target.checked)}
            required
            type="checkbox"
          />
          <span>May we contact you about this enquiry?</span>
        </label>
        {errors.consent && (
          <span
            className="hero-enquiry__error"
            id={`${fieldId("consent")}-error`}
          >
            {errors.consent}
          </span>
        )}

        <div aria-live="polite" className="hero-enquiry__status" role="status">
          {status}
        </div>
        <button className="hero-enquiry__submit" type="submit">
          Request a private call / virtual tour{" "}
          <span aria-hidden="true">→</span>
        </button>
      </form>
      <p className="hero-enquiry__note">
        Your details are not sent or stored in this preview.
      </p>
    </aside>
  );
}
