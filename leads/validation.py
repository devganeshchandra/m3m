"""
Server-side versions of the rules in static/js/validation.js.
Keep the two files in step so visitors see the same messages either way.
"""

import re
import unicodedata

import phonenumbers

NAME_ERROR = "Enter your name using letters. Spaces, hyphens and apostrophes are fine."
EMAIL_ERROR = "Enter a valid email address, such as name@example.com."
PHONE_ERROR = (
    "Enter a valid 10-digit Indian mobile number, or include +country code for an international number."
)

_LOCAL_PART = re.compile(r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*$")
_DOMAIN_LABEL = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")
_TLD = re.compile(r"^[A-Za-z]{2,63}$")
_IDN_TLD = re.compile(r"^xn--[A-Za-z0-9-]{2,59}$")
_NAME_SEPARATORS = "'’.-"


def _is_letter(char):
    return unicodedata.category(char).startswith("L")


def _is_letter_or_mark(char):
    return unicodedata.category(char)[0] in {"L", "M"}


def _valid_name_word(word):
    # \p{L}[\p{L}\p{M}]*(?:['’.-][\p{L}\p{M}]+)*\.?
    if word.endswith(".") and len(word) > 1:
        word = word[:-1]
    if not word or not _is_letter(word[0]):
        return False
    previous_separator = False
    for char in word[1:]:
        if char in _NAME_SEPARATORS:
            if previous_separator:
                return False
            previous_separator = True
        elif _is_letter_or_mark(char):
            previous_separator = False
        else:
            return False
    return not previous_separator


def normalize_name(value):
    return " ".join((value or "").split())


def validate_name(value):
    name = normalize_name(value)
    letters = sum(1 for char in name if _is_letter(char))
    if letters >= 2 and all(_valid_name_word(word) for word in name.split(" ")):
        return ""
    return NAME_ERROR


# Extra checks for paid-ad landing pages, where junk leads cost money and sales time.
JUNK_NAME_ERROR = "Please enter your real full name so our team can address you properly."
DISPOSABLE_EMAIL_ERROR = "Please use a permanent email address so we can send you the details."
_JUNK_NAMES = {
    "test", "testing", "tester", "asdf", "asd", "qwerty", "abc", "abcd", "xyz", "na", "none", "null",
    "name", "fullname", "full name", "user", "demo", "sample", "fake", "aaa", "xxx", "hello", "hi",
}
_DISPOSABLE_DOMAINS = {
    "mailinator.com", "guerrillamail.com", "10minutemail.com", "tempmail.com", "temp-mail.org",
    "yopmail.com", "trashmail.com", "getnada.com", "sharklasers.com", "dispostable.com",
    "throwawaymail.com", "maildrop.cc", "fakeinbox.com", "mintemail.com", "emailondeck.com",
    "example.com", "example.org", "test.com",
}


def validate_real_name(value):
    """A full name that is not an obvious placeholder: no test words, not one letter repeated."""
    name = normalize_name(value)
    if message := validate_name(name):
        return message
    compact = name.lower().replace(" ", "")
    if name.lower() in _JUNK_NAMES or compact in _JUNK_NAMES or len(set(compact)) <= 2:
        return JUNK_NAME_ERROR
    return ""


def validate_lead_email(value):
    if message := validate_email(value):
        return message
    domain = (value or "").strip().rsplit("@", 1)[-1].lower()
    return DISPOSABLE_EMAIL_ERROR if domain in _DISPOSABLE_DOMAINS else ""


def validate_email(value):
    email = (value or "").strip()
    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return EMAIL_ERROR
    local_part, domain = parts
    labels = domain.split(".")
    tld = labels[-1]
    valid = (
        len(email) <= 254
        and len(local_part) <= 64
        and _LOCAL_PART.match(local_part)
        and len(labels) >= 2
        and all(len(label) <= 63 and _DOMAIN_LABEL.match(label) for label in labels)
        and (_TLD.match(tld) or _IDN_TLD.match(tld))
    )
    return "" if valid else EMAIL_ERROR


def parse_phone(value):
    """Return the number in E.164 format, or None if it is not valid."""
    raw = (value or "").strip()
    if not raw:
        return None
    try:
        number = phonenumbers.parse(raw, None if raw.startswith("+") else "IN")
    except phonenumbers.NumberParseException:
        return None
    national = str(number.national_number)
    if not phonenumbers.is_valid_number(number) or re.fullmatch(r"(\d)\1+", national):
        return None
    return phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)


def validate_phone(value):
    return "" if parse_phone(value) else PHONE_ERROR
