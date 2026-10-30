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
    (HERO, "hero_badge", "Small badge above the title", "By invitation"),
    (PLAN, "plan_eyebrow", "Small label", "The plan"),
    (PLAN, "plan_title", "Heading", "What exactly is *M3M* planning to develop?"),
    (
        PLAN,
        "plan_lead",
        "Intro",
        "One address, four defining facts. Choose one to see it, or let the story play.",
    ),
    (PLAN, "plan_note", "Note on the picture", "AI-generated concepts, not official renders"),
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
    (BRAND, "brand_monogram", "Large faint letters behind the section", "ES"),
    (BRAND, "brand_caption", "Caption on the large picture", "The couture salon · AI-generated concept"),
    (DETAILS, "details_eyebrow", "Small label", "The couture residence"),
    (DETAILS, "details_title", "Heading", "A residence *tailored* like haute couture."),
    (
        DETAILS,
        "details_lead",
        "Intro",
        "Everything announced so far, in one room. Touch the gold points to explore it.",
    ),
    (DETAILS, "details_card_label", "Card: small label", "Residence dossier"),
    (DETAILS, "details_card_no", "Card: reference shown at the top", "ES · 111"),
    (DETAILS, "details_button", "Card: button", "Reserve a private presentation"),
    (DETAILS, "details_hint", "Hint on the picture", "Explore the residence"),
    (
        DETAILS,
        "details_footnote",
        "Footnote",
        "Source: joint M3M India, Smartworld Developers and ELIE SAAB announcement, January 2026.",
    ),
    (COMMUNITY, "community_eyebrow", "Small label", "Community"),
    (COMMUNITY, "community_title", "Heading", "What type of society is *M3M* trying to create?"),
    (COMMUNITY, "community_lead", "Intro", "Two levels: a private enclave, inside a complete township."),
    (COMMUNITY, "community_hint", "Hint beside the rings", "Choose a circle"),
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
        "amenities_lead",
        "Intro",
        "Seven worlds of resort living, planned for residents. Hover or tap to open each.",
    ),
    (
        AMENITIES,
        "amenities_footnote",
        "Footnote",
        "As described in the ELIE SAAB project announcement. Final specifications follow the approved plans. Images "
        "are representative.",
    ),
    (TOWERS, "towers_eyebrow", "Small label", "Towers & layouts"),
    (TOWERS, "towers_title", "Heading", "What type of towers, blocks and *layouts*?"),
    (TOWERS, "towers_established", "First list: heading", "What is established"),
    (TOWERS, "towers_pending", "Second list: heading", "To be confirmed in the sale documents"),
    (TOWERS, "towers_pending_tag", "Label on each awaited item", "To be announced"),
    (TOWERS, "towers_level", "Word before each level number", "Level"),
    (STRATEGY, "strategy_eyebrow", "Small label", "Strategy"),
    (STRATEGY, "strategy_title", "Heading", "What is M3M’s broader *development strategy*?"),
    (STRATEGY, "strategy_number", "Word before each number", "Strategy"),
    (LOCATION, "location_caption", "Caption on the picture", "Sector 111 · SCDA · Dwarka Expressway"),
    (LOCATION, "location_eyebrow", "Small label", "Location"),
    (LOCATION, "location_title", "Heading", "Location & *connectivity*"),
    (LOCATION, "location_lead", "Intro", "Sector 111, Gurugram, within SCDA and along the Dwarka Expressway corridor."),
    (LOCATION, "location_origin", "Starting point for routes (as typed in Google Maps)", "Sector 111, Gurugram, Haryana"),
    (LOCATION, "location_from", "Label before the starting point", "From Billionaire Block"),
    (LOCATION, "location_route", "Link to the route in Google Maps", "See the route"),
    (LOCATION, "location_unit", "Word after a travel time", "min"),
    (
        LOCATION,
        "location_footnote",
        "Footnote",
        "Indicative connectivity. Travel times depend on the entrance, route and traffic.",
    ),
    (CHECKS, "checks_eyebrow", "Small label", "Timeline, investment & legal"),
    (CHECKS, "checks_title", "Heading", "Launch timeline, investment *& legal checks*"),
    (CHECKS, "checks_list_title", "Checklist: heading", "Before treating any specification as final, verify"),
    (CHECKS, "checks_timeline_title", "Timeline: heading", "The road to 2030"),
    (CHECKS, "checks_progress", "Checklist: progress ({done} and {total} are filled in)", "{done} of {total} verified"),
    (CHECKS, "checks_hint", "Checklist: hint", "Tick each point as you verify it."),
    (
        CHECKS,
        "checks_callout",
        "Highlighted note",
        "The Billionaire’s Block is the enclave’s identity. Each residential project has its own promoter, approvals "
        "and RERA disclosures, so check that project’s documents.",
    ),
    (SOURCES, "sources_eyebrow", "Small label", "Sources"),
    (SOURCES, "sources_title", "Heading", "Sources for *further research*"),
    (
        SOURCES,
        "sources_lead",
        "Intro",
        "The announcement that put Gurugram on the couture map, and where to check every detail for yourself.",
    ),
    (SOURCES, "sources_ticker", "Moving line of names (separate with ·)", "Outlook Luxe · Business Today · M3M India · Haryana RERA · ELIE SAAB"),
    (SOURCES, "sources_featured", "Label on the featured source", "Featured announcement"),
    (SOURCES, "sources_featured_quote", "Quote on the featured source", "The brand’s first branded residential developments in the country."),
    (SOURCES, "sources_read", "Link text on each card", "Read"),
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
    (FORM, "field_chauffeur_note", "Chauffeur: small line under it", "Complimentary, from anywhere in Delhi NCR"),
    (FORM, "field_mode", "Field: how to meet", "How would you like to meet?"),
    (FORM, "field_purpose", "Field: purpose", "You are considering it as"),
    (FORM, "field_day", "Field: day", "Choose a day"),
    (FORM, "field_time", "Field: time", "Preferred time"),
    (FORM, "field_guests", "Field: guests", "Guests attending"),
    (FORM, "field_day_more", "Day tiles: button for a later date", "Later date"),
    (FORM, "form_pass_label", "Invitation card: title", "Private viewing invitation"),
    (FORM, "form_admit", "Invitation card: small line above the title", "Billionaire Block · by M3M"),
    (FORM, "form_pass_no", "Invitation card: letters before the number", "BB"),
    (FORM, "form_step_choose", "Invitation card: first step", "Your viewing"),
    (FORM, "form_step_details", "Invitation card: second step", "Your details"),
    (FORM, "form_confirmed", "Stamp shown after sending", "Invited"),
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
        "salon.jpg",
        "Double-height salon with a crystal chandelier and city views at sunset, AI-generated concept",
    ),
    (
        BRAND,
        "brand_inset",
        "Small picture",
        "deck-jacuzzi.jpg",
        "Wrap-around deck with a private jacuzzi above a lake at dusk, AI-generated concept",
    ),
    (
        BRAND,
        "brand_detail",
        "Third picture",
        "suite.jpg",
        "Master suite with floor-to-ceiling windows at sunset, AI-generated concept",
    ),
    (
        DETAILS,
        "details_image",
        "Large picture with the gold points",
        "living-room.jpg",
        "Couture-inspired living room opening to a terrace and lake at sunset, AI-generated concept",
    ),
    (
        SOURCES,
        "sources_image",
        "Picture on the featured source",
        "sky-villa.jpg",
        "Double-height sky villa living room above the clouds, AI-generated concept",
    ),
    (
        FORM,
        "form_image",
        "Picture beside the invitation",
        "private-terrace.jpg",
        "Resident on a private terrace overlooking greenery, AI-generated concept",
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
    "hero_stats": ("Hero: figures along the bottom", "Value: the bold figure. Title: the line under it."),
    "facts": (
        "The plan: four facts",
        "Title: small label. Value: the bold figure. Group: a unit after the figure (e.g. acres), which makes the "
        "figure count up. Text: the line under it. Image: the picture shown when the fact is chosen.",
    ),
    "brand_chips": (
        "ELIE SAAB Residences: figures",
        "Value: a number that counts up (optional). Title: the words after it, or the same number to show the number alone.",
    ),
    "announced_details": ("Announced details", "Title: the label. Subtitle: the detail."),
    "hotspots": (
        "Couture residence: gold points on the picture",
        "Title, Text. Value: where the point sits, as across,down in percent (e.g. 22,55).",
    ),
    "community": (
        "Community circles",
        "Value: the letter. Title. Subtitle: the area (e.g. 170 acres). Image, Image description. "
        "Text: one point per line. The first is the inner circle.",
    ),
    "amenities": ("Amenities", "Title, Text: one line, Image, Image description."),
    "towers_established": ("Towers: what is established", "Title: the bold start. Text: the rest of the sentence."),
    "towers_pending": ("Towers: awaiting the master plan", "Title only."),
    "strategies": ("Strategies", "Title, Text, Image, Image description."),
    "routes": (
        "Location: destinations",
        "Title. Subtitle: small line above it. Text: one sentence. Value: travel time in minutes (optional). "
        "Link: the destination as typed in Google Maps. Image: the picture shown when it is chosen.",
    ),
    "figures": ("Timeline & investment figures", "Title: the figure. Text: what it means."),
    "milestones": ("Timeline", "Title: the date. Subtitle: the milestone. Text: one line. Group: done or next."),
    "legal_checks": ("Before you buy, verify", "Title only."),
    "sources": (
        "Sources",
        "Title, Text: one line. Subtitle: the link text. Link: the web address. Group: featured puts it in the "
        "large card.",
    ),
    "visit_modes": ("Private viewing: ways to meet", "Title. Subtitle: small line under it."),
    "visit_purposes": ("Private viewing: purposes", "Title only."),
    "visit_slots": (
        "Private viewing: times",
        "Title. Subtitle: the hours. Value: morning, afternoon, evening or flexible.",
    ),
}

# The plan: label, figure, unit, line, picture, picture description.
FACTS = (
    (
        "Location",
        "Sector 111, Gurugram",
        "",
        "Dwarka Expressway, within SCDA",
        "expressway-night.jpg",
        "Illuminated towers beside an expressway at blue hour, AI-generated concept",
    ),
    (
        "Billionaire’s Block",
        "170",
        "acres",
        "Planned branded-residence enclave",
        "enclave-drone.jpg",
        "Top-down view of a landscaped enclave with a lake and garden avenues, AI-generated concept",
    ),
    (
        "The township",
        "SCDA",
        "",
        "Smart City Delhi Airport, M3M’s mixed-use master development",
        "township-aerial.jpg",
        "Aerial view of an integrated township with towers, offices, a lake and an expressway, AI-generated concept",
    ),
    (
        "First announced branded project",
        "ELIE SAAB Residences",
        "",
        "300 planned residences in Gurugram",
        "branded-towers.jpg",
        "Three slender residential towers beside a reflecting lake at dusk, AI-generated concept",
    ),
)

# Location: destination, kind, one line, Google Maps query, picture, picture description.
ROUTES = (
    (
        "Delhi and the NCR",
        "The capital region",
        "Across the Dwarka Expressway into Delhi and the wider NCR.",
        "Dwarka, New Delhi",
        "expressway-night.jpg",
        "Expressway into the city at blue hour, representative image",
    ),
    (
        "Indira Gandhi International Airport",
        "International gateway",
        "India’s busiest airport, along the same expressway corridor.",
        "Indira Gandhi International Airport, New Delhi",
        "airport-corridor.jpg",
        "Expressway corridor with flyovers leading to an airport, representative image",
    ),
    (
        "The Aerocity area",
        "Hospitality district",
        "Five-star hotels, fine dining and business venues by the airport.",
        "Aerocity, New Delhi",
        "arrival.jpg",
        "Five-star hotel arrival court at night, representative image",
    ),
    (
        "Gurugram’s business districts",
        "Corporate hubs",
        "Cyber City, Golf Course Road and the city’s Grade-A offices.",
        "Cyber City, Gurugram",
        "township-concept.jpg",
        "Offices and towers of a business district in morning light, representative image",
    ),
    (
        "The wider SCDA development",
        "Your own township",
        "Offices, retail, hospitality and green walkways around the enclave.",
        "",
        "township-aerial.jpg",
        "Aerial view of an integrated township with a lake, AI-generated concept",
    ),
)

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
    "hero_stats": [
        {"value": value, "title": title}
        for value, title in (
            ("170 acres", "Branded-residence enclave"),
            ("300", "ELIE SAAB residences"),
            ("4,200+ sq ft", "Four-bedroom homes"),
            ("2030", "Completion target"),
        )
    ],
    "facts": [
        {"title": title, "value": value, "group": group, "text": text, "image": image, "image_alt": alt}
        for title, value, group, text, image, alt in FACTS
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
    "hotspots": [
        {"title": title, "text": text, "value": where}
        for title, text, where in (
            ("ELIE SAAB Maison", "Furnishings and décor from the couture house’s own Maison.", "22,56"),
            ("Waterfront views", "Residences planned with waterfront views.", "84,40"),
            ("Wrap-around decks", "Generous outdoor decks, with private jacuzzis.", "62,49"),
            ("Four bedrooms", "About 4,200–4,650 sq ft of living, in 300 residences.", "48,14"),
        )
    ],
    "community": [
        {
            "value": "A",
            "title": "Billionaire’s Block — exclusive luxury community",
            "subtitle": "170 acres · the inner circle",
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
            "subtitle": "The township around it",
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
        {"title": title, "subtitle": kind, "text": line, "link": query, "image": image, "image_alt": alt}
        for title, kind, line, query, image, alt in ROUTES
    ],
    "figures": [
        {"title": "₹3,500 cr", "text": "Combined investment, Gurugram and Noida ELIE SAAB projects"},
        {"title": "2030", "text": "Announced completion target"},
    ],
    "milestones": [
        {"title": when, "subtitle": what, "text": line, "group": state}
        for when, what, line, state in (
            ("October 2025", "RERA registered", "Registered with HRERA Gurugram: GGM/992/724/2025/95.", "done"),
            ("January 2026", "Announcement", "M3M India, Smartworld Developers and ELIE SAAB announce the residences.", "done"),

            ("Next", "Construction", "The towers rise, with the schedule set out in the agreement.", "next"),
            ("2030", "Completion target", "The completion year given at the announcement.", "next"),
        )
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
        {"title": title, "text": text, "subtitle": label, "link": url, "group": group}
        for title, text, label, url, group in (
            (
                "M3M India — official website",
                "The developer’s projects, including SCDA and its luxury corridor.",
                "Open m3mindia.com",
                "https://m3mindia.com/",
                "",
            ),
            (
                "ELIE SAAB Signature Residences — announcement",
                "Brand and interiors context, ELIE SAAB Maison and the launch details.",
                "Read on Outlook Luxe",
                "https://luxe.outlookindia.com/art-design/real-estate/m3m-india-and-smartworld-developers-launch-elie-saab-signature-residences-in-india",
                "featured",
            ),
            (
                "Launch figures — Business Today",
                "Residences, sizes, pricing and investment as reported at launch.",
                "Read on Business Today",
                "https://www.businesstoday.in/real-estate/story/m3m-eyes-rs-8300-crore-from-elie-saab-branded-residences-in-gurugram-noida-510767-2026-01-13",
                "",
            ),
            (
                "Haryana RERA",
                "Independent check of registration and statutory disclosures.",
                "Open Haryana RERA",
                "https://haryanarera.gov.in/",
                "",
            ),
        )
    ],
    "visit_modes": [
        {"title": title, "subtitle": note}
        for title, note in (
            ("Site visit", "At the experience centre"),
            ("Virtual presentation", "A live video walk-through"),
            ("At your office", "We come to you"),
        )
    ],
    "visit_purposes": [{"title": title} for title in ("My own residence", "An investment", "Both")],
    "visit_slots": [
        {"title": title, "subtitle": hours, "value": value}
        for title, hours, value in (
            ("Morning", "9 AM – 12 PM", "morning"),
            ("Afternoon", "12 – 3 PM", "afternoon"),
            ("Evening", "3 – 6 PM", "evening"),
        )
    ],
}
