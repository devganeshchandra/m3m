"""M3M Trump Tower Noida ad landing page (templates/projects/landing/m3m-trump-tower-noida.html).

No official project page exists yet: only the arrival render is official. Every other image is a
representative luxury interior, labelled on the page. Prices, unit counts and land area are deliberately
absent (listing sites disagree); they are offered in the price list instead. The size range is the one
M3M's sales team gives for the 4 & 5 BHK residences.
"""

from projects.landing_pages import common

SLUG = "m3m-trump-tower-noida"
NAME = "M3M Trump Tower Noida"
STATIC_DIR = "images/landing/trump/"

SEO = {
    "seo_title": "M3M Trump Tower Noida, Sector 94 | 4 & 5 BHK Branded Residences",
    "seo_description": (
        "M3M Trump Tower Noida, Sector 94 on Noida Expressway: 4 & 5 BHK branded residences. "
        "Get the price list, floor plans and payment plan."
    ),
    "share_title": "M3M Trump Tower Noida · 4 & 5 BHK Residences",
    "share_description": "Branded 4 & 5 BHK residences in Sector 94, Noida. Get the price list and floor plans.",
    "share_image": "arrival.jpg",
}

HERO = "1. Hero"
BAND = "2. At a glance"
STEPS = "3. Three steps"
LIFT = "4. The private lift"
RESIDENCES = "5. Residences"
COLLECTION = "6. The private collection"
LIFE = "7. Lifestyle"
LOCATION = "8. Location"
FAQ = "9. Questions"
FINAL = "10. Final form"
LEGAL = "11. Disclaimer"
EXTRAS = "12. Pop-ups & sticky buttons"
FORM = "Forms"

TEXTS = [
    (common.HEADER, "brand", "Project name in the header", "Trump Tower Noida"),
    *common.TEXTS,
    (HERO, "hero_badge", "Badge", "Now launched · Sector 94, Noida"),
    (HERO, "hero_title_small", "Title: small line", "M3M"),
    (HERO, "hero_title", "Title", "Trump Tower"),
    (HERO, "hero_title_em", "Title: italic line", "Noida"),
    (HERO, "hero_line", "Line under the title", "An address the world recognises, now on Noida Expressway. Branded 4 & 5 BHK residences."),
    (HERO, "card_ribbon", "Form card & popup: ribbon", "Private preview"),
    (HERO, "card_title", "Form card & popup: title", "Get the price list"),
    (HERO, "card_sub", "Form card & popup: line", "Floor plans, payment plan & a site visit, sent to you."),
    (HERO, "card_button", "Form card: button", "Get price list"),
    (HERO, "hero_legal", "Small print at the bottom", "UP RERA {rera} · Arrival court: artistic impression · Other images representative"),
    (BAND, "band_1_title", "1st item: bold", "4 & 5 BHK"),
    (BAND, "band_1_text", "1st item: line", "Branded residences"),
    (BAND, "band_2_title", "2nd item: bold", "Sector 94"),
    (BAND, "band_2_text", "2nd item: line", "Noida Expressway"),
    (BAND, "band_3_title", "3rd item: bold", "Trump"),
    (BAND, "band_3_text", "3rd item: line", "A global luxury name"),
    (BAND, "band_4_title", "4th item: bold", "UP RERA"),
    (BAND, "band_4_text", "4th item: line", "{rera}"),
    (STEPS, "steps_title", "Heading", "Your price list in *three simple steps.*"),
    (STEPS, "steps_button", "Button", "Start now, it’s free"),
    (STEPS, "steps_popup", "Button: popup title", "Get the price list"),
    (LIFT, "lift_kicker", "Small label", "The private lift"),
    (LIFT, "lift_title", "Heading", "Rise to *your residence.*"),
    (
        LIFT,
        "lift_lead",
        "Intro",
        "Choose your residence and how high you would like to live. The lift takes you there, and M3M’s team "
        "sends the prices and floor plans for the floors you chose.",
    ),
    (LIFT, "lift_step_1", "Step 1: question", "Which residence?"),
    (LIFT, "lift_step_2", "Step 2: question", "How high would you like to live?"),
    (LIFT, "lift_step_3", "Step 3: question", "Who shall we welcome?"),
    (LIFT, "lift_next", "Button: next step", "Continue"),
    (LIFT, "lift_back", "Button: back", "Back"),
    (LIFT, "lift_choose_error", "Message when nothing is chosen", "Choose one to continue."),
    (
        LIFT,
        "lift_privacy",
        "Privacy promise",
        "Seen only by M3M’s official team for Trump Tower Noida, who will call you personally. Never shared, never sold.",
    ),
    (LIFT, "lift_button", "Send button", "Take me up"),
    (LIFT, "lift_display", "Lift display: before a floor is chosen", "Lobby"),
    (LIFT, "lift_plate", "Nameplate: label", "The residence of"),
    (LIFT, "lift_guest", "Nameplate: name until one is typed", "Your name"),
    (LIFT, "lift_welcome", "Shown when the lift arrives (after sending)", "Welcome home"),
    (LIFT, "lift_request", "Note saved with each lead", "Requested: Private lift (prices & floor plans)"),
    (RESIDENCES, "res_eyebrow", "Small label", "The residences"),
    (RESIDENCES, "res_title", "Heading", "Homes with a *famous name.*"),
    (RESIDENCES, "res_lead", "Intro", "Generous 4 and 5 BHK residences, finished to a branded standard."),
    (RESIDENCES, "res_button", "Residence button ({unit} = the residence)", "Unlock {unit} details"),
    (RESIDENCES, "res_popup", "Residence button: popup title", "Get the {unit} price & floor plan"),
    (RESIDENCES, "res_note", "Note under the rooms", "Interior images are representative and do not show the actual residences."),
    (COLLECTION, "vault_kicker", "Small label", "The private collection"),
    (COLLECTION, "vault_title", "Heading", "Unlock what *others wait for.*"),
    (
        COLLECTION,
        "vault_lead",
        "Intro",
        "Four sealed envelopes, kept for registered enquirers. Break a seal, or all four, and our team sends it to "
        "you privately.",
    ),
    (COLLECTION, "vault_sealed", "Label on each envelope", "Sealed"),
    (COLLECTION, "vault_unlock", "Button on each envelope", "Break the seal"),
    (COLLECTION, "vault_all", "Main button", "Unlock the whole collection"),
    (COLLECTION, "vault_all_popup", "Main button: popup title", "Unlock the price list, floor plans & brochure"),
    (LIFE, "life_eyebrow", "Small label", "The lifestyle"),
    (LIFE, "life_title", "Heading", "Every day, *a little extraordinary.*"),
    (LIFE, "life_cta_text", "Last tile: text", "The full amenity list is in the official brochure."),
    (LIFE, "life_cta_button", "Last tile: button", "Get the brochure"),
    (LIFE, "life_cta_popup", "Last tile: popup title", "Download the brochure"),
    (LIFE, "life_note", "Note", "Lifestyle images are representative. Amenities follow the official project documents."),
    (LOCATION, "loc_eyebrow", "Small label", "Location"),
    (LOCATION, "loc_title", "Heading", "Sector 94, *at the heart of Noida.*"),
    (LOCATION, "loc_lead", "Intro", "Tap a destination on the board to see the route from Sector 94."),
    (LOCATION, "loc_unit", "Unit after each travel time", "min"),
    (LOCATION, "loc_origin", "Where the routes start (as typed in Google Maps)", "Sector 94, Noida, Uttar Pradesh"),
    (LOCATION, "loc_board", "Board: title", "Departures · Sector 94"),
    (LOCATION, "loc_board_place", "Board: first column", "Destination"),
    (LOCATION, "loc_board_time", "Board: last column", "Drive"),
    (LOCATION, "loc_board_go", "Board: line on each place", "Show route"),
    (LOCATION, "loc_note", "Note", "Travel times as stated by M3M India for its Sector 94 projects; they vary with route and traffic."),
    (LOCATION, "loc_button", "Button", "Book a site visit"),
    (LOCATION, "loc_popup", "Button: popup title", "Book a site visit"),
    (LOCATION, "loc_map_title", "Map description (for screen readers)", "Map of Sector 94, Noida"),
    (
        LOCATION,
        "loc_map_url",
        "Map link, used when the project has none (Google Maps → Share → Embed a map → the src=… link)",
        "https://www.google.com/maps?q=Sector+94,+Noida,+Uttar+Pradesh&output=embed",
    ),
    (FAQ, "faq_eyebrow", "Small label", "Questions"),
    (FAQ, "faq_title", "Heading", "What buyers *ask us first.*"),
    (FINAL, "final_eyebrow", "Small label", "Private preview"),
    (FINAL, "final_title", "Heading", "Your Trump address *starts here.*"),
    (FINAL, "final_whatsapp", "WhatsApp button", "Ask on WhatsApp"),
    (
        FINAL,
        "final_whatsapp_message",
        "WhatsApp: the message typed for the visitor",
        "Hi, I would like the price list and floor plans for M3M Trump Tower Noida.",
    ),
    (FINAL, "final_call", "Call button (the phone number follows)", "Call"),
    (FINAL, "final_card_title", "Form card: title", "Request a callback"),
    (FINAL, "final_card_sub", "Form card: line", "Our team calls you within a working day."),
    (FINAL, "final_card_button", "Form card: button", "Request a callback"),
    (LEGAL, "legal_name", "Project name (bold)", "M3M Trump Tower Noida"),
    (LEGAL, "legal_rera", "RERA line", "UP RERA {rera} · Project details at"),
    (LEGAL, "legal_link_label", "RERA link text", "up-rera.in/projects"),
    (LEGAL, "legal_link_url", "RERA link address", "https://www.up-rera.in/projects"),
    (
        LEGAL,
        "legal_text",
        "Disclaimer",
        "M3M Trump Tower Noida is not owned, developed or sold by The Trump Organization or any of its current or "
        "former principals or affiliates; the “Trump” name and mark are used under licence. Except for the "
        "arrival-court render, all images are representative luxury interiors and do not show the actual project. "
        "Nothing here constitutes a legal offer or forms part of any binding agreement. Please verify all details, "
        "including areas, specifications and prices, with M3M India Private Limited and the RERA disclosures before "
        "making any decision.",
    ),
    (EXTRAS, "slidein_kicker", "Slide-in offer: small line", "Still deciding?"),
    (EXTRAS, "slidein_title", "Slide-in offer: title", "Get the 4 & 5 BHK floor plans"),
    (EXTRAS, "slidein_button", "Slide-in offer: button", "Send them to me"),
    (EXTRAS, "slidein_popup", "Slide-in offer: popup title", "Get the floor plans"),
    (EXTRAS, "sticky_button", "Side tab & mobile bar: button", "Get price list"),
    (EXTRAS, "sticky_popup", "Side tab & mobile bar: popup title", "Get the price list"),
    (EXTRAS, "sticky_call", "Mobile bar: call button", "Call"),
    (FORM, "form_unit_error", "Message when no residence is chosen", "Choose 4 BHK or 5 BHK."),
    (FORM, "form_unit_note", "Small line under each residence button", "Residence"),
    (FORM, "form_note", "Note under the form", "Your details are safe. M3M India may call, WhatsApp or email you about this project."),
]

IMAGES = [
    (common.HEADER, "brand_logo", "Logo (on the dark header and popup; PNG or WebP with transparency)",
     "trump-logo.webp", "Trump Towers Delhi NCR, Tribeca and M3M"),
    (FINAL, "final_bg", "Background", "pool.jpg", ""),
    (EXTRAS, "slidein_image", "Slide-in offer: picture", "suite.jpg", ""),
]

LISTS = {
    **common.LISTS,
    "slides": ("Hero slideshow", "Image: the slide. Title: its caption."),
    "hero_points": ("Hero: three figures", "Value: the bold part. Title: the line under it."),
    "steps": ("Three steps", "Title: the step. Text: one line under it."),
    "residences": (
        "Residences",
        "Title: e.g. “4 BHK”. Value: short code saved with the lead (e.g. 4bhk). Subtitle: small label. "
        "Text: one point per line. Image: the card background. Also the choices in the hero and final forms.",
    ),
    "interiors": ("Residence rooms", "Image, Title and Text: one line under the title."),
    "club": ("Lifestyle tiles", "Image and Title."),
    "specs": ("The private lift: key facts", "Title: the label (e.g. Size). Value: the fact (e.g. 4925 – 5685 sq.ft.)."),
    "lift_floors": (
        "The private lift: floors",
        "Title: the view. Subtitle: the floors. Value: the short word on the lift display (e.g. High). "
        "Image: the view the lift doors open on.",
    ),
    "vault": (
        "The private collection: envelopes",
        "Title, Subtitle (line under it) and Image (shown blurred inside). Link: the popup title. "
        "Value: the residence the popup preselects (optional, e.g. 4bhk).",
    ),
    "connectivity": (
        "Travel times",
        "Value: minutes. Title: the place. Subtitle: its kind, e.g. Hospital. "
        "Link: the place as typed in Google Maps, for the route.",
    ),
    "faq": (
        "Questions",
        "Title: the question. Text: the answer. Subtitle: button label (leave empty for no button). "
        "Link: the popup title that button opens.",
    ),
    "perks": ("Final form: what you get", "Title only."),
}

REPRESENTATIVE = ", representative image"

# Travel times M3M states for its Sector 94 projects (The Cullinan, same sector): (minutes, place, kind, map query)
CONNECTIVITY = (
    ("2", "Amity University", "Education", "Amity University, Sector 125, Noida"),
    ("5", "Max Healthcare", "Hospital", "Max Super Speciality Hospital, Patparganj"),
    ("5", "Jasola Business Park", "Business", "Jasola District Centre, New Delhi"),
    ("10", "Apollo Hospital", "Hospital", "Indraprastha Apollo Hospital, Sarita Vihar"),
    ("12", "Ansal Plaza", "Shopping", "Ansal Plaza, Khel Gaon Marg, New Delhi"),
    ("12", "Radisson Blu, Sector 18", "Hospitality", "Radisson Blu MBD Hotel, Noida"),
)

SPECS = (
    ("Apartments", "4 & 5 BHK"),
    ("Price", "On request"),
    ("Size", "4925 – 5685 sq.ft."),
    ("Location", "Noida"),
)

LIFT_FLOORS = (
    ("City view", "Lower floors", "Low", "living"),
    ("The skyline", "Middle floors", "Mid", "salon"),
    ("Above the clouds", "Higher floors", "High", "clouds"),
    ("Any floor", "Show me every option", "Any", "lounge-hall"),
)

VAULT_ITEMS = (
    ("Launch price list", "Every residence, every floor", "Unlock the launch price list", "", "dossier"),
    ("Floor plans", "4 & 5 BHK, in full", "Unlock the floor plans", "", "suite"),
    ("Payment plan", "Milestones and launch offers", "Unlock the payment plan", "", "lobby"),
    ("Brochure", "The complete Trump Tower story", "Unlock the brochure", "", "arrival"),
)

ITEMS = {
    "nav": common.nav(("residences", "Residences"), ("lifestyle", "Lifestyle"), ("location", "Location"), ("faq", "FAQ")),
    "popup_units": common.popup_units(
        ("4bhk", "4 BHK", "Residence", "residential", SLUG),
        ("5bhk", "5 BHK", "Residence", "residential", SLUG),
    ),
    # "arrival" is the only official render; the rest are representative interiors.
    "slides": [
        {"image": f"{name}.jpg", "title": caption}
        for name, caption in (
            ("arrival", "The arrival court"),
            ("salon", "Living, above the city"),
            ("pool", "An evening by the pool"),
            ("clouds", "Mornings above the clouds"),
            ("living", "Light, space and calm"),
        )
    ],
    "hero_points": [
        {"value": "4 & 5", "title": "BHK residences"},
        {"value": "Trump", "title": "branded living"},
        {"value": "Sector 94", "title": "Noida Expressway"},
    ],
    "steps": [
        {"title": "Share your details", "text": "Name, mobile and 4 or 5 BHK. It takes 20 seconds."},
        {"title": "Get the price list", "text": "Our team shares prices, floor plans and the payment plan."},
        {"title": "Visit privately", "text": "See the project at a time that suits you."},
    ],
    "residences": [
        {
            "value": value,
            "title": title,
            "subtitle": "Residence",
            "text": "Size on request\nFloor plan on request\nLaunch price on request",
            "image": image,
        }
        for value, title, image in (("4bhk", "4 BHK", "salon.jpg"), ("5bhk", "5 BHK", "lounge-hall.jpg"))
    ],
    "interiors": [
        {"image": f"{name}.jpg", "title": title, "text": line, "image_alt": title + REPRESENTATIVE}
        for name, title, line in (
            ("living", "The living room", "Wide, bright and made for gathering."),
            ("dining", "The dining room", "A table for every occasion."),
            ("suite", "The principal suite", "Quiet, layered and generous."),
            ("lounge-hall", "The lounge", "Space to breathe, views to keep."),
        )
    ],
    "club": [
        {"image": f"{name}.jpg", "title": title, "image_alt": title + REPRESENTATIVE}
        for name, title in (
            ("pool", "Swimming pool"),
            ("spa", "Spa & wellness"),
            ("gym", "Fitness studio"),
            ("bar", "Residents’ lounge"),
            ("cinema", "Screening room"),
            ("library", "Reading lounge"),
            ("games", "Games room"),
        )
    ],
    "specs": [{"title": label, "value": fact} for label, fact in SPECS],
    "lift_floors": [
        {"title": title, "subtitle": floors, "value": word, "image": f"{name}.jpg"}
        for title, floors, word, name in LIFT_FLOORS
    ],
    "vault": [
        {"title": title, "subtitle": line, "link": popup, "value": preset, "image": f"{name}.jpg"}
        for title, line, popup, preset, name in VAULT_ITEMS
    ],
    "connectivity": [
        {"value": minutes, "title": place, "subtitle": kind, "link": query}
        for minutes, place, kind, query in CONNECTIVITY
    ],
    "faq": [
        {
            "title": "What is the price of M3M Trump Tower Noida?",
            "text": "Prices depend on the residence, floor and view. Request the launch price list and our team will "
            "share the current prices and payment plan.",
            "subtitle": "Get the price list",
            "link": "Get the launch price list",
        },
        {
            "title": "Which residences are available?",
            "text": "The project offers 4 BHK and 5 BHK residences. Sizes and floor plans are shared on request.",
            "subtitle": "Get the floor plans",
            "link": "Get the floor plans",
        },
        {
            "title": "Where is the project?",
            "text": "In Sector 94, Noida, on the Noida Expressway corridor, minutes from Amity University and Jasola "
            "Business Park.",
            "subtitle": "Get the location map",
            "link": "Get the location map",
        },
        {
            "title": "Is the project RERA registered?",
            "text": "Yes. The UP RERA registration is {rera}; details can be checked on up-rera.in.",
        },
        {
            "title": "Can I visit the site?",
            "text": "Yes. Share your details and our team will arrange a private visit at a time that suits you.",
            "subtitle": "Book a site visit",
            "link": "Book a private site visit",
        },
    ],
    "perks": [
        {"title": title}
        for title in ("Launch price list", "4 & 5 BHK floor plans", "Payment plan", "Private site visit")
    ],
}
