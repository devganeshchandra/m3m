"""M3M The Cullinan ad landing page (templates/projects/landing/m3m-the-cullinan-residential.html).

Facts, captions, amenities and travel times follow m3mindia.com/residential/m3m-the-cullinan and the
project banner's RERA block. Prices and sizes are not published: they are the lead hook, shared by
the sales team.
"""

from projects.landing_pages import common

SLUG = "m3m-the-cullinan-residential"
NAME = "M3M The Cullinan"
STATIC_DIR = "images/landing/cullinan/"
AVENUE = "m3m-the-cullinan-avenue"

SEO = {
    "seo_title": "M3M The Cullinan, Sector 94 Noida | 3, 4 & 5 BHK Luxury Residences",
    "seo_description": (
        "M3M The Cullinan, Sector 94 Noida Expressway: 3, 4 & 5 BHK residences with floor-to-ceiling windows, "
        "golf course and skyline views, an infinity pool and a lavish clubhouse. Get the price list and floor plans."
    ),
    "share_title": "M3M The Cullinan, Sector 94 Noida",
    "share_description": "3, 4 & 5 BHK luxury residences on Noida Expressway. Get the price list and floor plans.",
    "share_image": "hero-aerial.jpg",
}

HERO = "1. Hero"
RESIDENCES = "2. Residences"
CERT = "3. Cut your own Cullinan"
AMENITIES = "4. Amenities"
AVENUE_SECTION = "5. Commercial (The Cullinan Avenue)"
GALLERY = "6. A closer look"
LOCATION = "7. Location"
VAULT = "8. The private vault"
LEGAL = "9. Disclaimer"
EXTRAS = "10. Popup & sticky bar"
FORM = "Forms"

TEXTS = [
    (common.HEADER, "brand", "Project name in the header", "The Cullinan"),
    *common.TEXTS,
    *common.contact_texts(),
    *common.rera_texts(extra="Agent RERA: UPRERAAGT10202"),
    (HERO, "hero_kicker", "Small line above the title", "Sector 94 · Noida Expressway"),
    (HERO, "hero_title_small", "Title: small line", "M3M"),
    (HERO, "hero_title_the", "Title: first word (thin)", "The"),
    (HERO, "hero_title", "Title", "Cullinan"),
    (HERO, "hero_line", "Line under the title", "Redefining luxury living. 3, 4 & 5 BHK residences with golf course and skyline views."),
    (HERO, "hero_form_title", "Form title", "Get the price list"),
    (HERO, "hero_form_title_more", "Form title: lighter ending", "& floor plans"),
    (HERO, "hero_form_button", "Form button", "Get price list"),
    (HERO, "hero_caption", "Picture caption", "Artistic impression"),
    (RESIDENCES, "tour_kicker", "Small label", "The residences"),
    (RESIDENCES, "tour_title", "Heading", "An emblem of *grace and grandeur.*"),
    (RESIDENCES, "tour_lead", "Intro", "Expansive 3, 4 and 5 BHK homes with extended balconies, spacious rooms and panoramic windows."),
    (RESIDENCES, "tour_hint", "Line above the room tabs", "Tap a room to step inside"),
    (RESIDENCES, "config_text", "Residence cards: line", "Size, floor plan & price on request"),
    (RESIDENCES, "config_button", "Residence cards: button", "Get floor plan"),
    (RESIDENCES, "config_popup", "Residence cards: popup title ({unit} = the residence)", "Get the {unit} floor plan & price"),
    (RESIDENCES, "price_title", "Price card: title", "Launch price list"),
    (RESIDENCES, "price_text", "Price card: line", "Current prices and payment plans, shared by our team."),
    (RESIDENCES, "price_button", "Price card: button", "Unlock prices"),
    (RESIDENCES, "price_popup", "Price card: popup title", "Get the price list"),
    (CERT, "cert_kicker", "Small label", "Your Cullinan, certified"),
    (CERT, "cert_title", "Heading", "Cut your own *Cullinan.*"),
    (
        CERT,
        "cert_lead",
        "Intro",
        "Inspired by how a diamond is graded. Choose your residence, what we prepare and when we call, and your "
        "private certificate fills in as you go.",
    ),
    (CERT, "cert_step_1", "Step 1: question", "Carat · Choose your residence"),
    (CERT, "cert_step_2", "Step 2: question", "Cut · What shall we prepare for you?"),
    (CERT, "cert_step_3", "Step 3: question", "Clarity · When is a good time to talk?"),
    (CERT, "cert_step_4", "Step 4: question", "Certificate · Where shall we reach you?"),
    (CERT, "cert_next", "Button: next step", "Continue"),
    (CERT, "cert_back", "Button: back", "Back"),
    (CERT, "cert_choose_error", "Message when nothing is chosen", "Choose one to continue."),
    (
        CERT,
        "cert_privacy",
        "Privacy promise",
        "This is your private information. Only M3M’s official relationship manager for The Cullinan will see it, "
        "and they will call you personally at the time you chose. Never shared, never sold.",
    ),
    (CERT, "cert_button", "Send button", "Certify my Cullinan"),
    (CERT, "cert_doc_title", "Certificate: title", "Certificate of grading"),
    (CERT, "cert_doc_sub", "Certificate: line under the title", "M3M The Cullinan · Sector 94, Noida"),
    (CERT, "cert_owner", "Certificate: name label", "Prepared for"),
    (CERT, "cert_guest", "Certificate: name until one is typed", "Your name"),
    (CERT, "cert_carat", "Certificate: label 1", "Carat"),
    (CERT, "cert_cut", "Certificate: label 2", "Cut"),
    (CERT, "cert_clarity", "Certificate: label 3", "Clarity"),
    (CERT, "cert_blank", "Certificate: value until chosen", "To be graded"),
    (CERT, "cert_seal", "Seal after sending", "Certified"),
    (CERT, "cert_request", "Note saved with each lead", "Requested: Cut your own Cullinan"),
    (AMENITIES, "amen_kicker", "Small label", "Premier offerings"),
    (AMENITIES, "amen_title", "Heading", "Every day, *beautifully lived.*"),
    (AMENITIES, "amen_all", "Filter button: everything", "All"),
    (AMENITIES, "amen_more", "Line under the amenities", "Also: active lifestyle zones, community spaces and a recreational zone."),
    (AMENITIES, "amen_button", "Button", "Download the brochure"),
    (AMENITIES, "amen_popup", "Button: popup title", "Download the brochure"),
    (AVENUE_SECTION, "avenue_kicker", "Small label", "Commercial · M3M The Cullinan Avenue"),
    (AVENUE_SECTION, "avenue_title", "Heading", "A landmark in *luxury retail.*"),
    (AVENUE_SECTION, "avenue_lead", "Intro", "Luxury boutique retail, dining and lounges at Sector 94, Noida."),
    (AVENUE_SECTION, "avenue_button", "Main button", "Get retail details"),
    (AVENUE_SECTION, "avenue_popup", "Main button: popup title", "Get retail shop details"),
    (AVENUE_SECTION, "avenue_link", "Second button", "Retail price list"),
    (AVENUE_SECTION, "avenue_link_popup", "Second button: popup title", "Get the retail price list"),
    (GALLERY, "look_kicker", "Small label", "A closer look"),
    (GALLERY, "look_note", "Note", "All images are artistic impressions."),
    (LOCATION, "loc_kicker", "Small label", "Connectivity"),
    (LOCATION, "loc_title", "Heading", "Minutes from *everything you need.*"),
    (LOCATION, "loc_lead", "Intro", "Tap a place to see the route from The Cullinan."),
    (LOCATION, "loc_unit", "Unit after each travel time", "min"),
    (LOCATION, "loc_origin", "Where the routes start (as typed in Google Maps)", "M3M The Cullinan, Sector 94, Noida"),
    (LOCATION, "loc_live", "Map tab: live map", "Live map"),
    (LOCATION, "loc_plan", "Map tab: location plan", "Location plan"),
    (LOCATION, "loc_note", "Note", "*Drive times as Google Maps shows them from the project for the fastest route; live traffic can change them."),
    (LOCATION, "loc_button", "Button", "Book a site visit"),
    (LOCATION, "loc_popup", "Button: popup title", "Book a site visit"),
    (LOCATION, "loc_map_title", "Live map description (for screen readers)", "Google map of Sector 94, Noida"),
    (
        LOCATION,
        "loc_map_url",
        "Map link, used when the project has none (Google Maps → Share → Embed a map → the src=… link)",
        "https://www.google.com/maps?q=M3M+The+Cullinan,+Sector+94,+Noida&output=embed",
    ),
    (VAULT, "vault_kicker", "Small label", "The private vault"),
    (VAULT, "vault_title", "Heading", "Unlock what *others wait for.*"),
    (
        VAULT,
        "vault_lead",
        "Intro",
        "Four documents, kept for registered enquirers. Open one, or the whole vault, and our team sends it to you "
        "privately.",
    ),
    (VAULT, "vault_sealed", "Label on each sealed document", "Sealed"),
    (VAULT, "vault_unlock", "Button on each document", "Unlock"),
    (VAULT, "vault_all", "Main button", "Unlock the whole vault"),
    (VAULT, "vault_all_popup", "Main button: popup title", "Unlock the price list, floor plans & brochure"),
    (LEGAL, "legal_name", "Project name (bold)", "M3M The Cullinan"),
    (LEGAL, "legal_rera", "RERA line", "UP RERA {rera} · Promoter: Lavish Buildmart Pvt. Ltd. (UPRERAPRM221722) · Details at"),
    (LEGAL, "legal_link_label", "RERA link text", "up-rera.in/projects"),
    (LEGAL, "legal_link_url", "RERA link address", "https://www.up-rera.in/projects"),
    (
        LEGAL,
        "legal_text",
        "Disclaimer",
        "All the information and contents of this advertisement are only for general information and not a legal "
        "offering. Nothing contained herein constitutes a legal offer or forms part of any legally binding agreement "
        "or commitment. Please verify all details, including area and other relevant terms, independently with M3M "
        "India Private Limited before concluding any decision. All images are artistic impressions; travel times are "
        "indicative.",
    ),
    (EXTRAS, "dialog_kicker", "Popup: small line", "M3M The Cullinan · Sector 94"),
    (EXTRAS, "dialog_title", "Popup: title", "Get the price list"),
    (
        EXTRAS,
        "dialog_intro",
        "Popup: line under the title",
        "Launch prices, floor plans and offers, shared privately by M3M’s official team.",
    ),
    (EXTRAS, "dialog_place", "Popup: line on the picture", "Sector 94 · Noida Expressway"),
    (EXTRAS, "sticky_call", "Mobile bar: call button", "Call"),
    (EXTRAS, "sticky_button", "Mobile bar: button", "Get price list"),
    (EXTRAS, "sticky_popup", "Mobile bar: popup title", "Get the price list"),
    (FORM, "form_step_one", "Step 1 heading", "I’m interested in"),
    (FORM, "form_step_two", "Step 2 heading", "Where should we send it?"),
    (FORM, "form_note", "Note under the form", "By submitting, you agree that M3M India may call, WhatsApp or email you about this project."),
    (FORM, "form_commercial_project", "Project slug that receives retail (commercial) leads", AVENUE),
]

IMAGES = [
    (common.HEADER, "brand_logo", "Logo (on the dark header; PNG or WebP with transparency)", "cullinan-logo.webp",
     "M3M The Cullinan, everything imagined"),
    (common.RERA, "rera_qr", "QR code", "rera-qr.webp", "UP RERA QR code for M3M The Cullinan"),
    (HERO, "hero_image", "Main picture", "hero-aerial.jpg", ""),
    (AVENUE_SECTION, "avenue_a", "Collage: large picture", "avenue-facade.jpg", "The Cullinan Avenue retail façade at dusk, artistic impression"),
    (AVENUE_SECTION, "avenue_b", "Collage: second picture", "avenue-skylight.jpg", "A multi-level retail hub, artistic impression"),
    (AVENUE_SECTION, "avenue_c", "Collage: third picture", "avenue-cafe.jpg", "Café and dining at the Avenue, artistic impression"),
    (LOCATION, "location_map", "Location map", "location-map.jpg", "Location map of M3M The Cullinan, Sector 94, Noida"),
    (EXTRAS, "dialog_image", "Popup: picture", "living.jpg", ""),
]

LISTS = {
    **common.LISTS,
    "hero_stats": ("Hero: three figures", "Value: the bold part. Title: the line under it."),
    "ticker": ("Moving ticker", "Title only."),
    "rooms": ("Room tour", "Subtitle: the tab name. Title and Text: the caption. Image: the room."),
    "units": (
        "Form choices & residence cards",
        "Title: e.g. “3 BHK”. Subtitle: small line under it. Value: short code saved with the lead (e.g. 3bhk; "
        "use retail for a shop). Group: residential or commercial; residential choices also get a residence card.",
    ),
    "pillars": ("Why The Cullinan", "Title only."),
    "amenities": (
        "Amenities",
        "Image and Title. Group: the filter it appears under (keep items of the same group next to each other).",
    ),
    "avenue_tags": ("Commercial: tags", "Title only."),
    "slides": ("A closer look: slider", "Image and Title (the caption)."),
    "connectivity": (
        "Travel times",
        "Value: minutes. Title: the place. Subtitle: its kind, e.g. Hospital. "
        "Link: the place as typed in Google Maps, for the route.",
    ),
    "cert_cuts": ("Cut your own Cullinan: what to prepare", "Title and Subtitle (line under it)."),
    "cert_slots": (
        "Cut your own Cullinan: times",
        "Title and Subtitle (the hours). Value must be one of: morning, afternoon, evening, flexible.",
    ),
    "vault": (
        "The private vault: documents",
        "Title, Subtitle (line under it) and Image (shown blurred). Link: the popup title. "
        "Value: the residence the popup preselects (optional, e.g. 3bhk).",
    ),
}

IMPRESSION = ", artistic impression"

# Drive times Google Maps shows from the project (fastest route, weekday afternoon), so the number
# matches the route the map draws: (minutes, place, kind, map query)
CONNECTIVITY = (
    ("7", "Amity University", "Education", "Amity University, Sector 125, Noida"),
    ("31", "Max Healthcare", "Hospital", "Max Super Speciality Hospital, Patparganj"),
    ("12", "Jasola Business Park", "Business", "Jasola District Centre, New Delhi"),
    ("17", "Apollo Hospital", "Hospital", "Indraprastha Apollo Hospital, Sarita Vihar"),
    ("35", "Ansal Plaza", "Shopping", "Ansal Plaza, Khel Gaon Marg, New Delhi"),
    ("13", "Radisson Blu, Sector 18", "Hospitality", "Radisson Blu MBD Hotel, Noida"),
)

CERT_CUTS = (
    ("Price & payment plan", "Launch pricing, privately"),
    ("Floor plans & sizes", "Every layout, in full"),
    ("A private site visit", "At a time that suits you"),
    ("Investment details", "Pricing, plans and paperwork"),
)

CERT_SLOTS = (
    ("Morning", "9 AM – 12 PM", "morning"),
    ("Afternoon", "12 – 3 PM", "afternoon"),
    ("Evening", "3 – 6 PM", "evening"),
    ("Any time", "Whenever suits", "flexible"),
)

VAULT_ITEMS = (
    ("Launch price list", "Every residence, every floor", "Unlock the launch price list", "", "towers-day"),
    ("Floor plans", "3, 4 & 5 BHK, in full", "Unlock the floor plans", "", "master-suite"),
    ("Payment plan", "Milestones and offers", "Unlock the payment plan", "", "open-living"),
    ("Brochure", "The complete Cullinan story", "Unlock the brochure", "", "lobby"),
)

ITEMS = {
    "nav": common.nav(
        ("residences", "Residences"),
        ("amenities", "Amenities"),
        ("commercial", "Commercial"),
        ("gallery", "Gallery"),
        ("location", "Location"),
    ),
    "popup_units": common.popup_units(
        ("3bhk", "3 BHK", "Residence", "residential", SLUG),
        ("4bhk", "4 BHK", "Residence", "residential", SLUG),
        ("5bhk", "5 BHK", "Residence", "residential", SLUG),
        ("retail", "Retail shop", "The Cullinan Avenue", "commercial", AVENUE),
    ),
    "hero_stats": [
        {"value": "3 · 4 · 5", "title": "BHK residences"},
        {"value": "Infinity", "title": "pool & clubhouse"},
        {"value": "7 min", "title": "to Amity University*"},
    ],
    "ticker": [
        {"title": title}
        for title in (
            "Floor-to-ceiling windows",
            "Golf course & skyline views",
            "Extended balconies",
            "Infinity pool",
            "Lavish clubhouse",
            "Landscaped gardens",
        )
    ],
    "rooms": [
        {"image": f"{name}.jpg", "subtitle": tab, "title": title, "text": line, "image_alt": title + IMPRESSION}
        for name, tab, title, line in (
            ("living", "Living", "A symphony of elegance", "Floor-to-ceiling windows and skyline views."),
            ("dining", "Dining", "Dine in grandeur", "A dining room made for gatherings."),
            ("open-living", "Open plan", "Contemporary living masterpiece", "Open-concept design, luxury and comfort."),
            ("master-suite", "Master suite", "Contemporary master suite", "A private sanctuary with urban vistas."),
            ("lobby", "Lobby", "A grand arrival", "Marble, sculpted light and a warm welcome."),
        )
    ],
    "units": [
        {"value": value, "title": title, "subtitle": note, "group": group}
        for value, title, note, group in (
            ("3bhk", "3 BHK", "Residence", "residential"),
            ("4bhk", "4 BHK", "Residence", "residential"),
            ("5bhk", "5 BHK", "Residence", "residential"),
            ("retail", "Retail shop", "The Cullinan Avenue", "commercial"),
        )
    ],
    "pillars": [
        {"title": title}
        for title in ("Strategically planned", "Unmatched location", "Well connected", "Unparalleled luxury")
    ],
    "amenities": [
        {"image": f"{name}.jpg", "title": title, "group": group, "image_alt": title + IMPRESSION}
        for name, title, group in (
            ("amenity-pool", "Swimming pools", "Wellness"),
            ("amenity-spa", "Spa & wellness", "Wellness"),
            ("amenity-gym", "Fitness centre", "Active"),
            ("amenity-courts", "Sports courts", "Active"),
            ("amenity-game-lounge", "Clubhouse", "Leisure"),
            ("amenity-cinema", "Movie theatre", "Leisure"),
            ("amenity-gaming", "Game room", "Leisure"),
            ("amenity-party-lawn", "Party lawn", "Outdoors"),
            ("amenity-gardens", "Outdoor spaces", "Outdoors"),
            ("amenity-kids", "Children’s play area", "Family"),
            ("amenity-seniors", "Senior citizens’ corner", "Family"),
            ("amenity-community", "Community centre", "Family"),
        )
    ],
    "avenue_tags": [{"title": title} for title in ("Luxury boutiques", "Fine dining", "Lounges", "Multi-level hub")],
    "slides": [
        {"image": f"{name}.jpg", "title": caption, "image_alt": caption + IMPRESSION}
        for name, caption in (
            ("hero-aerial", "The Cullinan by night"),
            ("living", "A symphony of elegance"),
            ("towers-green", "Towers among the greens"),
            ("master-suite", "The master suite"),
            ("towers-day", "Sector 94, Noida Expressway"),
            ("billiards-lounge", "The billiards lounge"),
        )
    ],
    "connectivity": [
        {"value": minutes, "title": place, "subtitle": kind, "link": query}
        for minutes, place, kind, query in CONNECTIVITY
    ],
    "cert_cuts": [{"title": title, "subtitle": line} for title, line in CERT_CUTS],
    "cert_slots": [{"title": title, "subtitle": hours, "value": value} for title, hours, value in CERT_SLOTS],
    "vault": [
        {"title": title, "subtitle": line, "link": popup, "value": preset, "image": f"{name}.jpg"}
        for title, line, popup, preset, name in VAULT_ITEMS
    ],
}
