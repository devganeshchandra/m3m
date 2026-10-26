/*
 * Enquiry form validation. Mirrors leads/validation.py on the server —
 * keep the two in step.
 */
(function () {
  "use strict";

  var NAME_ERROR =
    "Enter your name using letters. Spaces, hyphens and apostrophes are fine.";
  var EMAIL_ERROR = "Enter a valid email address, such as name@example.com.";
  var PHONE_ERROR =
    "Enter a valid 10-digit Indian mobile number, or include +country code for an international number.";
  var CALL_TIME_ERROR = "Choose a preferred time for your call.";
  var CONSENT_ERROR =
    "Please confirm that we may contact you about this enquiry.";
  // Ad landing pages: extra checks against junk leads (mirrors validate_real_name / validate_lead_email).
  var JUNK_NAME_ERROR = "Please enter your real full name so our team can address you properly.";
  var DISPOSABLE_EMAIL_ERROR = "Please use a permanent email address so we can send you the details.";
  var INTEREST_ERROR = "Choose residential or commercial.";
  var JUNK_NAMES = [
    "test", "testing", "tester", "asdf", "asd", "qwerty", "abc", "abcd", "xyz", "na", "none", "null",
    "name", "fullname", "full name", "user", "demo", "sample", "fake", "aaa", "xxx", "hello", "hi",
  ];
  var DISPOSABLE_DOMAINS = [
    "mailinator.com", "guerrillamail.com", "10minutemail.com", "tempmail.com", "temp-mail.org",
    "yopmail.com", "trashmail.com", "getnada.com", "sharklasers.com", "dispostable.com",
    "throwawaymail.com", "maildrop.cc", "fakeinbox.com", "mintemail.com", "emailondeck.com",
    "example.com", "example.org", "test.com",
  ];

  function validateRealName(value) {
    var name = String(value || "").trim().replace(/\s+/g, " ");
    var error = validateName(name);
    if (error) return error;
    var lower = name.toLowerCase();
    var compact = lower.replace(/ /g, "");
    var distinct = new Set(compact.split("")).size;
    return JUNK_NAMES.indexOf(lower) !== -1 || JUNK_NAMES.indexOf(compact) !== -1 || distinct <= 2
      ? JUNK_NAME_ERROR
      : "";
  }

  function validateLeadEmail(value) {
    var error = validateEmail(value);
    if (error) return error;
    var domain = String(value).trim().split("@").pop().toLowerCase();
    return DISPOSABLE_DOMAINS.indexOf(domain) !== -1 ? DISPOSABLE_EMAIL_ERROR : "";
  }

  function validateName(value) {
    var name = String(value || "").trim().replace(/\s+/g, " ");
    var letterCount = (name.match(/\p{L}/gu) || []).length;
    var namePattern =
      /^\p{L}[\p{L}\p{M}]*(?:['’.-][\p{L}\p{M}]+)*\.?(?: \p{L}[\p{L}\p{M}]*(?:['’.-][\p{L}\p{M}]+)*\.?)*$/u;
    return letterCount >= 2 && namePattern.test(name) ? "" : NAME_ERROR;
  }

  function validateEmail(value) {
    var email = String(value || "").trim();
    var parts = email.split("@");
    if (parts.length !== 2 || !parts[0] || !parts[1]) return EMAIL_ERROR;

    var localPart = parts[0];
    var labels = parts[1].split(".");
    var localPattern =
      /^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*$/;
    var labelPattern = /^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$/;
    var topLevelDomain = labels[labels.length - 1];

    return email.length <= 254 &&
      localPart.length <= 64 &&
      localPattern.test(localPart) &&
      labels.length >= 2 &&
      labels.every(function (label) {
        return label.length <= 63 && labelPattern.test(label);
      }) &&
      (/^[A-Za-z]{2,63}$/.test(topLevelDomain) ||
        /^xn--[A-Za-z0-9-]{2,59}$/.test(topLevelDomain))
      ? ""
      : EMAIL_ERROR;
  }

  function validatePhone(value) {
    var input = String(value || "").trim();
    var lib = window.libphonenumber;
    if (!lib) return input.replace(/\D/g, "").length >= 10 ? "" : PHONE_ERROR;

    var phone = input.charAt(0) === "+"
      ? lib.parsePhoneNumberFromString(input, { extract: false })
      : lib.parsePhoneNumberFromString(input, { defaultCountry: "IN", extract: false });

    if (!phone || !phone.isValid() || /^(\d)\1+$/.test(phone.nationalNumber)) {
      return PHONE_ERROR;
    }
    return "";
  }

  function validateControl(control) {
    switch (control.dataset.validate) {
      case "name":
        return validateName(control.value);
      case "phone":
        return validatePhone(control.value);
      case "email":
        return validateEmail(control.value);
      case "callTime":
        return control.value ? "" : CALL_TIME_ERROR;
      case "realName":
        return validateRealName(control.value);
      case "leadEmail":
        return validateLeadEmail(control.value);
      case "choice":
        return control.value ? "" : control.dataset.requiredMessage || "Please choose an option.";
      case "interest":
        return control.value === "residential" || control.value === "commercial" ? "" : INTEREST_ERROR;
      case "consent":
        return control.checked ? "" : control.dataset.consentMessage || CONSENT_ERROR;
      default:
        return "";
    }
  }

  window.M3MValidation = {
    validateName: validateName,
    validateEmail: validateEmail,
    validatePhone: validatePhone,
    validateControl: validateControl,
  };
})();
