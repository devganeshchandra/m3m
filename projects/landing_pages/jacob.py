"""M3M Jacob & Co. Residences ad landing page (templates/projects/landing/m3m-jacob-co-residences.html).

Facts follow m3mindia.com/residential/m3m-jacob-co and the project record in the admin. Prices and
sizes are not published: they are the lead hook, shared by the sales team. Images are official M3M
artistic impressions, enhanced.
"""

from projects.landing_pages import common

SLUG = "m3m-jacob-co-residences"
NAME = "M3M Jacob & Co. Residences"
STATIC_DIR = "images/landing/jacob-co/"

SEO = {
    "seo_title": "M3M Jacob & Co. Residences, Sector 97 Noida | 3, 4 & 5 BHK Branded Residences",
    "seo_description": (
        "M3M Jacob & Co. Residences on Noida Expressway, Sector 97: branded 3, 4 & 5 BHK residences with sky "
        "lounges, a temperature-controlled pool and concierge services. Unlock the brochure and price list."
    ),
    "share_title": "M3M Jacob & Co. Residences, Sector 97 Noida",
    "share_description": "Branded 3, 4 & 5 BHK residences on Noida Expressway. Unlock the brochure and price list.",
    "share_image": "crown-lounge.jpg",
}

HERO = "1. Hero"
RESIDENCES = "2. Residences"
PRICE = "3. Price band"
COMMERCIAL = "4. Commercial"
AMENITIES = "5. Amenities"
GALLERY = "6. A closer look"
LOCATION = "7. Location"
FINAL = "8. Final form"
LEGAL = "9. Disclaimer"
EXTRAS = "10. Popup & sticky bar"
FORM = "Forms"

TEXTS = [
    (common.HEADER, "brand", "Project name in the header", "Jacob & Co. Residences"),
    *common.TEXTS,
    (HERO, "hero_eyebrow", "Small line above the title", "Now launched · Sector 97, Noida Expressway"),
    (HERO, "hero_title_small", "Title: small part", "M3M"),
    (HERO, "hero_title", "Title", "Jacob & Co."),
    (HERO, "hero_title_em", "Title: italic line", "Residences"),
    (HERO, "hero_tagline", "Line under the title", "Inspired by the impossible. The artistry of Jacob & Co., in architectural form."),
    (HERO, "hero_button", "First button", "Unlock the brochure"),
    (HERO, "hero_popup", "First button: popup title", "Unlock the brochure"),
    (HERO, "hero_button_2", "Second button", "Get the price list"),
    (HERO, "hero_popup_2", "Second button: popup title", "Get the price list"),
    (HERO, "hero_rera", "RERA line", "UP RERA: {rera}"),
    (HERO, "card_eyebrow", "Form card: small label", "Limited launch inventory"),
    (HERO, "card_title", "Form card: title", "Get the brochure & price list"),
    (HERO, "card_button", "Form card: button", "Unlock now"),
    (RESIDENCES, "res_eyebrow", "Small label", "The residences"),
    (RESIDENCES, "res_title", "Heading", "An icon *in the making.*"),
    (RESIDENCES, "res_lead", "Intro", "Calm over chaos. Views over walls. Homes where your legacy resides."),
    (RESIDENCES, "res_button", "Button on each residence", "Size & price"),
    (PRICE, "price_eyebrow", "Small label", "Launch price list"),
    (PRICE, "price_title", "Heading", "Prices are shared with *registered enquirers.*"),
    (PRICE, "price_button", "Button", "Unlock the price list"),
    (PRICE, "price_popup", "Button: popup title", "Get the price list"),
    (COMMERCIAL, "com_caption", "Image caption", "Artistic impression"),
    (COMMERCIAL, "com_eyebrow", "Small label", "Commercial · M3M Jacob Jewel Crest"),
    (COMMERCIAL, "com_title", "Heading", "Retail at the foot *of an icon.*"),
    (COMMERCIAL, "com_lead", "Text", "Shops and F&B spaces within the Jacob & Co. project on Noida Expressway."),
    (COMMERCIAL, "com_button", "First button", "Get commercial details"),
    (COMMERCIAL, "com_popup", "First button: popup title", "Get commercial unit details"),
    (COMMERCIAL, "com_button_2", "Second button", "Commercial price list"),
    (COMMERCIAL, "com_popup_2", "Second button: popup title", "Get the commercial price list"),
    (AMENITIES, "amen_eyebrow", "Small label", "Amenities"),
    (AMENITIES, "amen_title", "Heading", "A lifestyle *beyond imagination.*"),
    (AMENITIES, "amen_cta_text", "Text under the tiles", "The complete amenity list is in the brochure."),
    (AMENITIES, "amen_cta_button", "Button", "Unlock the brochure"),
    (AMENITIES, "amen_cta_popup", "Button: popup title", "Unlock the brochure"),
    (GALLERY, "gal_eyebrow", "Small label", "A closer look"),
    (GALLERY, "gal_title", "Heading", "Glimpses of a *masterpiece.*"),
    (GALLERY, "gal_note", "Note", "All images are artistic impressions."),
    (LOCATION, "loc_eyebrow", "Small label", "Location"),
    (LOCATION, "loc_title", "Heading", "Sector 97, *Noida Expressway.*"),
    (LOCATION, "loc_button", "Button", "Get location map & travel times"),
    (LOCATION, "loc_popup", "Button: popup title", "Get the location map & travel times"),
    (LOCATION, "loc_map_title", "Map description (for screen readers)", "Map of Sector 97, Noida"),
    (
        LOCATION,
        "loc_map_url",
        "Map link, used when the project has none (Google Maps → Share → Embed a map → the src=… link)",
        "https://www.google.com/maps?q=Sector+97,+Noida,+Uttar+Pradesh&output=embed",
    ),
    (FINAL, "final_eyebrow", "Small label", "Private preview"),
    (FINAL, "final_title", "Heading", "Own an icon *in the making.*"),
    (FINAL, "final_button", "Form button", "Request a callback"),
    (LEGAL, "legal_label", "RERA label (bold)", "UP RERA:"),
    (LEGAL, "legal_rera", "RERA number", "{rera}"),
    (LEGAL, "legal_link_label", "RERA link text", "up-rera.in"),
    (LEGAL, "legal_link_url", "RERA link address", "https://www.up-rera.in/"),
    (
        LEGAL,
        "legal_text",
        "Disclaimer",
        "The Project is registered under the name “M3M J&C” with UPRERA and the Towers 1, 2 & 3 in the Project are "
        "named as ‘M3M Jacob & Co Residences’. The “M3M Jacob & Co Residences” are not owned, developed or sold by "
        "Jacob & Co Ventures LLC or any of its affiliates and use the ‘Jacob & Co’ name and mark under license from "
        "Jacob & Co Ventures LLC, which license is subject to the terms of the License Agreement. Mayfairsky Estates "
        "Pvt Ltd. is the promoter and developer executing the Project. All images are artistic impressions. The "
        "information here is for general information only and does not constitute a legal offer or invitation to "
        "offer.",
    ),
    (EXTRAS, "popup_name", "Popup: project name on the picture", "M3M Jacob & Co. Residences"),
    (EXTRAS, "popup_place", "Popup: place on the picture", "Sector 97 · Noida"),
    (EXTRAS, "popup_eyebrow", "Popup: small label", "Instant access"),
    (EXTRAS, "popup_title", "Popup: title when opened on its own", "Unlock the brochure"),
    (EXTRAS, "sticky_call", "Mobile bar: call button", "Call"),
    (EXTRAS, "sticky_button", "Mobile bar: button", "Unlock brochure"),
    (EXTRAS, "sticky_popup", "Mobile bar: popup title", "Unlock the brochure"),
    (FORM, "commercial_slug", "Project that receives commercial leads (its slug)", "m3m-jacob-jewel-crest-noida"),
    (FORM, "form_request", "Note saved with each lead", "Requested: Project details"),
    (FORM, "form_name_label", "Name: label", "Full name"),
    (FORM, "form_name_placeholder", "Name: hint", "Your full name"),
    (FORM, "form_phone_label", "Mobile: label", "Mobile number"),
    (FORM, "form_phone_placeholder", "Mobile: hint", "10-digit mobile number"),
    (FORM, "form_email_label", "Email: label", "Email"),
    (FORM, "form_email_placeholder", "Email: hint", "name@email.com"),
    (FORM, "form_looking_for", "Project type: label", "Looking for"),
    (FORM, "form_choose", "Project type: placeholder", "Choose project type"),
    (FORM, "form_residential", "Project type: residential choice", "Residential · 3, 4 & 5 BHK"),
    (FORM, "form_commercial", "Project type: commercial choice", "Commercial · Retail & F&B"),
    (
        FORM,
        "form_note",
        "Note under the form",
        "By submitting, you agree that M3M India may call, WhatsApp or email you about this project. No spam.",
    ),
]

IMAGES = [
    (RESIDENCES, "res_main", "Large picture", "residence-balcony.jpg",
     "Living room opening to a private balcony over green views, artistic impression"),
    (RESIDENCES, "res_side", "Small picture", "balcony-golf-view.jpg",
     "Private balcony overlooking a golf course, artistic impression"),
    (PRICE, "price_bg", "Background", "aerial-pools.jpg", ""),
    (COMMERCIAL, "com_image", "Picture", "towers-podium.jpg",
     "Residential towers rising above a lit retail podium, artistic impression"),
    (FINAL, "final_bg", "Background", "crown-lounge.jpg", ""),
    (EXTRAS, "popup_image", "Popup: picture", "residence-balcony.jpg", ""),
]

LISTS = {
    **common.LISTS,
    "slides": ("Hero slideshow", "Image. Title: a name for the admin only (not shown)."),
    "hero_chips": ("Hero: short points", "Title only."),
    "trust": ("At a glance strip", "Title: the label. Text: the value ({rera} = the RERA number)."),
    "configs": (
        "Residence types",
        "Title: the number, e.g. “3”. Subtitle: small text after it, e.g. “BHK”. Text: line under it. "
        "Value: the residence code the popup preselects (e.g. 3bhk). Link: the popup title.",
    ),
    "commercial": ("Commercial: what's included", "Title only."),
    "amenities": (
        "Amenity tiles",
        "Image, Title and Subtitle (small line above the title). Group: type “wide” for a double-width tile.",
    ),
    "gallery": ("A closer look (gallery)", "Image and Title: its caption."),
    "places": ("Location: places nearby", "Title: the place. Subtitle: small line under it."),
    "perks": ("Final form: what you get", "Title only."),
}

IMPRESSION = ", artistic impression"

ITEMS = {
    "nav": common.nav(
        ("residences", "Residences"), ("commercial", "Commercial"), ("amenities", "Amenities"),
        ("gallery", "Gallery"), ("location", "Location"),
    ),
    "popup_units": common.popup_units(
        ("3bhk", "3 BHK", "Residence", "residential", SLUG),
        ("4bhk", "4 BHK", "Residence", "residential", SLUG),
        ("5bhk", "5 BHK", "Residence", "residential", SLUG),
        ("retail", "Retail shop", "Jewel Crest", "commercial", "m3m-jacob-jewel-crest-noida"),
    ),
    "slides": [
        {"title": title, "image": f"{name}.jpg"}
        for name, title in (("crown-lounge", "Sky lounge"), ("towers-podium", "Towers & podium"), ("lagoon-pool", "Lagoon pool"))
    ],
    "hero_chips": [
        {"title": title} for title in ("3, 4 & 5 BHK", "Branded residences", "Sky lounges", "Concierge & butler")
    ],
    "trust": [
        {"title": label, "text": value}
        for label, value in (
            ("Developer", "M3M India"),
            ("Residences", "3, 4 & 5 BHK"),
            ("Towers", "1, 2 & 3"),
            ("Location", "Sector 97, Noida"),
            ("UP RERA", "{rera}"),
        )
    ],
    "configs": [
        {
            "title": number,
            "subtitle": "BHK",
            "text": "Branded residence",
            "value": f"{number}bhk",
            "link": f"Get the {number} BHK floor plan & price",
        }
        for number in ("3", "4", "5")
    ],
    "commercial": [{"title": title} for title in ("Retail shops", "Food court", "Restaurants")],
    "amenities": [
        {"image": f"{name}.jpg", "subtitle": line, "title": title, "group": group, "image_alt": alt}
        for name, line, title, group, alt in (
            ("crown-lounge", "A crown above the clouds", "Sky lounges & temperature-controlled pool", "wide",
             "Sky lounge and pool in the crown of the tower above the clouds, artistic impression"),
            ("lagoon-pool", "Breathe. Unwind. Belong.", "Wellness & spa retreats", "",
             "Lagoon pool among palms and landscaped gardens, artistic impression"),
            ("tower-night", "Evenings, elevated", "Private entertainment hubs", "",
             "Illuminated tower at night, artistic impression"),
            ("towers-blue-hour", "Hospitality at home", "Concierge & butler services", "wide",
             "Towers and pool deck at blue hour, artistic impression"),
        )
    ],
    "gallery": [
        {"image": f"{name}.jpg", "title": caption, "image_alt": caption + IMPRESSION}
        for name, caption in (
            ("crown-lounge", "A crown above the clouds"),
            ("balcony-golf-view", "Life, framed by nature"),
            ("lagoon-pool", "A luxurious oasis"),
            ("residence-balcony", "Views over walls"),
            ("towers-podium", "The towers and podium"),
            ("aerial-pools", "Pools and gardens from above"),
            ("tower-night", "The tower by night"),
            ("towers-blue-hour", "Blue hour"),
        )
    ],
    "places": [
        {"title": place, "subtitle": line}
        for place, line in (
            ("Noida–Greater Noida Expressway", "The address"),
            ("Central Noida & Sector 18", "Business & retail"),
            ("South Delhi", "Via Kalindi Kunj & DND"),
            ("Greater Noida", "Along the expressway"),
            ("Noida International Airport, Jewar", "Via Yamuna Expressway"),
        )
    ],
    "perks": [
        {"title": title}
        for title in ("Brochure & launch price list", "Floor plans for 3, 4 & 5 BHK", "Site visit at a time that suits you")
    ],
}
