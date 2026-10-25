"""
Starter content for the menu pages (Projects, Our Journey, Media, Insights,
Contact). Used by `python manage.py seed_content`. Everything here can be
edited afterwards in the admin.
"""

import datetime

# Which collection each starter project appears in, and the three shown on
# the homepage. PLACEHOLDERS: confirm each project's real status in the admin.
PROJECT_STATUS = {
    "m3m-jacob-co-residences": "current",
    "m3m-jacob-jewel-crest-noida": "current",
    "m3m-the-line-retail-shops": "delivered",
    "m3m-the-line-pentsuites": "delivered",
    "m3m-the-cullinan-residential": "current",
    "m3m-the-cullinan-avenue": "current",
    "smartworld-noida-residential": "upcoming",
    "smartworld-noida-commercial": "upcoming",
    "m3m-trump-tower-noida": "current",
}
FEATURED_PROJECTS = {"m3m-jacob-co-residences", "m3m-the-cullinan-residential", "m3m-trump-tower-noida"}

MEDIA_CATEGORIES = {
    "A welcoming sense of arrival": "interiors",
    "Spaces made for gathering": "interiors",
    "Wellness, thoughtfully considered": "amenities",
    "An architectural first impression": "architecture",
    "A quieter moment by the water": "outdoors",
    "Room to move and reset": "amenities",
    "A pool framed by the city": "amenities",
    "Evenings with a point of view": "interiors",
    "Landscaped spaces to unwind": "outdoors",
    "A little more room to play": "outdoors",
    "A landmark on the skyline": "architecture",
    "An illuminated expression of design": "architecture",
    "A new perspective on the city": "architecture",
}

INNER_PAGES = [
    {
        "key": "projects",
        "banner": "dark_banners/b3.jpeg",
        "banner_alt": "Artistic impression of an M3M township at dusk",
        "eyebrow": "The M3M portfolio",
        "title": "Addresses that",
        "title_emphasis": "define a skyline.",
        "intro": (
            "Residences, retail and destinations across Noida Expressway and Central Noida, "
            "from landmarks already home to families and businesses to the next chapter on the horizon."
        ),
        "intro_label": "The collection",
        "intro_heading": "Every address, a considered point of view.",
        "intro_text": (
            "Each M3M project begins with a simple question: how should this place feel to live in, "
            "to work in, to arrive at? The answers differ from address to address, but the intent is "
            "constant: architecture that holds its own, amenities that earn their place and details "
            "that make the everyday feel a little more considered.\n\n"
            "Explore the collection by stage, from delivered landmarks to the projects available to own "
            "today and the launches still to come, or filter by residential and commercial spaces."
        ),
        "delivered_text": (
            "Completed, handed over and already part of the city's rhythm. These addresses show how an "
            "M3M project lives long after the launch."
        ),
        "current_text": (
            "Available to own today: residences and destinations where you can choose your configuration, "
            "visit the experience centre and begin a conversation with our team."
        ),
        "upcoming_text": (
            "The next chapter of the collection. Register your interest to hear first about plans, "
            "previews and launch details."
        ),
        "seo_title": "Projects in Noida | M3M India",
        "seo_description": (
            "Explore M3M India projects in Noida: delivered landmarks, residences and retail available now, "
            "and upcoming launches on Noida Expressway and Central Noida."
        ),
    },
    {
        "key": "journey",
        "banner": "dark_banners/b1.jpeg",
        "banner_alt": "Artistic impression of an M3M development rising from its plans",
        "eyebrow": "Our Journey",
        "title": "A track record.",
        "title_emphasis": "A way of thinking.",
        "intro": (
            "Since 2010, M3M India has grown around a clear belief: lasting places begin with trust, "
            "thoughtful design and a commitment to people."
        ),
        "intro_label": "Our story",
        "intro_heading": "Built on a belief that places should outlast trends.",
        "intro_text": (
            "M3M India began in 2010 with an ambition to create addresses that feel distinctive the day they "
            "are unveiled and remain relevant for decades after. That ambition has grown into a portfolio of "
            "residential, commercial and mixed-use destinations across the region.\n\n"
            "From our corporate home at M3M International Financial Center on Golf Course Road (Extn.), "
            "Gurugram, the same principles guide every project: clear communication with the people who "
            "choose us, design that earns its place, and a long view of how neighbourhoods grow.\n\n"
            "Today that thinking continues in Noida, where a growing collection of residences and "
            "destinations along Noida Expressway and in Central Noida is shaping a new view of the city."
        ),
        "quote_text": "Lasting places begin with trust, thoughtful design and a commitment to people.",
        "quote_attribution": "The M3M philosophy",
        "seo_title": "Our Journey | M3M India",
        "seo_description": (
            "The M3M India story since 2010: our values, our track record and the thinking behind every address."
        ),
    },
    {
        "key": "media",
        "banner": "media/m7.jpeg",
        "banner_alt": "Artistic impression of an indoor pool at an M3M residence",
        "eyebrow": "Media centre",
        "title": "Spaces made",
        "title_emphasis": "to be experienced.",
        "intro": (
            "A closer look at the architecture, interiors and amenities that shape the M3M point of view, "
            "together with recent coverage in the press."
        ),
        "intro_label": "The gallery",
        "intro_heading": "Arrival, gathering, wellness, skyline.",
        "intro_text": (
            "Browse the moments that define an M3M address, from the first impression at the entrance to "
            "the quiet corners residents return to every day. Images are artistic impressions and are "
            "indicative only."
        ),
        "seo_title": "Media Centre: Gallery, Videos & Press | M3M India",
        "seo_description": "Image gallery, videos and press coverage of M3M India projects and news.",
    },
    {
        "key": "insights",
        "banner": "media/m8.jpeg",
        "banner_alt": "Artistic impression of a residents' lounge at dusk",
        "eyebrow": "Ideas & perspectives",
        "title": "Insights",
        "title_emphasis": "from M3M.",
        "intro": (
            "Ideas, buyer guides and city stories behind each address: considered reading for anyone "
            "exploring their next home or investment."
        ),
        "intro_label": "The journal",
        "intro_heading": "Read, reflect, then decide.",
        "intro_text": "",
        "seo_title": "Insights: Real Estate Guides & Ideas | M3M India",
        "seo_description": (
            "Articles from M3M India on design, wellness, Noida and practical guides for home buyers."
        ),
    },
    {
        "key": "contact",
        "banner": "media/m4.jpeg",
        "banner_alt": "Artistic impression of the arrival at an M3M development",
        "eyebrow": "We’re here to help",
        "title": "Let’s find",
        "title_emphasis": "your next address.",
        "intro": (
            "Speak with our team about a project, arrange a site visit or ask us anything. Choose the way "
            "that suits you best."
        ),
        "intro_label": "Get in touch",
        "intro_heading": "A personal conversation, at your pace.",
        "intro_text": (
            "Share a few details and a convenient time, and a member of our team will call you. Prefer to "
            "talk now? Call us toll-free or message us on WhatsApp."
        ),
        "seo_title": "Contact Us | M3M India",
        "seo_description": (
            "Contact M3M India: call toll-free 1800 123 3333, WhatsApp our team, or request a call back. "
            "Corporate office at M3M International Financial Center, Gurugram."
        ),
    },
]

MILESTONES = [
    (
        "2010",
        "The beginning",
        "M3M India is founded with a belief that lasting places begin with trust, thoughtful design and a "
        "commitment to people.",
    ),
    (
        "Gurugram",
        "A corporate home on Golf Course Road (Extn.)",
        "M3M International Financial Center, Sector-66, becomes the base from which the portfolio is shaped.",
    ),
    (
        "Noida",
        "A new view of Noida",
        "A growing collection of residences and destinations takes shape across Noida Expressway and "
        "Central Noida.",
    ),
    (
        "Today",
        "66 projects in the portfolio, 43 completed",
        "Company figures as stated on the M3M India website, and a collection that continues to grow.",
    ),
]

FAQS = [
    (
        "How soon will someone contact me?",
        "Our team calls you in the time window you choose on the form. If you need to talk sooner, call "
        "us toll-free or message us on WhatsApp.",
    ),
    (
        "Can I arrange a site visit?",
        "Yes. Mention the project you’re interested in and our team will help you plan a visit at a "
        "convenient time.",
    ),
    (
        "I live outside India. Can I still enquire?",
        "Of course. Enter your number with its country code (for example +44 or +971) and choose “Overseas "
        "(NRI)” where asked. We can also continue the conversation on WhatsApp.",
    ),
    (
        "Where can I check a project’s RERA registration?",
        "Each project page lists its RERA registration number. You can verify it on the website of the "
        "Uttar Pradesh Real Estate Regulatory Authority (UP RERA).",
    ),
    (
        "How are my details used?",
        "Your details are used only to respond to your enquiry. You can ask us to stop contacting you at "
        "any time.",
    ),
]

INSIGHT_ARTICLES = [
    {
        "title": "Wellness woven into the everyday",
        "slug": "wellness-woven-into-the-everyday",
        "category": "Thoughtful living",
        "image": "media/m3.jpeg",
        "published_on": datetime.date(2026, 10, 6),
        "is_featured": True,
        "description": "Spaces to pause, reset and make time for the moments that matter.",
        "body": """Wellness at home is rarely about a single amenity. It is the sum of small decisions: how much daylight reaches a room in the morning, how quiet a corridor feels in the evening, how easily you can step outside and breathe.

## Designing for routine, not occasion

The most valuable wellness spaces are the ones you use without thinking about it. A fitness studio a lift ride away, a landscaped walk that makes a short stroll part of the day, a pool that invites a swim before work rather than only on weekends. When these spaces sit naturally along your daily route, they stop being features and become habits.

## Light, air and a sense of calm

Generous glazing, cross-ventilation and considered acoustics shape how a home feels far more than any single finish. Rooms that receive natural light at the right times of day, and bedrooms that stay quiet at night, contribute quietly to better rest and clearer mornings.

## Room to connect

Wellbeing is social as much as physical. Lounges, shared gardens and spaces for children to play give residents a reason to meet, and a neighbourhood a reason to feel like a community.

When you visit a project, look beyond the amenity list. Ask how the spaces connect, when the light arrives and where you would actually spend your time. The best answers are usually found in the everyday.""",
    },
    {
        "title": "A new view of Noida",
        "slug": "a-new-view-of-noida",
        "category": "City perspective",
        "image": "media/m8.jpeg",
        "published_on": datetime.date(2026, 9, 22),
        "description": "Discover addresses shaped by the energy and possibilities of the city.",
        "body": """Noida has steadily grown from a planned satellite of Delhi into a city with its own rhythm: business districts, retail destinations, green belts and a growing collection of considered residential addresses.

## Noida Expressway

The Noida–Greater Noida Expressway has become one of the city’s defining corridors. Sectors along it combine wide roads, access to Delhi and Greater Noida, and room for larger, master-planned developments with landscaped open spaces.

## Central Noida

Closer to the city’s established neighbourhoods, Central Noida offers a different appeal: proximity to offices, schools and everyday conveniences, and destinations where living, retail and dining sit side by side.

## Choosing your part of the city

The right address depends on how you live. Consider your daily commute, the schools and hospitals that matter to your family, and whether you prefer the energy of a mixed-use destination or the calm of a residential enclave. Visiting at different times of day, during the morning rush and on a quiet weekend, often reveals more than any map.

Noida’s story is still being written, and each new address adds a chapter.""",
    },
    {
        "title": "The details that define an address",
        "slug": "the-details-that-define-an-address",
        "category": "Design & detail",
        "image": "media/m13.jpeg",
        "published_on": datetime.date(2026, 9, 8),
        "description": "From arrival to the everyday, thoughtful design leaves its mark.",
        "body": """First impressions are formed in seconds: the approach, the entrance, the moment a door opens onto a lobby. But an address earns its reputation over years, in the details residents notice every day.

## The arrival

A well-designed arrival slows you down in the best way. A drop-off that feels unhurried, a lobby with natural light and a clear sense of welcome all set the tone before you reach your front door.

## Materials that age well

Finishes chosen for how they will look in ten years, not only on handover day, make a lasting difference. Natural stone, quality fittings and durable surfaces in shared spaces keep an address feeling cared for.

## The quiet engineering

Some of the most important details are the ones you never see: acoustic separation between homes, efficient lifts, thoughtful service areas and well-planned parking. When they work, daily life simply feels easier.

## Designed for people

Ultimately, good detail is about people: handrails at the right height, seating where you might pause, lighting that guides without glaring. When you next walk through a project, notice how it makes you feel. That feeling is the design at work.""",
    },
    {
        "title": "Reading a RERA registration: a buyer’s checklist",
        "slug": "reading-a-rera-registration-a-buyers-checklist",
        "category": "Buyer’s guide",
        "image": "media/m11.jpeg",
        "published_on": datetime.date(2026, 8, 25),
        "description": "What a project’s RERA registration tells you, and what to check before you decide.",
        "body": """Under the Real Estate (Regulation and Development) Act, 2016, most residential and commercial projects must be registered with the state’s real estate regulatory authority before they are marketed. In Uttar Pradesh, that is UP RERA. A project’s registration number is your starting point for informed due diligence.

## Find the registration

Every project page on this website lists its RERA number. Search for it on the UP RERA website to see the official project record.

## What to review

Check that the promoter’s name and the project name match what you have been shown. Review the approved plans, the declared completion timeline and the land and approval details in the registration. Where available, look at the project’s periodic progress updates.

## Understand carpet area

RERA defines carpet area as the net usable floor area of an apartment, excluding external walls, service shafts and exclusive balconies or terraces, but including internal partition walls. Comparing homes on carpet area gives you a like-for-like view.

## Keep your documents

Keep copies of the allotment letter, the agreement for sale and every payment receipt. Read the agreement carefully, and seek independent legal advice if anything is unclear.

This checklist is general information, not legal advice. Our team is happy to walk you through the registration details for any M3M project.""",
    },
    {
        "title": "Making the most of a site visit",
        "slug": "making-the-most-of-a-site-visit",
        "category": "Buyer’s guide",
        "image": "media/m1.jpeg",
        "published_on": datetime.date(2026, 8, 11),
        "description": "A short guide to what to look for, and what to ask, when you visit a project.",
        "body": """Brochures and renders tell you what a project intends to be. A site visit tells you how it feels. A little preparation helps you come away with the answers that matter.

## Before you go

Shortlist the configurations that suit you and note the questions you want answered: sizes, orientation, timelines and payment plans. If you can, plan to visit the location at the time of day you would usually commute.

## At the experience centre

Sample apartments help you judge proportions. Notice ceiling heights, window sizes, storage and how rooms connect. Ask which specifications are standard and which are shown as options.

## Around the site

Walk the approach roads and look at the neighbourhood: schools, hospitals, markets and green spaces. Notice noise levels and how easy it is to get in and out at busy times.

## Questions worth asking

Which tower and floor would suit your preferred view and light? What is the declared completion timeline in the RERA registration? Which amenities will be ready at handover?

Take photos and notes. Comparing visits side by side, a few days later, often makes the decision clearer.""",
    },
    {
        "title": "Residential or commercial: framing the decision",
        "slug": "residential-or-commercial-framing-the-decision",
        "category": "Perspective",
        "image": "media/m10.jpeg",
        "published_on": datetime.date(2026, 7, 28),
        "description": "Questions to help you think through whether a home or a commercial space fits your goals.",
        "body": """Whether you are buying a home, a retail space or a serviced apartment, the right choice starts with a clear sense of what you want the property to do for you.

## Start with purpose

A home is first a place to live: proximity to work, schools and family usually matter most. A commercial space is chosen for its location, visibility and the kind of footfall it attracts. A serviced apartment sits between the two, valued for convenience and management.

## Consider your time horizon

How long do you plan to hold the property, and how involved do you want to be? Some spaces suit owners who will use them every day; others suit those who prefer a hands-off arrangement.

## Look closely at the destination

For commercial spaces especially, the surrounding mix matters: neighbouring brands, dining, entertainment and access. For homes, look at open space, amenities and community.

## Ask for clarity

Review sizes, specifications, timelines and every cost involved. Read the agreement carefully.

This article is general information, not financial or legal advice. Speak with an independent adviser about your own situation, and with our team about any M3M project you are considering.""",
    },
]

# Billionaire Block page. Images are artistic impressions in seed/images/billionaire_block/.
# PLACEHOLDERS: every figure, size, distance and amenity below is indicative. Confirm each one
# against the final project brief in the admin before the page goes live.
BILLIONAIRE_BLOCK_FILES = {
    "hero_video": "billionaire_block/hero.mp4",
    "hero_image": "home_banners/towers-above-clouds.jpg",
    "architecture_image": "billionaire_block/twin-towers-sunset.jpg",
    "about_image": "billionaire_block/aerial-masterplan.jpg",
    "about_image_2": "billionaire_block/towers-blue-hour.jpg",
    "building_image": "billionaire_block/towers-day.jpg",
    "building_image_2": "billionaire_block/salon.jpg",
    "security_image": "billionaire_block/podium-facade.jpg",
    "specs_image": "billionaire_block/materials.jpg",
}

# (name, tagline, size, configuration, features, image, image alt)
BILLIONAIRE_RESIDENCES = [
    (
        "Signature Residences",
        "Single-floor homes, open to the sky on four sides.",
        "10,000 – 12,500 sq ft",
        "4 & 5 bedrooms with staff quarters",
        "Private lift opening into the foyer\n"
        "Four-side open, with views in every direction\n"
        "Formal and family living wings\n"
        "Wraparound sky deck",
        "billionaire_block/salon.jpg",
        "Signature Residence living salon at dusk",
    ),
    (
        "Sky Villas",
        "Duplex homes with double-height living and a private pool deck.",
        "14,000 – 16,000 sq ft",
        "5 bedrooms across two floors, with staff quarters",
        "Double-height salon with a sculptural staircase\n"
        "Private pool deck and garden terrace\n"
        "Principal suite occupying its own wing\n"
        "Show kitchen and separate chef’s kitchen",
        "billionaire_block/sky-villa.jpg",
        "Sky Villa double-height living room with a floating staircase",
    ),
    (
        "The Penthouse",
        "One home at the summit. Nothing above it but sky.",
        "25,000+ sq ft",
        "Bespoke triplex with rooftop pavilion",
        "Rooftop infinity pool and glass pavilion\n"
        "Private screening room and wine cellar\n"
        "Personal spa with steam and massage suite\n"
        "Interiors finished to the owner’s brief",
        "billionaire_block/penthouse.jpg",
        "Penthouse rooftop pool above a sea of clouds",
    ),
]

# (section, title, value, text, image, image alt)
BILLIONAIRE_ITEMS = [
    # Key numbers: value is the figure, text is the unit shown beside it.
    ("stat", "Residences in the collection", "48", "", "", ""),
    ("stat", "Area of each residence", "12,000+", "sq ft", "", ""),
    ("stat", "Ceiling height", "14", "ft", "", ""),
    ("stat", "Private residents’ club", "1,00,000", "sq ft", "", ""),
    # Residence features
    ("feature", "Private elevator into the residence", "", "The lift opens only into your own foyer, never onto a corridor.", "", ""),
    ("feature", "Four-side open", "", "Light, air and views on every side of the home.", "", ""),
    ("feature", "14 ft ceilings", "", "Volumes proportioned for art, chandeliers and calm.", "", ""),
    ("feature", "Italian marble", "", "Book-matched slabs, selected block by block at the quarry.", "", ""),
    ("feature", "Home automation", "", "Light, climate, shading and security from a single panel.", "", ""),
    ("feature", "Private pool decks", "", "Plunge pools and sun decks in select residences.", "", ""),
    ("feature", "Staff quarters with service entry", "", "A separate service lift and entrance for the household team.", "", ""),
    ("feature", "VRV with fresh-air system", "", "Quiet, zoned climate control with filtered fresh air.", "", ""),
    ("feature", "Private wine cellar", "", "A temperature-controlled cellar within the residence.", "", ""),
    # The club
    ("club", "Infinity pool", "", "A heated pool with an edge that meets the sky.", "billionaire_block/sky-pool.jpg", "Infinity pool above the city at night"),
    ("club", "Spa & hammam", "", "Marble hammam, steam, sauna and treatment suites.", "billionaire_block/spa.jpg", "Domed marble hammam with soft steam"),
    ("club", "Cigar lounge", "", "Leather, walnut and a walk-in humidor.", "billionaire_block/cigar-lounge.jpg", "Cigar lounge with leather club chairs and a humidor"),
    ("club", "Whisky bar", "", "Rare single malts behind a backlit onyx bar.", "billionaire_block/whisky-bar.jpg", "Whisky bar with a backlit onyx counter"),
    ("club", "Private dining", "", "A table for twelve, served by the club’s chefs.", "billionaire_block/private-dining.jpg", "Private dining room set for twelve"),
    ("club", "Padel & squash", "", "Glass-walled courts with coaching on request.", "billionaire_block/padel.jpg", "Indoor padel court with glass walls"),
    ("club", "Golf simulator", "", "The world’s great courses, in every season.", "billionaire_block/golf-simulator.jpg", "Golf simulator suite with leather chairs"),
    ("club", "Private cinema", "", "Twelve reclining seats and reference-grade sound.", "billionaire_block/cinema.jpg", "Private screening room with velvet recliners"),
    ("club", "Art gallery", "", "A curated, rotating collection for residents.", "billionaire_block/lift-lobby.jpg", "Sculpture on a plinth before a backlit onyx wall"),
    ("club", "Library", "", "Double-height shelves and quiet reading rooms.", "billionaire_block/library.jpg", "Library with double-height oak shelves"),
    ("club", "Kids’ academy", "", "Supervised studios for play, art and learning.", "billionaire_block/kids-academy.jpg", "Children’s studio with a climbing wall and easels"),
    # Lifestyle services
    ("service", "24×7 concierge", "", "One call for anything, at any hour.", "", ""),
    ("service", "Chauffeur & valet", "", "Your car is ready before you reach the lobby.", "", ""),
    ("service", "In-residence dining", "", "The club’s chefs cook in your home on request.", "", ""),
    ("service", "Housekeeping", "", "Discreet daily care by a trained residence team.", "", ""),
    ("service", "Wellness doctor", "", "A resident physician for consultations at home.", "", ""),
    ("service", "Personal trainer", "", "Programmes built around your schedule.", "", ""),
    ("service", "Car detailing", "", "Your collection, cared for in the basement atelier.", "", ""),
    ("service", "Pet care", "", "Grooming, walking and care when you travel.", "", ""),
    # Privacy & security
    ("security", "Private lift lobbies", "", "No shared corridors. Your lift arrives only at your door.", "", ""),
    ("security", "One or two residences per floor", "", "Neighbours you choose to meet, not ones you pass.", "", ""),
    ("security", "Biometric & facial recognition", "", "Access that knows residents, staff and expected guests.", "", ""),
    ("security", "Private porte-cochère per tower", "", "Every tower has its own covered, discreet arrival.", "", ""),
    ("security", "Helipad", "", "For arrivals that cannot wait for traffic.", "", ""),
    # Location: value is the indicative travel time.
    ("location", "Golf Course Road", "2 min", "", "", ""),
    ("location", "DLF Cyber City", "15 min", "", "", ""),
    ("location", "Indira Gandhi International Airport", "35 min", "", "", ""),
    ("location", "Leading international schools", "10 min", "", "", ""),
    ("location", "Medanta & Fortis hospitals", "15 min", "", "", ""),
    ("location", "DLF Golf & Country Club", "10 min", "", "", ""),
    # Gallery
    ("gallery", "The enclave from above", "", "", "billionaire_block/aerial-masterplan.jpg", "Aerial view of a green enclave with lakes, golf greens and villas"),
    ("gallery", "The towers above the clouds", "", "", "billionaire_block/sky-towers.jpg", "Sculptural towers rising above the clouds"),
    ("gallery", "Sky Villa salon", "", "", "billionaire_block/sky-villa.jpg", "Double-height Sky Villa salon"),
    ("gallery", "The retail podium", "", "", "billionaire_block/podium-facade.jpg", "Daylight façade of the retail podium with a sculpted canopy"),
    ("gallery", "Penthouse terrace", "", "", "billionaire_block/penthouse.jpg", "Penthouse pool above the clouds"),
    ("gallery", "Twin towers at sunset", "", "", "billionaire_block/twin-towers-sunset.jpg", "Twin residential towers at sunset"),
    ("gallery", "The towers by day", "", "", "billionaire_block/towers-day.jpg", "Residential towers and landscaped podium by day"),
    ("gallery", "Principal suite", "", "", "billionaire_block/suite.jpg", "Principal suite at golden hour"),
    ("gallery", "The towers at blue hour", "", "", "billionaire_block/towers-blue-hour.jpg", "Residential towers and retail podium at blue hour"),
    ("gallery", "The towers by night", "", "", "billionaire_block/towers-night.jpg", "Residential towers lit at night beside the expressway"),
    # Specifications
    ("spec", "Flooring", "", "Book-matched Italian marble in living and dining areas. Engineered oak in bedrooms. Natural stone on terraces and pool decks.", "", ""),
    ("spec", "Kitchen", "", "Show kitchen with stone island and integrated appliances by leading European makers. Separate chef’s kitchen with commercial-grade equipment, cold room and pantry.", "", ""),
    ("spec", "Bathrooms", "", "Marble-clad walls and floors, freestanding stone baths, rain showers, heated floors and designer sanitaryware with brushed-bronze fittings.", "", ""),
    ("spec", "Doors", "", "Full-height veneered doors with concealed frames and bespoke bronze hardware. Main entrance door with biometric lock.", "", ""),
    ("spec", "Windows", "", "Floor-to-ceiling double-glazed, acoustic and thermally insulated glazing in slim aluminium frames, with motorised sheers and blackout blinds.", "", ""),
    ("spec", "Smart home", "", "Integrated control of lighting scenes, climate, shading, audio-visual and security, from wall panels and mobile devices.", "", ""),
    ("spec", "Air conditioning", "", "VRV system with individual room control and a central fresh-air system with filtration and humidity control.", "", ""),
    # Amenities: items with an image appear as photos, the rest only in the list beside them.
    ("amenity_indoor", "Boxing ring", "", "", "billionaire_block/amenity-boxing-ring.jpg", "Two boxers sparring in a boxing ring"),
    ("amenity_indoor", "Bowling alley", "", "", "billionaire_block/amenity-bowling-alley.jpg", "Bowling lane with a red ball before the pins"),
    ("amenity_indoor", "Mini theatre", "", "", "billionaire_block/amenity-mini-theatre.jpg", "Mini theatre with red and black seats facing the screen"),
    ("amenity_indoor", "CrossFit gym", "", "", "billionaire_block/amenity-crossfit-gym.jpg", "Woman training with battle ropes in a gym"),
    ("amenity_indoor", "Library", "", "", "billionaire_block/amenity-library.jpg", "Library lounge with armchairs beside tall bookshelves"),
    ("amenity_indoor", "E-sports room", "", "", "", ""),
    ("amenity_indoor", "Business centre", "", "", "", ""),
    ("amenity_indoor", "Indoor games room", "", "", "", ""),
    ("amenity_wellness", "Swimming pool", "", "", "billionaire_block/amenity-swimming-pool.jpg", "Swimmers in a landscaped pool below the towers"),
    ("amenity_wellness", "Cricket practice pitch", "", "", "billionaire_block/amenity-cricket-pitch.jpg", "Batsman in the nets of a cricket practice pitch"),
    ("amenity_wellness", "Golf putting", "", "", "billionaire_block/amenity-golf-putting.jpg", "Golfer on a putting green with sand bunkers"),
    ("amenity_wellness", "Yoga & aerobic deck", "", "", "billionaire_block/amenity-yoga-deck.jpg", "Two women meditating on an open-air yoga deck"),
    ("amenity_wellness", "Cycle track", "", "", "", ""),
    ("amenity_wellness", "Jogging track", "", "", "", ""),
    ("amenity_wellness", "Trampoline park", "", "", "", ""),
    ("amenity_wellness", "Fitness station", "", "", "", ""),
    ("amenity_wellness", "Ping-pong area", "", "", "", ""),
    ("amenity_leisure", "Jungle gym, sand pit & musical garden", "", "", "billionaire_block/amenity-jungle-gym.jpg", "Aerial view of a children’s play garden with a jungle gym and sand pit"),
    ("amenity_leisure", "Seating alcove", "", "", "billionaire_block/amenity-seating-alcove.jpg", "Shaded seating alcove under a timber canopy in the gardens"),
    ("amenity_leisure", "Swimming pool & meditation deck", "", "", "billionaire_block/amenity-meditation-deck.jpg", "Aerial view of a curved pool beside a meditation deck at dusk"),
    ("amenity_leisure", "Festival lawn", "", "", "", ""),
    ("amenity_leisure", "Walking trail", "", "", "", ""),
    ("amenity_leisure", "Tree house with bird-watching deck", "", "", "", ""),
    ("amenity_leisure", "Reading garden", "", "", "", ""),
    ("amenity_leisure", "Frisbee zone", "", "", "", ""),
    ("amenity_leisure", "Picnic & barbecue area", "", "", "", ""),
    ("amenity_leisure", "Pets’ park", "", "", "", ""),
    ("amenity_leisure", "Circles of joy", "", "", "", ""),
    ("amenity_leisure", "Resting pavilion", "", "", "", ""),
    ("amenity_leisure", "Sunrise & sunset deck", "", "", "", ""),
    ("amenity_leisure", "Bonfire court", "", "", "", ""),
    ("gallery", "The living room", "", "", "billionaire_block/living-room.jpg", "Woman reading by full-height glass doors in a sunlit living room"),
    ("gallery", "Infinity pool deck", "", "", "billionaire_block/infinity-pool-deck.jpg", "Woman walking beside an infinity pool above a forested valley"),
    ("gallery", "Private terrace", "", "", "billionaire_block/private-terrace.jpg", "Woman on a glass-railed terrace overlooking green hills"),
]

# News about the Billionaire's Block, summarised from the published articles (checked 24 Oct 2026).
# (tag, title, publication, date, summary, body, key points, url, paid press release)
BILLIONAIRE_NEWS = [
    (
        "Partnership",
        "M3M partners ELIE SAAB on ₹3,500 crore of branded residences",
        "PTI via The Week",
        datetime.date(2026, 1, 13),
        "Two ultra-luxury projects for Delhi-NCR: 300 Signature Residences in Gurugram and about 650 homes in Noida.",
        "M3M India has partnered with the global fashion and lifestyle house ELIE SAAB to build two ultra-luxury "
        "residential projects in Delhi-NCR, with a combined investment of ₹3,500 crore, PTI reported.\n\n"
        "In Gurugram, M3M India will build 300 apartments on Dwarka Expressway, branded Signature Residences by "
        "ELIE SAAB, with about 1.3 million sq ft of built area and an investment of around ₹2,000 crore. In Noida, "
        "group firm Smartworld Developers will build about 650 units.\n\n"
        "“We have partnered ELIE SAAB for two branded residential projects in Delhi-NCR,” said M3M India promoter "
        "Pankaj Bansal.",
        "₹3,500 crore combined investment\n"
        "300 residences in Gurugram, on Dwarka Expressway\n"
        "About 1.3 million sq ft of built area in Gurugram\n"
        "About 650 units in Noida by Smartworld Developers",
        "https://www.theweek.in/wire-updates/business/2026/01/13/m3m-to-invest-rs-3-500-cr-to-build-elie-saab-branded-housing-projects-in-ncr.html",
        False,
    ),
    (
        "Pricing",
        "Gurugram residences priced from about ₹15 crore",
        "Business Today",
        datetime.date(2026, 1, 13),
        "Four-bedroom homes of 4,200 to 4,650 sq ft in Sector 111, Dwarka Expressway, at ₹37,000 per sq ft.",
        "Business Today reports that M3M expects ₹8,300 crore in revenue from its ELIE SAAB-branded residences in "
        "Gurugram and Noida.\n\n"
        "The Gurugram project, in Sector 111 on Dwarka Expressway, has 300 four-bedroom residences of 4,200 to "
        "4,650 sq ft. Pankaj Bansal, Promoter of M3M India and Founder of Smartworld Developers, said the starting "
        "price is about ₹15 crore, at ₹37,000 per sq ft.\n\n"
        "The Gurugram investment is ₹2,000 crore, including land and construction, with a revenue potential of "
        "₹4,700 crore.",
        "Starting price of about ₹15 crore\n"
        "Four bedrooms, 4,200 to 4,650 sq ft\n"
        "₹37,000 per sq ft\n"
        "₹4,700 crore revenue potential in Gurugram",
        "https://www.businesstoday.in/real-estate/story/m3m-eyes-rs-8300-crore-from-elie-saab-branded-residences-in-gurugram-noida-510767-2026-01-13",
        False,
    ),
    (
        "Launch",
        "ELIE SAAB Signature Residences unveiled at the Billionaire’s Block",
        "Outlook Luxe",
        datetime.date(2026, 1, 15),
        "The first branded address in a 170-acre enclave planned for a select group of global luxury names, due in 2030.",
        "Outlook Luxe describes the Billionaire’s Block as a 170-acre enclave within Smart City Delhi Airport, "
        "Sector 111, “a carefully curated enclave designed to host a select group of globally renowned branded "
        "residences”.\n\n"
        "The Signature Residences by ELIE SAAB are its first address: 300 four-bedroom homes with generous "
        "floor-to-ceiling heights, waterfront views and outdoor living areas with private jacuzzis. The interiors "
        "are a creative collaboration with designer Carlo Colombo, with furniture and décor from the ELIE SAAB "
        "Maison collection, crafted in Italy.\n\n"
        "Shared amenities include concierge services, a spa, swimming pools, fitness centres and residents’ "
        "lounges. Completion is scheduled for 2030.",
        "170-acre Billionaire’s Block enclave\n"
        "Interiors in collaboration with Carlo Colombo\n"
        "ELIE SAAB Maison furniture, crafted in Italy\n"
        "Completion scheduled for 2030",
        "https://luxe.outlookindia.com/art-design/real-estate/m3m-india-and-smartworld-developers-launch-elie-saab-signature-residences-in-india",
        False,
    ),
    (
        "Recognition",
        "Billionaires’ Block wins a master development award",
        "ANI via LatestLY",
        datetime.date(2026, 7, 17),
        "Named Unique Branded Residences’ Master Development at the India Property Awards 2026.",
        "M3M’s Billionaires’ Block received the Unique Branded Residences’ Master Development Award at the India "
        "Property Awards 2026, according to a press release distributed by ANI on 17 July 2026.\n\n"
        "The release describes the development as an integrated branded destination that brings together "
        "architecture, public spaces, wellness, hospitality and resident services, and names Roseate as a "
        "hospitality partner.",
        "India Property Awards 2026\n"
        "Unique Branded Residences’ Master Development Award\n"
        "Roseate named as hospitality partner",
        "https://www.latestly.com/agency-news/business-news-m3ms-billionaires-block-wins-unique-branded-residences-master-development-award-at-the-india-property-awards-2026-7520457.html",
        True,
    ),
]
