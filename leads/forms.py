from django import forms

from leads import validation
from leads.models import Enquiry
from projects.models import Project

CONSENT_ERROR = "Please confirm that we may contact you about this enquiry."
GUIDED_CONSENT_ERROR = "Please confirm that we may contact you about this request."


class EnquiryForm(forms.Form):
    """Handles all three website forms; `source` decides which fields are required."""

    source = forms.ChoiceField(choices=Enquiry.Source.choices)
    name = forms.CharField(max_length=80, required=False)
    phone = forms.CharField(max_length=25, required=False)
    email = forms.CharField(max_length=254, required=False)
    callTime = forms.CharField(max_length=20, required=False)
    interest = forms.CharField(max_length=20, required=False)
    residency = forms.CharField(max_length=20, required=False)
    project = forms.SlugField(max_length=120, required=False)
    consent = forms.BooleanField(required=False)
    message = forms.CharField(max_length=2000, required=False)
    # Billionaire Block private viewing: folded into the message for the sales team.
    residence = forms.CharField(max_length=80, required=False)
    visit_date = forms.DateField(required=False)
    chauffeur = forms.BooleanField(required=False)
    page_url = forms.CharField(max_length=1000, required=False)
    # Honeypot: real visitors never see or fill this field.
    website = forms.CharField(required=False)

    utm_source = forms.CharField(max_length=120, required=False)
    utm_medium = forms.CharField(max_length=120, required=False)
    utm_campaign = forms.CharField(max_length=120, required=False)
    utm_term = forms.CharField(max_length=120, required=False)
    utm_content = forms.CharField(max_length=120, required=False)

    def clean(self):
        data = super().clean()
        source = data.get("source")
        if not source:
            return data

        errors = {}
        if source in {Enquiry.Source.HERO, Enquiry.Source.POPUP, Enquiry.Source.CONTACT}:
            if data.get("callTime") not in Enquiry.CallTime.values:
                errors["callTime"] = "Choose a preferred time for your call."
        if source == Enquiry.Source.LANDING:
            if message := validation.validate_real_name(data.get("name")):
                errors["name"] = message
            if data.get("interest") not in Enquiry.Interest.values:
                errors["interest"] = "Choose residential or commercial."
            if message := validation.validate_lead_email(data.get("email")):
                errors["email"] = message
        elif source != Enquiry.Source.GUIDED:
            if message := validation.validate_name(data.get("name")):
                errors["name"] = message
        if source in Enquiry.BANNER_FORMS and data.get("interest") not in Enquiry.Interest.values:
            errors["interest"] = "Choose residential or commercial."

        if source == Enquiry.Source.GUIDED:
            if data.get("interest") not in Enquiry.Interest.values:
                errors["interest"] = "Choose the direction that feels right for you."
            if data.get("residency") not in Enquiry.Residency.values:
                errors["residency"] = "Choose the option that best describes you."
            if not data.get("project"):
                errors["project"] = "Choose a project for your personal M3M edit."

        phone = validation.parse_phone(data.get("phone"))
        if not phone:
            errors["phone"] = validation.PHONE_ERROR
        # The brochure form asks only for a name and phone number.
        if source not in {Enquiry.Source.BROCHURE, Enquiry.Source.LANDING} or (
            source == Enquiry.Source.BROCHURE and data.get("email")
        ):
            if message := validation.validate_email(data.get("email")):
                errors["email"] = message
        # These forms have no consent checkbox: sending them is the request to be contacted.
        # The landing page states the contact terms beside its submit button.
        no_consent = {
            Enquiry.Source.HERO,
            Enquiry.Source.BILLIONAIRE,
            Enquiry.Source.BROCHURE,
            Enquiry.Source.LANDING,
            *Enquiry.BANNER_FORMS,
        }
        if source not in no_consent and not data.get("consent"):
            errors["consent"] = GUIDED_CONSENT_ERROR if source == Enquiry.Source.GUIDED else CONSENT_ERROR

        project = None
        if data.get("project"):
            project = Project.objects.published().filter(slug=data["project"]).first()
            if project is None:
                errors["project"] = "Choose a project for your personal M3M edit."

        for field, message in errors.items():
            self.add_error(field, message)

        data["phone"] = phone
        data["project_obj"] = project
        return data

    def full_message(self):
        data = self.cleaned_data
        lines = []
        if data.get("residence"):
            lines.append(f"Preferred residence: {data['residence']}")
        if data.get("visit_date"):
            lines.append(f"Preferred date: {data['visit_date']:%d %b %Y}")
        if data.get("chauffeur"):
            lines.append("Chauffeur pickup requested")
        if data["source"] == Enquiry.Source.BROCHURE:
            lines.append("Brochure download")
        message = (data.get("message") or "").strip()
        return "\n".join(lines + ([""] if lines and message else []) + ([message] if message else []))

    def is_spam(self):
        return bool(self.cleaned_data.get("website"))

    def save(self, request):
        data = self.cleaned_data
        return Enquiry.objects.create(
            source=data["source"],
            project=data["project_obj"],
            name=validation.normalize_name(data.get("name")),
            phone=data["phone"],
            email=(data.get("email") or "").strip(),
            call_time=data.get("callTime") or "",
            interest=data.get("interest") or "",
            residency=data.get("residency") or "",
            consent=True,
            message=self.full_message(),
            page_url=(data.get("page_url") or request.headers.get("referer", ""))[:1000],
            utm_source=data.get("utm_source", ""),
            utm_medium=data.get("utm_medium", ""),
            utm_campaign=data.get("utm_campaign", ""),
            utm_term=data.get("utm_term", ""),
            utm_content=data.get("utm_content", ""),
            ip_address=client_ip(request),
            user_agent=request.headers.get("user-agent", "")[:500],
        )


def client_ip(request):
    forwarded = request.headers.get("x-forwarded-for")
    ip = forwarded.split(",")[0].strip() if forwarded else request.META.get("REMOTE_ADDR")
    return ip or None
