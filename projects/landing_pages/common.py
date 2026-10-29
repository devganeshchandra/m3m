"""Content slots shared by the project ad landing pages: the header and the rotating popup forms."""

HEADER = "Header"
POPUP = "Popup forms"

TEXTS = [
    (HEADER, "nav_enquire", "Last menu link (jumps to the final form)", "Enquire"),
    (HEADER, "nav_cta", "Header button", "Enquire now"),
    (HEADER, "nav_cta_popup", "Header button: popup title", "Request a callback"),
    (POPUP, "popup_interest", "Style B: step 1 heading", "I’m interested in"),
    (POPUP, "popup_send_to", "Style B: step 2 heading", "Where should we send it?"),
    (POPUP, "popup_looking_for", "Style A: list label", "Looking for"),
    (POPUP, "popup_choose", "Style A: list placeholder", "Choose residence"),
    (POPUP, "popup_unit_error", "Message when no residence is chosen", "Choose the residence you’re interested in."),
    (POPUP, "popup_submit", "Send button", "Send me the details"),
    (POPUP, "popup_note", "Consent note", "By submitting, you agree that M3M India may call, WhatsApp or email you about this project."),
]

LISTS = {
    "nav": ("Header menu", "Title: the link text. Link: the section it jumps to (residences, amenities, gallery, location, faq…)."),
    "popup_units": (
        "Popup: residence choices",
        "Title: e.g. “4 BHK”. Subtitle: small line under it. Value: short code saved with the lead (e.g. 4bhk). "
        "Group: residential or commercial. Link: the project slug the lead is filed under.",
    ),
}


def nav(*links):
    return [{"title": title, "link": anchor} for anchor, title in links]


def popup_units(*units):
    return [
        {"value": value, "title": title, "subtitle": note, "group": interest, "link": slug}
        for value, title, note, interest, slug in units
    ]
