import { parsePhoneNumberFromString } from "libphonenumber-js/min";

export type EnquiryValues = {
  name: string;
  phone: string;
  email: string;
  callTime: string;
  consent: boolean;
};

export type EnquiryErrors = Partial<Record<keyof EnquiryValues, string>>;

export const initialValues: EnquiryValues = {
  name: "",
  phone: "",
  email: "",
  callTime: "",
  consent: false,
};

export function validateName(value: string) {
  const name = value.trim().replace(/\s+/g, " ");
  const letterCount = (name.match(/\p{L}/gu) ?? []).length;
  const namePattern =
    /^\p{L}[\p{L}\p{M}]*(?:['’.-][\p{L}\p{M}]+)*\.?(?: \p{L}[\p{L}\p{M}]*(?:['’.-][\p{L}\p{M}]+)*\.?)*$/u;

  return letterCount >= 2 && namePattern.test(name)
    ? ""
    : "Enter your name using letters. Spaces, hyphens and apostrophes are fine.";
}

export function validateEmail(value: string) {
  const email = value.trim();
  const [localPart, ...domainParts] = email.split("@");
  if (domainParts.length !== 1 || !localPart || !domainParts[0]) {
    return "Enter a valid email address, such as name@example.com.";
  }

  const domain = domainParts[0];
  const labels = domain.split(".");
  const localPattern =
    /^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*$/;
  const labelPattern = /^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$/;
  const topLevelDomain = labels[labels.length - 1];

  return email.length <= 254 &&
    localPart.length <= 64 &&
    localPattern.test(localPart) &&
    labels.length >= 2 &&
    labels.every((label) => label.length <= 63 && labelPattern.test(label)) &&
    (/^[A-Za-z]{2,63}$/.test(topLevelDomain) ||
      /^xn--[A-Za-z0-9-]{2,59}$/.test(topLevelDomain))
    ? ""
    : "Enter a valid email address, such as name@example.com.";
}

export function validatePhone(value: string) {
  const input = value.trim();
  const phone = input.startsWith("+")
    ? parsePhoneNumberFromString(input, { extract: false })
    : parsePhoneNumberFromString(input, {
        defaultCountry: "IN",
        extract: false,
      });

  if (!phone?.isValid() || /^(\d)\1+$/.test(phone.nationalNumber)) {
    return "Enter a valid 10-digit Indian mobile number, or include +country code for an international number.";
  }

  return "";
}

export function validateField<K extends keyof EnquiryValues>(
  field: K,
  values: EnquiryValues,
): string {
  switch (field) {
    case "name":
      return validateName(values.name);
    case "phone":
      return validatePhone(values.phone);
    case "email":
      return validateEmail(values.email);
    case "callTime":
      return values.callTime ? "" : "Choose a preferred time for your call.";
    case "consent":
      return values.consent
        ? ""
        : "Please confirm that we may contact you about this enquiry.";
  }
}
