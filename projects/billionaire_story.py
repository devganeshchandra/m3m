"""Copy for the research story on the Billionaire Block page (templates/projects/billionaire/story.html).

Facts follow the January 2026 M3M India / Smartworld Developers / ELIE SAAB announcement as reported by
Business Today and Outlook Luxe, and the client's research notes. Images live in static/images/billionaire/
and are AI-generated concepts or artistic impressions; alt texts say so.
"""

# (file, caption, alt)
PLAN_SLIDES = [
    ("township-aerial", "Drone view of the whole township", "Aerial view of an integrated township with towers, offices, a lake and an expressway, AI-generated concept"),
    ("branded-towers", "Branded luxury residential concept", "Three slender residential towers beside a reflecting lake at dusk, AI-generated concept"),
    ("township-concept", "Wider integrated township concept", "Mixed-use township with residences, offices, a hotel and green spines in morning mist, AI-generated concept"),
    ("enclave-drone", "The enclave from above", "Top-down view of a landscaped enclave with a lake and garden avenues, AI-generated concept"),
    ("expressway-night", "Along the Dwarka Expressway corridor", "Illuminated towers beside an expressway at blue hour, AI-generated concept"),
]

# (label, value)
ANNOUNCED_DETAILS = [
    ("Project", "Signature Residences by ELIE SAAB"),
    ("Location", "Sector 111, SCDA, Gurugram"),
    ("Residences", "300"),
    ("Configuration", "Four-bedroom residences"),
    ("Sizes", "Approx. 4,200–4,650 sq ft"),
    ("Outdoor living", "Wrap-around decks and private jacuzzis"),
    ("Views", "Waterfront views, part of the announced concept"),
    ("Design identity", "ELIE SAAB Maison furnishings and décor"),
    ("Expected completion", "2030, per the launch announcement"),
]

# (letter, title, image file, alt, points)
COMMUNITY = [
    (
        "A",
        "Billionaire’s Block — exclusive luxury community",
        "enclave-courtyard",
        "Residents walking through a shaded garden courtyard with a water channel, AI-generated concept",
        [
            "Brand-led residential identity",
            "Privacy-oriented living",
            "Large residences, expansive balconies, brand-specific interiors",
            "Lifestyle-led common spaces",
            "International design influence",
        ],
    ),
    (
        "B",
        "SCDA — integrated urban community",
        "township-boulevard",
        "Tree-lined boulevard with cafés, offices and a cycling lane at sunset, AI-generated concept",
        [
            "Luxury residential developments",
            "Grade-A office spaces",
            "High-street retail and shopping",
            "Premium hospitality",
            "Pedestrian routes, cycling paths and landscaped walkways",
        ],
    ),
]

# (title, one line, image file, alt)
AMENITIES = [
    ("Swimming pools & leisure", "Poolside spaces woven into the residences.", "amenity-pool", "Pool deck at night, representative image"),
    ("Wellness & spa", "Spaces for rest and personal well-being.", "amenity-spa", "Domed marble spa, representative image"),
    ("Fitness & health", "A fitness centre for residents.", "amenity-fitness", "Residents’ fitness centre with lake views, AI-generated concept"),
    ("Residents’ lounges", "Shared interiors in ELIE SAAB Maison style.", "amenity-lounge", "Lounge with tall bookshelves, representative image"),
    ("Landscaped outdoors", "Privacy, decks and waterfront views.", "enclave-drone-1200", "Landscaped enclave with a lake from above, AI-generated concept"),
    ("Concierge services", "Hospitality-style resident assistance.", "amenity-concierge", "Arrival court at night, representative image"),
    ("Family & children", "Dedicated children’s play areas.", "amenity-children", "Children’s studio, representative image"),
]

# (title, text, image file, alt)
STRATEGIES = [
    ("Build an enclave, not just one project", "A larger planned precinct for several branded residences.", "masterplan-model-1200", "Scale model of a master-planned township, AI-generated concept"),
    ("Bring international brands into residential design", "ELIE SAAB’s design language and Maison furnishings.", "strategy-design", "Marble, bronze and fluted stone detail, artistic impression"),
    ("Integrate homes with urban infrastructure", "Residences, offices, retail and hospitality in one township.", "township-concept-1200", "Mixed-use township in morning mist, AI-generated concept"),
    ("Position the product around a complete lifestyle", "Concierge, wellness, pools, fitness, lounges and play.", "strategy-lifestyle", "Terrace pool above the clouds at sunset, artistic impression"),
]

LEGAL_CHECKS = [
    "The project’s legal promoter and Haryana RERA registration",
    "The approved layout and sanctioned building plans",
    "The final number of towers, floors and residences",
    "The exact apartment sizes and areas in the sale",
    "The amenities written into the agreement and approved plans",
    "The construction and possession schedule",
    "Maintenance charges, clubhouse rules and running costs",
    "Whether services are in the maintenance fee or charged separately",
]

# (title, text, link label, url) — only pages that were opened and checked
SOURCES = [
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
]


def context():
    return {
        "plan_slides": PLAN_SLIDES,
        "announced_details": ANNOUNCED_DETAILS,
        "community": COMMUNITY,
        "amenities": AMENITIES,
        "strategies": STRATEGIES,
        "legal_checks": LEGAL_CHECKS,
        "sources": SOURCES,
    }
