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
AMENITIES = "3. Amenities"
AVENUE_SECTION = "4. Commercial (The Cullinan Avenue)"
GALLERY = "5. A closer look"
LOCATION = "6. Location"
FINAL = "7. Final form"
LEGAL = "8. Disclaimer"
EXTRAS = "9. Popup & sticky bar"
FORM = "Forms"

TEXTS = [
    (common.HEADER, "brand", "Project name in the header", "The Cullinan"),
    *common.TEXTS,
    (HERO, "hero_kicker", "Small line above the title", "Sector 94 · Noida Expressway"),
    (HERO, "hero_title_small", "Title: small line", "M3M"),
    (HERO, "hero_title_the", "Title: first word (thin)", "The"),
    (HERO, "hero_title", "Title", "Cullinan"),
    (HERO, "hero_line", "Line under the title", "Redefining luxury living. 3, 4 & 5 BHK residences with golf course and skyline views."),
    (HERO, "hero_form_title", "Form title", "Get the price list"),
    (HERO, "hero_form_title_more", "Form title: lighter ending", "& floor plans"),
    (HERO, "hero_form_button", "Form button", "Get price list"),
    (HERO, "hero_caption_rera", "Picture caption: RERA", "UP RERA {rera}"),
    (HERO, "hero_caption", "Picture caption", "Artistic impression"),
    (RESIDENCES, "tour_kicker", "Small label", "The residences"),
    (RESIDENCES, "tour_title", "Heading", "An emblem of *grace and grandeur.*"),
    (RESIDENCES, "tour_lead", "Intro", "Expansive 3, 4 and 5 BHK homes with extended balconies, spacious rooms and panoramic windows."),
    (RESIDENCES, "config_text", "Residence cards: line", "Size, floor plan & price on request"),
    (RESIDENCES, "config_button", "Residence cards: button", "Get floor plan"),
    (RESIDENCES, "config_popup", "Residence cards: popup title ({unit} = the residence)", "Get the {unit} floor plan & price"),
    (RESIDENCES, "price_title", "Price card: title", "Launch price list"),
    (RESIDENCES, "price_text", "Price card: line", "Current prices and payment plans, shared by our team."),
    (RESIDENCES, "price_button", "Price card: button", "Unlock prices"),
    (RESIDENCES, "price_popup", "Price card: popup title", "Get the price list"),
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
    (LOCATION, "loc_unit", "Unit after each travel time", "min"),
    (LOCATION, "loc_note", "Note", "*Travel times as stated by M3M India; they vary with route and traffic."),
    (LOCATION, "loc_button", "Button", "Book a site visit"),
    (LOCATION, "loc_popup", "Button: popup title", "Book a site visit"),
    (LOCATION, "loc_map_title", "Live map description (for screen readers)", "Google map of Sector 94, Noida"),
    (
        LOCATION,
        "loc_map_url",
        "Map link, used when the project has none (Google Maps → Share → Embed a map → the src=… link)",
        "https://www.google.com/maps?q=M3M+The+Cullinan,+Sector+94,+Noida&output=embed",
    ),
    (FINAL, "final_kicker", "Small label", "Private preview"),
    (FINAL, "final_title", "Heading", "Your Cullinan *awaits.*"),
    (FINAL, "final_button", "Form button", "Request a callback"),
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
    (EXTRAS, "sticky_call", "Mobile bar: call button", "Call"),
    (EXTRAS, "sticky_button", "Mobile bar: button", "Get price list"),
    (EXTRAS, "sticky_popup", "Mobile bar: popup title", "Get the price list"),
    (FORM, "form_step_one", "Step 1 heading", "I’m interested in"),
    (FORM, "form_step_two", "Step 2 heading", "Where should we send it?"),
    (FORM, "form_note", "Note under the form", "By submitting, you agree that M3M India may call, WhatsApp or email you about this project."),
    (FORM, "form_commercial_project", "Project slug that receives retail (commercial) leads", AVENUE),
]

IMAGES = [
    (HERO, "hero_image", "Main picture", "hero-aerial.jpg", ""),
    (AVENUE_SECTION, "avenue_a", "Collage: large picture", "avenue-facade.jpg", "The Cullinan Avenue retail façade at dusk, artistic impression"),
    (AVENUE_SECTION, "avenue_b", "Collage: second picture", "avenue-skylight.jpg", "Multi-level atrium under a skylight, artistic impression"),
    (AVENUE_SECTION, "avenue_c", "Collage: third picture", "avenue-cafe.jpg", "Café and dining at the Avenue, artistic impression"),
    (LOCATION, "location_map", "Location map", "location-map.jpg", "Location map of M3M The Cullinan, Sector 94, Noida"),
    (FINAL, "final_image", "Background picture", "towers-day.jpg", ""),
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
    "connectivity": ("Travel times", "Value: minutes. Title: the place."),
    "perks": ("Final form: what you get", "Title only."),
}

IMPRESSION = ", artistic impression"

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
        {"value": "2 min", "title": "to Amity University*"},
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
    "avenue_tags": [{"title": title} for title in ("Luxury boutiques", "Fine dining", "Lounges", "Multi-level atrium")],
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
    # (minutes, place) as stated on the official project page
    "connectivity": [
        {"value": minutes, "title": place}
        for minutes, place in (
            ("2", "Amity University"),
            ("5", "Max Healthcare"),
            ("5", "Jasola Business Park"),
            ("10", "Apollo Hospital"),
            ("12", "Ansal Plaza"),
            ("12", "Radisson Blu, Sector 18"),
        )
    ],
    "perks": [
        {"title": title}
        for title in (
            "Launch price list & payment plans",
            "Floor plans for 3, 4 & 5 BHK",
            "A site visit at a time that suits you",
        )
    ],
}
