"""Billionaire Block page (templates/projects/billionaire_block.html and billionaire/story.html).

Hero media, title, eyebrow and tagline, the private viewing form texts, the brochure, the footer
disclaimer, RERA and SEO stay on “Billionaire Block page”; everything else is here.

Facts follow the January 2026 M3M India / Smartworld Developers / ELIE SAAB announcement as reported by
Business Today and Outlook Luxe, and the client's research notes. Every image is an AI-generated concept
or artistic impression, never an official render; alt texts say so.
"""

SLUG = "billionaire-block"
NAME = "Billionaire Block"
STATIC_DIR = "images/billionaire/"
SEO = {}  # On “Billionaire Block page”.

NAV = "1. Header & menu"
HERO = "2. Hero"
PLAN = "3. The plan"
BRAND = "4. ELIE SAAB Residences"
DETAILS = "5. Announced details"
COMMUNITY = "6. Community"
AMENITIES = "7. Amenities"
TOWERS = "8. Towers & layouts"
STRATEGY = "9. Strategy"
LOCATION = "10. Location"
CHECKS = "11. Timeline & legal checks"
SOURCES = "12. Sources"
FORM = "13. Private viewing form"
FOOTER = "14. Footer & floating buttons"
POPUPS = "15. Pop-ups"

TEXTS = [
    (NAV, "skip", "Skip link (for keyboard users)", "Skip to content"),
    (NAV, "brand_by", "Small line after the name", "by M3M"),
    (NAV, "home", "Link back to the M3M website", "M3M Home"),
    (NAV, "home_short", "Same link on small screens", "Home"),
    (NAV, "home_aria", "Same link, for screen readers", "M3M Home: back to the M3M India website"),
    (NAV, "nav_cta", "Header button", "Enquire Now"),
    (NAV, "menu_open", "Menu button, for screen readers", "Open menu"),
    (NAV, "menu_brochure", "Menu: brochure button", "Download the brochure"),
    (NAV, "whatsapp", "WhatsApp link text", "WhatsApp"),
    (HERO, "hero_enquire", "First button", "Enquire Now"),
    (HERO, "hero_explore", "Second button", "Explore Residences"),
    (HERO, "hero_caption", "Caption at the bottom", "Artistic impression"),
    (HERO, "hero_scroll", "Scroll hint", "Scroll"),
    (HERO, "hero_scroll_aria", "Scroll hint, for screen readers", "Scroll to discover"),
    (PLAN, "plan_eyebrow", "Small label", "The plan"),
    (PLAN, "plan_title", "Heading", "What exactly is *M3M* planning to develop?"),
    (PLAN, "plan_note", "Note under the slideshow", "AI-generated concepts, not official renders"),
    (
        PLAN,
        "plan_footnote",
        "Footnote",
        "The 170-acre enclave is part of the wider SCDA township, not an addition to it. Township area as described "
        "in SCDA project information.",
    ),
    (BRAND, "brand_eyebrow", "Small label", "First in the enclave"),
    (BRAND, "brand_title", "Heading", "Signature Residences *by ELIE SAAB*"),
    (BRAND, "brand_lead", "Intro", "Four-bedroom homes, waterfront views and the couture house’s own Maison furnishings."),
    (BRAND, "brand_button", "Button", "Request Project Details"),
    (DETAILS, "details_eyebrow", "Small label", "Announced details"),
    (DETAILS, "details_title", "Heading", "A clearly defined *luxury* residence."),
    (
        DETAILS,
        "details_footnote",
        "Footnote",
        "Source: joint M3M India, Smartworld Developers and ELIE SAAB announcement, January 2026.",
    ),
    (COMMUNITY, "community_eyebrow", "Small label", "Community"),
    (COMMUNITY, "community_title", "Heading", "What type of society is *M3M* trying to create?"),
    (COMMUNITY, "community_lead", "Intro", "Two levels: a private enclave, inside a complete township."),
    (
        COMMUNITY,
        "community_footnote",
        "Footnote",
        "Stated project objectives and design intentions, not proof that every planned facility is built.",
    ),
    (AMENITIES, "amenities_eyebrow", "Small label", "Amenities"),
    (AMENITIES, "amenities_title", "Heading", "What amenities are they *planning* to deliver?"),
    (
        AMENITIES,
        "amenities_footnote",
        "Footnote",
        "Named in the ELIE SAAB project announcement. Final specifications follow the approved plans. Images are "
        "representative.",
    ),
    (TOWERS, "towers_eyebrow", "Small label", "Towers & layouts"),
    (TOWERS, "towers_title", "Heading", "What type of towers, blocks and *layouts*?"),
    (TOWERS, "towers_established", "First list: heading", "What is established"),
    (TOWERS, "towers_pending", "Second list: heading", "Awaiting the sanctioned master plan"),
    (STRATEGY, "strategy_eyebrow", "Small label", "Strategy"),
    (STRATEGY, "strategy_title", "Heading", "What is M3M’s broader *development strategy*?"),
    (STRATEGY, "strategy_number", "Word before each number", "Strategy"),
    (LOCATION, "location_caption", "Caption on the picture", "Sector 111 · SCDA · Dwarka Expressway"),
    (LOCATION, "location_eyebrow", "Small label", "Location"),
    (LOCATION, "location_title", "Heading", "Location & *connectivity*"),
    (LOCATION, "location_lead", "Intro", "Sector 111, Gurugram, within SCDA and along the Dwarka Expressway corridor."),
    (
        LOCATION,
        "location_footnote",
        "Footnote",
        "From the project announcement. Travel times depend on the entrance, route and traffic.",
    ),
    (CHECKS, "checks_eyebrow", "Small label", "Timeline, investment & legal"),
    (CHECKS, "checks_title", "Heading", "Launch timeline, investment *& legal checks*"),
    (CHECKS, "checks_list_title", "Checklist: heading", "Before treating any specification as final, verify"),
    (
        CHECKS,
        "checks_callout",
        "Highlighted note",
        "The Billionaire’s Block is the enclave’s identity. Each residential project has its own promoter, approvals "
        "and RERA disclosures, so check that project’s documents.",
    ),
    (SOURCES, "sources_eyebrow", "Small label", "Sources"),
    (SOURCES, "sources_title", "Heading", "Sources for *further research*"),
    (FORM, "form_steps_title", "“What happens next” heading", "What happens next"),
    (FORM, "form_call", "Call card: label", "Call us"),
    (FORM, "form_message", "WhatsApp card: label", "Message us"),
    (FORM, "field_name", "Field: name", "Full name"),
    (FORM, "field_email", "Field: email", "Email"),
    (FORM, "field_phone", "Field: phone", "Phone"),
    (FORM, "field_residence", "Field: residence", "Preferred residence"),
    (FORM, "field_residence_empty", "Field: residence, first choice", "Undecided"),
    (FORM, "field_date", "Field: date", "Preferred date"),
    (FORM, "field_message", "Field: message", "Message"),
    (FORM, "field_optional", "Word after “Message”", "(optional)"),
    (FORM, "field_chauffeur", "Chauffeur tick box", "Arrange a chauffeur pickup for my viewing"),
    (FORM, "form_submit", "Send button", "Request Invitation"),
    (FORM, "form_reset", "After sending: button", "Send another request"),
    (FOOTER, "footer_brochure", "Footer: brochure button", "Download brochure"),
    (FOOTER, "footer_rights", "Copyright line (after the year and company name)", "All rights reserved."),
    (FOOTER, "footer_disclaimer_link", "Disclaimer link text", "Disclaimer"),
    (FOOTER, "whatsapp_aria", "WhatsApp button, for screen readers", "Message us on WhatsApp"),
    (FOOTER, "sticky_cta", "Sticky button on phones", "Private Viewing"),
    (POPUPS, "plan_label", "Floor plan: small label", "Floor plan"),
    (POPUPS, "plan_size", "Floor plan: size label", "Size"),
    (POPUPS, "plan_configuration", "Floor plan: configuration label", "Configuration"),
    (
        POPUPS,
        "plan_placeholder",
        "Floor plan: text when no plan is uploaded",
        "Detailed floor plans are presented during your private viewing, alongside the material library and a "
        "walk-through of the residence.",
    ),
    (POPUPS, "plan_request", "Floor plan: button", "Request this floor plan"),
    (POPUPS, "brochure_label", "Brochure: small label", "Brochure"),
    (POPUPS, "brochure_submit", "Brochure: button", "Download Brochure"),
    (POPUPS, "brochure_thanks", "Brochure: after sending", "Thank you."),
    (POPUPS, "news_previous", "News story: previous", "← Previous story"),
    (POPUPS, "news_next", "News story: next", "Next story →"),
]

IMAGES = [
    (
        BRAND,
        "brand_main",
        "Large picture",
        "living-room.jpg",
        "Couture-inspired living room opening to a terrace and lake at sunset, AI-generated concept",
    ),
    (
        BRAND,
        "brand_inset",
        "Small picture",
        "deck-jacuzzi.jpg",
        "Wrap-around deck with a private jacuzzi above a lake at dusk, AI-generated concept",
    ),
    (
        TOWERS,
        "towers_image",
        "Tall picture",
        "tower-elevation.jpg",
        "Slender residential tower with wrap-around balconies at dusk, AI-generated concept",
    ),
    (
        TOWERS,
        "towers_model",
        "Second picture",
        "masterplan-model.jpg",
        "Architectural scale model of a master-planned township, AI-generated concept",
    ),
    (
        LOCATION,
        "location_image",
        "Picture",
        "airport-corridor.jpg",
        "Expressway corridor with flyovers leading towards an airport, AI-generated concept",
    ),
    (
        CHECKS,
        "checks_image",
        "Picture",
        "due-diligence.jpg",
        "Architectural plans, a bound agreement and a tower model on a desk, AI-generated concept",
    ),
]

LISTS = {
    "nav": (
        "Header links",
        "Title: the link text. Link: the section it jumps to (#overview, #residences…). "
        "Group: 2 or 3 hides the link on smaller screens (3 hides it first).",
    ),
    "menu": ("Menu links (phones)", "Title: the link text. Link: the section it jumps to, e.g. #community."),
    "plan_slides": ("The plan: slideshow", "Image, Title: its caption, Image description."),
    "facts": (
        "The plan: four facts",
        "Title: small label. Value: the bold figure. Group: a unit after the figure (e.g. acres), which makes the "
        "figure count up. Text: the line under it.",
    ),
    "brand_chips": (
        "ELIE SAAB Residences: figures",
        "Value: a number that counts up (optional). Title: the words after it, or the same number to show the number alone.",
    ),
    "announced_details": ("Announced details", "Title: the label. Subtitle: the detail."),
    "community": ("Community cards", "Value: the letter. Title, Image, Image description. Text: one point per line."),
    "amenities": ("Amenities", "Title, Text: one line, Image, Image description."),
    "towers_established": ("Towers: what is established", "Title: the bold start. Text: the rest of the sentence."),
    "towers_pending": ("Towers: awaiting the master plan", "Title only."),
    "strategies": ("Strategies", "Title, Text, Image, Image description."),
    "routes": ("Location: connections", "Title only."),
    "figures": ("Timeline & investment figures", "Title: the figure. Text: what it means."),
    "legal_checks": ("Before you buy, verify", "Title only."),
    "sources": ("Sources", "Title, Text: one line. Subtitle: the link text. Link: the web address."),
}

ITEMS = {
    "nav": [
        {"title": title, "link": link, "group": group}
        for title, link, group in (
            ("Overview", "#overview", ""),
            ("Residences", "#residences", ""),
            ("Community", "#community", "3"),
            ("Amenities", "#amenities", ""),
            ("Strategy", "#strategy", "2"),
            ("Location", "#location", ""),
            ("Legal", "#before-you-buy", "2"),
        )
    ],
    "menu": [
        {"title": title, "link": link}
        for title, link in (
            ("Overview", "#overview"),
            ("ELIE SAAB Residences", "#residences"),
            ("Community", "#community"),
            ("Amenities", "#amenities"),
            ("Towers & layouts", "#towers"),
            ("Strategy", "#strategy"),
            ("Location", "#location"),
            ("Timeline & legal checks", "#before-you-buy"),
            ("Sources", "#sources"),
            ("Enquire", "#private-viewing"),
        )
    ],
    "plan_slides": [
        {"image": f"{name}.jpg", "title": caption, "image_alt": alt}
        for name, caption, alt in (
            (
                "township-aerial",
                "Drone view of the whole township",
                "Aerial view of an integrated township with towers, offices, a lake and an expressway, AI-generated concept",
            ),
            (
                "branded-towers",
                "Branded luxury residential concept",
                "Three slender residential towers beside a reflecting lake at dusk, AI-generated concept",
            ),
            (
                "township-concept",
                "Wider integrated township concept",
                "Mixed-use township with residences, offices, a hotel and green spines in morning mist, AI-generated concept",
            ),
            (
                "enclave-drone",
                "The enclave from above",
                "Top-down view of a landscaped enclave with a lake and garden avenues, AI-generated concept",
            ),
            (
                "expressway-night",
                "Along the Dwarka Expressway corridor",
                "Illuminated towers beside an expressway at blue hour, AI-generated concept",
            ),
        )
    ],
    "facts": [
        {"title": "Location", "value": "Sector 111, Gurugram", "text": "Dwarka Expressway, within SCDA"},
        {"title": "Billionaire’s Block", "value": "170", "group": "acres", "text": "Planned branded-residence enclave"},
        {"title": "Larger SCDA township", "value": "250", "group": "acres", "text": "Mixed-use master development"},
        {
            "title": "First announced branded project",
            "value": "ELIE SAAB Residences",
            "text": "300 planned residences in Gurugram",
        },
    ],
    "brand_chips": [
        {"value": "300", "title": "residences"},
        {"title": "4 bedrooms"},
        {"title": "4,200–4,650 sq ft"},
        {"value": "2030", "title": "2030"},
    ],
    "announced_details": [
        {"title": label, "subtitle": value}
        for label, value in (
            ("Project", "Signature Residences by ELIE SAAB"),
            ("Location", "Sector 111, SCDA, Gurugram"),
            ("Residences", "300"),
            ("Configuration", "Four-bedroom residences"),
            ("Sizes", "Approx. 4,200–4,650 sq ft"),
            ("Outdoor living", "Wrap-around decks and private jacuzzis"),
            ("Views", "Waterfront views, part of the announced concept"),
            ("Design identity", "ELIE SAAB Maison furnishings and décor"),
            ("Expected completion", "2030, per the launch announcement"),
        )
    ],
    "community": [
        {
            "value": "A",
            "title": "Billionaire’s Block — exclusive luxury community",
            "image": "enclave-courtyard.jpg",
            "image_alt": "Residents walking through a shaded garden courtyard with a water channel, AI-generated concept",
            "text": "Brand-led residential identity\n"
            "Privacy-oriented living\n"
            "Large residences, expansive balconies, brand-specific interiors\n"
            "Lifestyle-led common spaces\n"
            "International design influence",
        },
        {
            "value": "B",
            "title": "SCDA — integrated urban community",
            "image": "township-boulevard.jpg",
            "image_alt": "Tree-lined boulevard with cafés, offices and a cycling lane at sunset, AI-generated concept",
            "text": "Luxury residential developments\n"
            "Grade-A office spaces\n"
            "High-street retail and shopping\n"
            "Premium hospitality\n"
            "Pedestrian routes, cycling paths and landscaped walkways",
        },
    ],
    "amenities": [
        {"title": title, "text": line, "image": image, "image_alt": alt}
        for title, line, image, alt in (
            ("Swimming pools & leisure", "Poolside spaces woven into the residences.", "amenity-pool.jpg", "Pool deck at night, representative image"),
            ("Wellness & spa", "Spaces for rest and personal well-being.", "amenity-spa.jpg", "Domed marble spa, representative image"),
            ("Fitness & health", "A fitness centre for residents.", "amenity-fitness.jpg", "Residents’ fitness centre with lake views, AI-generated concept"),
            ("Residents’ lounges", "Shared interiors in ELIE SAAB Maison style.", "amenity-lounge.jpg", "Lounge with tall bookshelves, representative image"),
            ("Landscaped outdoors", "Privacy, decks and waterfront views.", "enclave-drone.jpg", "Landscaped enclave with a lake from above, AI-generated concept"),
            ("Concierge services", "Hospitality-style resident assistance.", "amenity-concierge.jpg", "Arrival court at night, representative image"),
            ("Family & children", "Dedicated children’s play areas.", "amenity-children.jpg", "Children’s studio, representative image"),
        )
    ],
    "towers_established": [
        {"title": title, "text": text}
        for title, text in (
            ("The wider enclave", "hosts a selection of branded residences."),
            ("The first residence", "is ELIE SAAB, with 300 four-bedroom homes."),
            ("Apartment scale", "of about 4,200–4,650 sq ft."),
            ("Design emphasis", "on large living spaces, wrap-around decks and waterfront views."),
            ("Vertical format:", "a luxury high-rise residential development."),
        )
    ],
    "towers_pending": [
        {"title": title} for title in ("Number of towers", "Floors & heights", "Block layout", "Open-space plan")
    ],
    "strategies": [
        {"title": title, "text": text, "image": image, "image_alt": alt}
        for title, text, image, alt in (
            ("Build an enclave, not just one project", "A larger planned precinct for several branded residences.", "masterplan-model.jpg", "Scale model of a master-planned township, AI-generated concept"),
            ("Bring international brands into residential design", "ELIE SAAB’s design language and Maison furnishings.", "strategy-design.jpg", "Marble, bronze and fluted stone detail, artistic impression"),
            ("Integrate homes with urban infrastructure", "Residences, offices, retail and hospitality in one township.", "township-concept.jpg", "Mixed-use township in morning mist, AI-generated concept"),
            ("Position the product around a complete lifestyle", "Concierge, wellness, pools, fitness, lounges and play.", "strategy-lifestyle.jpg", "Terrace pool above the clouds at sunset, artistic impression"),
        )
    ],
    "routes": [
        {"title": title}
        for title in (
            "Delhi and the NCR",
            "Indira Gandhi International Airport",
            "The Aerocity area",
            "Gurugram’s business districts",
            "The wider SCDA development",
        )
    ],
    "figures": [
        {"title": "₹3,500 cr", "text": "Combined investment, Gurugram and Noida ELIE SAAB projects"},
        {"title": "2030", "text": "Announced completion target"},
    ],
    "legal_checks": [
        {"title": title}
        for title in (
            "The project’s legal promoter and Haryana RERA registration",
            "The approved layout and sanctioned building plans",
            "The final number of towers, floors and residences",
            "The exact apartment sizes and areas in the sale",
            "The amenities written into the agreement and approved plans",
            "The construction and possession schedule",
            "Maintenance charges, clubhouse rules and running costs",
            "Whether services are in the maintenance fee or charged separately",
        )
    ],
    # Only pages that were opened and checked.
    "sources": [
        {"title": title, "text": text, "subtitle": label, "link": url}
        for title, text, label, url in (
            (
                "M3M India — official website",
                "The developer’s projects, including SCDA and its luxury corridor.",
                "Open m3mindia.com",
                "https://m3mindia.com/",
            ),
            (
                "ELIE SAAB Signature Residences — announcement",
                "Brand and interiors context, ELIE SAAB Maison and the launch details.",
                "Read on Outlook Luxe",
                "https://luxe.outlookindia.com/art-design/real-estate/m3m-india-and-smartworld-developers-launch-elie-saab-signature-residences-in-india",
            ),
            (
                "Launch figures — Business Today",
                "Residences, sizes, pricing and investment as reported at launch.",
                "Read on Business Today",
                "https://www.businesstoday.in/real-estate/story/m3m-eyes-rs-8300-crore-from-elie-saab-branded-residences-in-gurugram-noida-510767-2026-01-13",
            ),
            (
                "Haryana RERA",
                "Independent check of registration and statutory disclosures.",
                "Open Haryana RERA",
                "https://haryanarera.gov.in/",
            ),
        )
    ],
}
