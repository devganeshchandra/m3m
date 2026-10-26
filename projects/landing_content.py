"""Extra content for project ad landing pages (templates/projects/landing/<slug>.html), keyed by slug."""

LANDING = {
    "m3m-jacob-co-residences": {
        # Popup forms: (value, label, note, interest, project the lead is filed against)
        "popup_units": [
            ("3bhk", "3 BHK", "Residence", "residential", "m3m-jacob-co-residences"),
            ("4bhk", "4 BHK", "Residence", "residential", "m3m-jacob-co-residences"),
            ("5bhk", "5 BHK", "Residence", "residential", "m3m-jacob-co-residences"),
            ("retail", "Retail shop", "Jewel Crest", "commercial", "m3m-jacob-jewel-crest-noida"),
        ],
        # Landing header: (section id, label)
        "nav": [("residences", "Residences"), ("commercial", "Commercial"), ("amenities", "Amenities"),
                ("gallery", "Gallery"), ("location", "Location")],
        # (file in static/images/landing/jacob-co/, caption)
        "gallery": [
            ("crown-lounge", "A crown above the clouds"),
            ("balcony-golf-view", "Life, framed by nature"),
            ("lagoon-pool", "A luxurious oasis"),
            ("residence-balcony", "Views over walls"),
            ("towers-podium", "The towers and podium"),
            ("aerial-pools", "Pools and gardens from above"),
            ("tower-night", "The tower by night"),
            ("towers-blue-hour", "Blue hour"),
        ],
    },
    # No official project page exists yet: only the arrival render is official. Every other image
    # is a representative luxury interior, labelled on the page. Prices, unit counts, sizes and land area are
    # deliberately absent (listing sites disagree); they are offered in the private dossier instead.
    "m3m-trump-tower-noida": {
        "popup_units": [
            ("4bhk", "4 BHK", "Residence", "residential", "m3m-trump-tower-noida"),
            ("5bhk", "5 BHK", "Residence", "residential", "m3m-trump-tower-noida"),
        ],
        "nav": [("residences", "Residences"), ("lifestyle", "Lifestyle"), ("location", "Location"), ("faq", "FAQ")],
        # Hero slideshow: (file in static/images/landing/trump/, caption). "arrival" is the only
        # official render; the rest are representative interiors, labelled on the page.
        "slides": [
            ("arrival", "The arrival court"),
            ("salon", "Living, above the city"),
            ("pool", "An evening by the pool"),
            ("clouds", "Mornings above the clouds"),
            ("living", "Light, space and calm"),
        ],
        "residences": [("4bhk", "4 BHK"), ("5bhk", "5 BHK")],
        # Residence gallery: (file, title, line)
        "interiors": [
            ("living", "The living room", "Wide, bright and made for gathering."),
            ("dining", "The dining room", "A table for every occasion."),
            ("suite", "The principal suite", "Quiet, layered and generous."),
            ("lounge-hall", "The lounge", "Space to breathe, views to keep."),
        ],
        # Lifestyle mosaic: (file, title)
        "club": [
            ("pool", "Swimming pool"),
            ("spa", "Spa & wellness"),
            ("gym", "Fitness studio"),
            ("bar", "Residents' lounge"),
            ("cinema", "Screening room"),
            ("library", "Reading lounge"),
            ("games", "Games room"),
        ],
        # Travel times M3M states for its Sector 94 projects (The Cullinan, same sector)
        "connectivity": [
            ("2", "Amity University"),
            ("5", "Max Healthcare"),
            ("5", "Jasola Business Park"),
            ("10", "Apollo Hospital"),
            ("12", "Ansal Plaza"),
            ("12", "Radisson Blu, Sector 18"),
        ],
    },
    # Facts, captions, amenities and travel times follow m3mindia.com/residential/m3m-the-cullinan.
    "m3m-the-cullinan-residential": {
        "popup_units": [
            ("3bhk", "3 BHK", "Residence", "residential", "m3m-the-cullinan-residential"),
            ("4bhk", "4 BHK", "Residence", "residential", "m3m-the-cullinan-residential"),
            ("5bhk", "5 BHK", "Residence", "residential", "m3m-the-cullinan-residential"),
            ("retail", "Retail shop", "The Cullinan Avenue", "commercial", "m3m-the-cullinan-avenue"),
        ],
        "nav": [("residences", "Residences"), ("amenities", "Amenities"), ("commercial", "Commercial"),
                ("gallery", "Gallery"), ("location", "Location")],
        # (value, label, note) for step 1 of the lead form; "retail" routes to The Cullinan Avenue.
        "units": [
            ("3bhk", "3 BHK", "Residence"),
            ("4bhk", "4 BHK", "Residence"),
            ("5bhk", "5 BHK", "Residence"),
            ("retail", "Retail shop", "The Cullinan Avenue"),
        ],
        # Room tour: (file in static/images/landing/cullinan/, tab, title, line)
        "rooms": [
            ("living", "Living", "A symphony of elegance", "Floor-to-ceiling windows and skyline views."),
            ("dining", "Dining", "Dine in grandeur", "A dining room made for gatherings."),
            ("open-living", "Open plan", "Contemporary living masterpiece", "Open-concept design, luxury and comfort."),
            ("master-suite", "Master suite", "Contemporary master suite", "A private sanctuary with urban vistas."),
            ("lobby", "Lobby", "A grand arrival", "Marble, sculpted light and a warm welcome."),
        ],
        # Amenity filmstrip: (file, name, group)
        "amenities": [
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
        ],
        "amenity_groups": ["Wellness", "Active", "Leisure", "Outdoors", "Family"],
        # (minutes, place) as stated on the official project page
        "connectivity": [
            ("2", "Amity University"),
            ("5", "Max Healthcare"),
            ("5", "Jasola Business Park"),
            ("10", "Apollo Hospital"),
            ("12", "Ansal Plaza"),
            ("12", "Radisson Blu, Sector 18"),
        ],
        # Cinematic slider: (file, caption)
        "slides": [
            ("hero-aerial", "The Cullinan by night"),
            ("living", "A symphony of elegance"),
            ("towers-green", "Towers among the greens"),
            ("master-suite", "The master suite"),
            ("towers-day", "Sector 94, Noida Expressway"),
            ("billiards-lounge", "The billiards lounge"),
        ],
    },
}


def context_for(slug):
    return LANDING.get(slug, {})
