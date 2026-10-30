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
PLANS = "3. Floor plans"
PRICE = "4. Price band"
COMMERCIAL = "5. Commercial"
AMENITIES = "6. Amenities"
GALLERY = "7. A closer look"
LOCATION = "8. Location"
PRIVATE = "9. Private line"
FINAL = "10. Private site visit"
LEGAL = "11. Disclaimer"
EXTRAS = "12. Popup & sticky bar"
FORM = "Forms"

TEXTS = [
    (common.HEADER, "brand", "Project name in the header", "Jacob & Co. Residences"),
    *common.TEXTS,
    *common.contact_texts(whatsapp="+917399673996"),
    *common.rera_texts(),
    (HERO, "hero_eyebrow", "Small line above the title", "Now launched · Sector 97, Noida Expressway"),
    (HERO, "hero_title_small", "Title: small part", "M3M"),
    (HERO, "hero_title", "Title", "Jacob & Co."),
    (HERO, "hero_title_em", "Title: italic line", "Residences"),
    (HERO, "hero_tagline", "Line under the title", "Inspired by the impossible. The artistry of Jacob & Co., in architectural form."),
    (HERO, "hero_button", "First button", "Unlock the brochure"),
    (HERO, "hero_popup", "First button: popup title", "Unlock the brochure"),
    (HERO, "hero_button_2", "Second button", "Get the price list"),
    (HERO, "hero_popup_2", "Second button: popup title", "Get the price list"),
    (HERO, "card_eyebrow", "Form card: small label", "Limited launch inventory"),
    (HERO, "card_title", "Form card: title", "Get the brochure & price list"),
    (HERO, "card_intro", "Form card: line under the title", "Launch prices, payment plans and floor plans, sent to you privately."),
    (HERO, "card_button", "Form card: button", "Unlock now"),
    (RESIDENCES, "res_eyebrow", "Small label", "The residences · 3, 4 & 5 BHK"),
    (RESIDENCES, "res_title", "Heading", "Where artistry *becomes an address.*"),
    (
        RESIDENCES,
        "res_lead",
        "Intro",
        "Three towers of branded 3, 4 and 5 BHK residences on Noida Expressway, where the artistry of Jacob & Co. "
        "meets the craftsmanship of M3M. Rooms flow into private balconies, light moves freely through every space, "
        "and the city becomes a view rather than a noise.",
    ),
    (RESIDENCES, "res_quote", "Quote beside the pictures", "Calm over chaos. Views over walls. Homes where your legacy resides."),
    (RESIDENCES, "res_badge", "Badge on the pictures", "Limited launch inventory"),
    (RESIDENCES, "res_button", "Button", "Explore the floor plans"),
    (PLANS, "plans_eyebrow", "Small label", "Configurations"),
    (PLANS, "plans_title", "Heading", "Floor plans, *privately shared.*"),
    (
        PLANS,
        "plans_lead",
        "Intro",
        "Every layout is reserved for registered enquirers. Tap a plan to unlock the full drawing, the size and the "
        "launch price.",
    ),
    (PLANS, "plans_unlock", "Text on the locked plan", "Unlock plan"),
    (PLANS, "plans_type_label", "Label: type", "Type"),
    (PLANS, "plans_area_label", "Label: size", "Size"),
    (PLANS, "plans_area_locked", "Size shown when none is typed in the list", "On request"),
    (PLANS, "plans_button", "Button on each plan", "Request private pricing"),
    (PLANS, "plans_note", "Note", "Plans are shown blurred until requested. Drawings are indicative."),
    (PRICE, "price_eyebrow", "Small label", "Launch price list"),
    (PRICE, "price_title", "Heading", "Prices are shared with *registered enquirers.*"),
    (PRICE, "price_button", "Button", "Unlock the price list"),
    (PRICE, "price_popup", "Button: popup title", "Get the price list"),
    (COMMERCIAL, "com_caption", "Image caption", "Artistic impression"),
    (COMMERCIAL, "com_eyebrow", "Small label", "Commercial · M3M Jewel Crest Avenue"),
    (COMMERCIAL, "com_title", "Heading", "Retail at the foot *of an icon.*"),
    (COMMERCIAL, "com_lead", "Text", "High-street retail, fine dining and cafés, integrated with the residences."),
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
    (LOCATION, "loc_eyebrow", "Small label", "Location advantage · Sector 97, Noida"),
    (LOCATION, "loc_title", "Heading", "Everything, *minutes away.*"),
    (
        LOCATION,
        "loc_lead",
        "Intro",
        "The mall, the metro, the campus and the expressway are a short drive from home. Tap a place to see the route.",
    ),
    (LOCATION, "loc_origin", "Where the routes start (as typed in Google Maps)", "M3M Jacob & Co. Residences, Sector 97, Noida"),
    (LOCATION, "loc_minutes", "Word after the number", "min"),
    (LOCATION, "loc_away", "Line under each place", "away by car"),
    (LOCATION, "loc_value_title", "Box: heading", "Connected to *what matters.*"),
    (
        LOCATION,
        "loc_value_text",
        "Box: text",
        "Noida Expressway, the metro and Central Noida, a short drive from home.",
    ),
    (LOCATION, "loc_corridors", "Label before the connected roads", "Connected to"),
    (LOCATION, "loc_note", "Note under the times", "Drive times as Google Maps shows them for the fastest route; live traffic can change them."),
    (LOCATION, "loc_button", "Button", "Get location map & travel times"),
    (LOCATION, "loc_popup", "Button: popup title", "Get the location map & travel times"),
    (LOCATION, "loc_map_title", "Map description (for screen readers)", "Map of Sector 97, Noida"),
    (
        LOCATION,
        "loc_map_url",
        "Map link, used when the project has none (Google Maps → Share → Embed a map → the src=… link)",
        "https://www.google.com/maps?q=Sector+97,+Noida,+Uttar+Pradesh&output=embed",
    ),
    (PRIVATE, "pl_eyebrow", "Small label", "The private line"),
    (PRIVATE, "pl_title", "Heading", "Three taps. *One private call.*"),
    (
        PRIVATE,
        "pl_lead",
        "Intro",
        "Choose what you would like to know and when to talk. Your letter writes itself, and your relationship "
        "manager calls you at that time.",
    ),
    (PRIVATE, "pl_step_1", "Step 1: question", "What shall we prepare for you?"),
    (PRIVATE, "pl_step_2", "Step 2: question", "When is a good time to talk?"),
    (PRIVATE, "pl_step_3", "Step 3: question", "Where shall we reach you?"),
    (PRIVATE, "pl_next", "Button: next step", "Continue"),
    (PRIVATE, "pl_back", "Button: back", "Back"),
    (PRIVATE, "pl_choose_error", "Message when nothing is chosen", "Choose one to continue."),
    (
        PRIVATE,
        "pl_privacy",
        "Privacy promise",
        "This is your private information. Only M3M’s official relationship manager for this project will see it, "
        "and they will call you personally at the time you chose. Never shared, never sold.",
    ),
    (PRIVATE, "pl_button", "Send button", "Seal my private call"),
    (PRIVATE, "pl_letter_to", "Letter: greeting", "Dear"),
    (PRIVATE, "pl_letter_guest", "Letter: name until one is typed", "Guest"),
    (PRIVATE, "pl_letter_prepare", "Letter: line before the choice", "We are preparing"),
    (PRIVATE, "pl_letter_call", "Letter: line before the time", "Your relationship manager will call you"),
    (PRIVATE, "pl_letter_blank", "Letter: gap until a choice is made", "…"),
    (PRIVATE, "pl_letter_sign", "Letter: signature", "M3M Jacob & Co. Residences"),
    (PRIVATE, "pl_sealed", "Stamp after sending", "Sealed"),
    (PRIVATE, "pl_request", "Note saved with each lead", "Requested: Private line call"),
    (FINAL, "final_eyebrow", "Small label", "By invitation · Private site visit"),
    (FINAL, "final_title", "Heading", "See it before *the world does.*"),
    (
        FINAL,
        "visit_lead",
        "Intro",
        "Reserve a private viewing of the site, hosted by your relationship manager. Choose a day and a time, and "
        "we will confirm it with you by phone.",
    ),
    (FINAL, "visit_admit", "Pass: small line", "Admit one"),
    (FINAL, "visit_pass_label", "Pass: title", "Private viewing pass"),
    (FINAL, "visit_day", "Pass: day question", "Choose a day"),
    (FINAL, "visit_time", "Pass: time question", "Choose a time"),
    (FINAL, "visit_day_error", "Message when no day is chosen", "Choose a day for your visit."),
    (FINAL, "visit_time_error", "Message when no time is chosen", "Choose a time for your visit."),
    (FINAL, "visit_chauffeur", "Pass: chauffeur switch", "Chauffeur pickup"),
    (FINAL, "visit_chauffeur_note", "Pass: line under the switch", "From your home or office, on request"),
    (FINAL, "final_button", "Pass: send button", "Reserve my viewing"),
    (FINAL, "visit_confirmed", "Stamp after sending", "Reserved"),
    (FINAL, "visit_request", "Note saved with each lead", "Requested: Private site visit"),
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
    (common.HEADER, "brand_logo", "Logo (white on transparent, PNG or WebP)", "jacob-logo.webp",
     "M3M Jacob & Co. Residences, Noida"),
    (common.RERA, "rera_qr", "QR code", "rera-qr.webp", "UP RERA QR code for M3M Jacob & Co. Residences"),
    (RESIDENCES, "res_main", "Large picture (first of the slideshow)", "residence-balcony.jpg",
     "Living room opening to a private balcony over green views, artistic impression"),
    (RESIDENCES, "res_side", "Small picture", "balcony-golf-view.jpg",
     "Private balcony overlooking a golf course, artistic impression"),
    (RESIDENCES, "res_tall", "Tall picture", "res-golf-view.jpg",
     "Greens and the Noida skyline seen from the residences, artistic impression"),
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
    "res_photos": ("Residences: more pictures", "Image and Title: its caption. They follow the large picture in its slideshow."),
    "res_pillars": ("Residences: what sets them apart", "Title and Text."),
    "configs": (
        "Floor plans",
        "Title: the number, e.g. “3”. Subtitle: small text after it, e.g. “BHK”. Text: line under it. "
        "Group: the size, e.g. “2,500 sq ft” (empty shows “On request”). Image: the floor plan, shown blurred. "
        "Value: the residence code the popup preselects (e.g. 3bhk). Link: the popup title.",
    ),
    "commercial": ("Commercial: what's included", "Title only."),
    "amenities": (
        "Amenity tiles",
        "Image, Title and Subtitle (small line above the title). Group: type “wide” for a double-width tile.",
    ),
    "gallery": ("A closer look (gallery)", "Image and Title: its caption."),
    "places": ("Location: connected roads", "Title: the road or area. Subtitle: not shown."),
    "drive_times": (
        "Location: minutes away",
        "Title: the place. Value: minutes by car (a number). Subtitle: its kind, e.g. Metro. "
        "Link: the place as typed in Google Maps, for the route (empty shows a close map of the project's area).",
    ),
    "pl_choices": ("Private line: step 1 cards", "Title, Subtitle (line under it) and Text: how the letter names it."),
    "pl_slots": (
        "Private line: times",
        "Title and Subtitle (the hours); Text: how the letter says it, e.g. “in the evening”. "
        "Value must be one of: morning, afternoon, evening, flexible.",
    ),
    "perks": ("Private site visit: what the visit includes", "Title only."),
}

IMPRESSION = ", artistic impression"

RES_PHOTOS = (
    ("res-interior", "Living rooms that open to the sky"),
    ("res-terrace", "A private terrace for every residence"),
    ("crown-deck", "The sky deck in the crown"),
    ("lagoon-cabana", "Cabanas on the lagoon"),
)

RES_PILLARS = (
    ("Calm over chaos", "Homes set above landscaped greens and water, away from the rush of the city."),
    ("Views over walls", "Generous glazing and private balconies frame the skyline and the greens beyond."),
    ("Service as standard", "Concierge and butler services make hospitality part of everyday life."),
    ("A name that endures", "The artistry of Jacob & Co., in an address made to be handed down."),
)

DRIVE_TIMES = (
    ("Mall of Noida", "4", "Shopping", "Mall of Noida, Noida"),
    ("Noida Expressway", "4", "Expressway", ""),
    ("Amity University", "9", "Education", "Amity University, Sector 125, Noida"),
    ("Botanical Garden Metro Station", "12", "Metro", "Botanical Garden Metro Station, Noida"),
    ("Radisson Blu MBD Hotel", "19", "Hospitality", "Radisson Blu MBD Hotel, Noida"),
)

PL_CHOICES = (
    ("Price & payment plan", "Launch pricing, privately", "the launch price and payment plan"),
    ("Floor plans & sizes", "Every layout, in full", "the floor plans and sizes"),
    ("A private site visit", "Chauffeured, at your time", "a private site visit"),
    ("Investment details", "Pricing, plans and paperwork", "the investment details"),
)

PERKS = (
    "Chauffeur pickup from your home or office",
    "A private walkthrough with your relationship manager",
    "The launch price list and floor plans, in hand",
)

PL_SLOTS = (
    ("Morning", "9 AM – 12 PM", "morning", "in the morning"),
    ("Afternoon", "12 – 3 PM", "afternoon", "in the afternoon"),
    ("Evening", "3 – 6 PM", "evening", "in the evening"),
    ("Any time", "Whenever suits", "flexible", "whenever suits you"),
)

ITEMS = {
    "nav": common.nav(
        ("residences", "Residences"), ("floor-plans", "Floor plans"), ("commercial", "Commercial"), ("amenities", "Amenities"),
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
            ("Promoter", "Mayfairsky Estates Pvt Ltd"),
            ("Residences", "3, 4 & 5 BHK"),
            ("Towers", "1, 2 & 3"),
            ("Location", "Sector 97, Noida"),
            ("UP RERA", "{rera}"),
        )
    ],
    "res_photos": [
        {"image": f"{name}.jpg", "title": caption, "image_alt": caption + IMPRESSION}
        for name, caption in RES_PHOTOS
    ],
    "res_pillars": [{"title": title, "text": text} for title, text in RES_PILLARS],
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
    "drive_times": [
        {"title": title, "value": minutes, "subtitle": kind, "link": query}
        for title, minutes, kind, query in DRIVE_TIMES
    ],
    "pl_choices": [{"title": title, "subtitle": line, "text": letter} for title, line, letter in PL_CHOICES],
    "pl_slots": [
        {"title": title, "subtitle": hours, "value": value, "text": letter} for title, hours, value, letter in PL_SLOTS
    ],
    "perks": [
        {"title": title}
        for title in PERKS
    ],
}
