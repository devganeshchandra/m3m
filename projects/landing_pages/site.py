"""Website texts shared across the main site: header, footer, the enquiry popup and the small headings,
buttons and notes on the menu pages that have no admin screen of their own.

Templates read them as st.<key> (core.context_processors.website_texts). Each section names the page or part
of the page the texts appear on, so the content team can find them from what they see on the website.
"""

SLUG = "website-texts"
NAME = "Website texts (header, footer, popup & page headings)"
STATIC_DIR = "images/"

SEO = {}

HEADER = "01. Header, footer & floating buttons (every page)"
POPUP = "02. Enquiry popup (every page)"
CTA = "03. “Let’s find your next address” band (menu pages)"
FORMS = "04. Banner enquiry forms (homepage and menu pages)"
HOME = "05. Homepage: buttons & small labels"
PROJECTS = "06. Projects page & project cards"
PROJECT = "07. Standard project pages (projects without an ad landing page)"
JOURNEY = "08. Our Journey page"
MEDIA = "09. Media Centre page"
INSIGHTS = "10. Insights pages"
CONTACT = "11. Contact page"
NOT_FOUND = "12. Page not found (404)"

TEXTS = [
    (HEADER, "header_cta", "Header: gold button", "Private consultation"),
    (HEADER, "header_all_projects", "Header: last link in the Projects menu", "View all projects →"),
    (HEADER, "footer_office", "Footer: address heading", "Corporate office"),
    (HEADER, "footer_explore", "Footer: links heading", "Explore"),
    (HEADER, "footer_connect", "Footer: contact heading", "Connect"),
    (HEADER, "footer_whatsapp", "Footer: WhatsApp link", "WhatsApp"),
    (HEADER, "footer_call", "Footer: call link", "Call M3M"),
    (HEADER, "footer_legal", "Footer: disclaimer heading", "Important information"),
    (HEADER, "footer_rights", "Footer: after the year and site name", "All rights reserved."),
    (HEADER, "float_call", "Phones: bottom bar, call", "Call"),
    (HEADER, "float_whatsapp", "Phones: bottom bar, WhatsApp", "WhatsApp"),
    (HEADER, "float_enquire", "Phones: bottom bar, enquire", "Enquire"),
    (POPUP, "popup_label", "Picture side: small label", "M3M India · Private consultation"),
    (POPUP, "popup_side_title", "Picture side: title", "A considered address."),
    (POPUP, "popup_side_text", "Picture side: line", "Begin with a conversation. Explore at your own pace."),
    (POPUP, "popup_title", "Title", "Enquire now"),
    (POPUP, "popup_intro", "Intro (the project name follows it)",
     "Share your details and preferred call time to begin a conversation about"),
    (POPUP, "popup_any_project", "Project name when opened from a general button", "M3M residences"),
    (POPUP, "popup_point_1", "First point", "Personal project guidance"),
    (POPUP, "popup_point_2", "Second point", "Choose a convenient call window"),
    (POPUP, "popup_consent", "Consent tick box",
     "I agree to be contacted by M3M India about this enquiry. My details will not be used for unrelated marketing."),
    (POPUP, "popup_button", "Send button", "Request a private call / virtual tour"),
    (POPUP, "popup_help", "Line before the phone and WhatsApp links", "For immediate assistance"),
    (POPUP, "popup_call", "Call link (the number follows it)", "Call"),
    (POPUP, "popup_whatsapp", "WhatsApp link", "WhatsApp our team"),
    (CTA, "cta_label", "Small label", "Private consultation"),
    (CTA, "cta_title", "Heading", "Let’s find *your next address.*"),
    (CTA, "cta_text", "Text",
     "Speak with our team about any M3M project, from configurations and pricing to a personal site visit."),
    (CTA, "cta_button", "Gold button", "Request a callback"),
    (CTA, "cta_whatsapp", "WhatsApp button", "WhatsApp our team"),
    (CTA, "cta_call", "Line before the phone number", "or call toll-free"),
    (FORMS, "home_form_label", "Homepage banner form: small label", "A more personal conversation"),
    (FORMS, "home_form_button", "Homepage banner form: button", "Request a private call / virtual tour"),
    (FORMS, "banner_form_label", "Menu page banner form: small label", "Personal guidance"),
    (FORMS, "banner_form_interest", "Menu page banner form: residential or commercial question", "Interested in"),
    (FORMS, "banner_form_button", "Menu page banner form: button", "Send me the details"),
    (FORMS, "form_note", "Note under both forms", "Your details are used only to respond to this enquiry."),
    (HOME, "home_projects_link", "Projects: link beside the heading", "Explore the collection"),
    (HOME, "home_projects_all", "Projects: button under the cards ({count} = the number of projects)",
     "Explore all {count} projects"),
    (HOME, "home_bb_caption", "Billionaire Block band: picture caption", "Artistic impression"),
    (HOME, "home_bb_link", "Billionaire Block band: link", "Request a private viewing"),
    (HOME, "home_glance", "Our Journey: figures heading", "M3M India at a glance"),
    (HOME, "home_journey_source", "Our Journey: source link", "M3M India website"),
    (HOME, "home_news_link", "In the news: button", "All press coverage"),
    (HOME, "home_media_link", "Media: button", "Explore the full gallery"),
    (HOME, "home_insights_link", "Insights: button", "Read all insights"),
    (HOME, "guided_step_1", "Project finder: step 1", "I’m looking for"),
    (HOME, "guided_step_2", "Project finder: step 2", "Pick an address"),
    (HOME, "guided_step_3", "Project finder: step 3", "I’m based in"),
    (HOME, "guided_step_4", "Project finder: step 4", "Where should we send it?"),
    (HOME, "guided_button", "Project finder: button", "Send me my M3M edit"),
    (HOME, "guided_note", "Project finder: note", "No account. No commitment. Used only for this request."),
    (HOME, "home_contact_link", "Contact: button", "All contact details"),
    (HOME, "home_call_label", "Contact: phone label", "Call us"),
    (HOME, "home_call_note", "Contact: line under the number (the site name follows it)", "Toll-free ·"),
    (HOME, "home_visit_label", "Contact: address label", "Visit us"),
    (HOME, "home_whatsapp", "Contact: WhatsApp link", "Continue the conversation on WhatsApp"),
    (PROJECTS, "card_details", "Project card: details button", "View details"),
    (PROJECTS, "card_enquire", "Project card: enquiry button", "Enquire now"),
    (PROJECTS, "card_register", "Project card: enquiry button for upcoming projects", "Register interest"),
    (PROJECTS, "list_empty_filter", "Projects page: when a filter finds nothing",
     "No addresses of this type in this collection yet."),
    (PROJECTS, "list_empty", "Projects page: a collection with no projects yet",
     "New addresses for this collection will be announced soon."),
    (PROJECTS, "list_register", "Projects page: button under an empty collection", "Register your interest"),
    (PROJECT, "project_all", "Back link", "All projects"),
    (PROJECT, "project_enquire", "Enquiry button", "Enquire now"),
    (PROJECT, "project_brochure", "Brochure button", "Download brochure"),
    (PROJECT, "project_highlights_label", "Highlights: small label", "Highlights"),
    (PROJECT, "project_highlights_title", "Highlights: heading", "What sets it apart."),
    (PROJECT, "project_configs_label", "Floor plans: small label", "Configurations"),
    (PROJECT, "project_configs_title", "Floor plans: heading", "Choose your space."),
    (PROJECT, "project_request", "Floor plans: button on each", "Request details"),
    (PROJECT, "project_gallery_label", "Gallery: small label", "Gallery"),
    (PROJECT, "project_gallery_title", "Gallery: heading", "A closer look."),
    (PROJECT, "project_location_label", "Location: small label", "Location"),
    (PROJECT, "project_related_title", "More projects: heading", "More from *this collection.*"),
    (PROJECT, "project_related_link", "More projects: link", "View the collection"),
    (PROJECT, "project_explore", "Last button", "Explore all M3M projects"),
    (JOURNEY, "journey_values_label", "Values: small label", "What guides us"),
    (JOURNEY, "journey_values_title", "Values: heading", "Four principles, *every address.*"),
    (JOURNEY, "journey_values_text", "Values: text",
     "The ideas that shape how we design, build and stay in conversation with the people who choose M3M."),
    (JOURNEY, "journey_milestones_label", "Milestones: small label", "Milestones"),
    (JOURNEY, "journey_milestones_title", "Milestones: heading", "The journey *so far.*"),
    (JOURNEY, "journey_source", "Figures: source note (the link follows it)", "Figures as published on the"),
    (JOURNEY, "journey_source_link", "Figures: source link", "M3M India website"),
    (JOURNEY, "journey_work_label", "Projects: small label", "The work"),
    (JOURNEY, "journey_work_title", "Projects: heading", "Signature *addresses.*"),
    (JOURNEY, "journey_work_link", "Projects: button", "Explore all projects"),
    (MEDIA, "media_films_label", "Films: small label", "Films"),
    (MEDIA, "media_films_title", "Films: heading", "See it *in motion.*"),
    (MEDIA, "media_press_label", "Press: small label", "In the headlines"),
    (MEDIA, "media_press_title", "Press: heading", "M3M, as seen *in the news.*"),
    (MEDIA, "media_press_text", "Press: text",
     "Coverage from established business and real estate publications. Stories open on the publisher’s website."),
    (INSIGHTS, "insights_featured", "List: label over the featured article", "Featured"),
    (INSIGHTS, "insights_read", "List: featured article button", "Read the article"),
    (INSIGHTS, "insight_cta_title", "Article: enquiry box title", "Exploring an M3M address?"),
    (INSIGHTS, "insight_cta_text", "Article: enquiry box text", "Our team can answer your questions and arrange a visit."),
    (INSIGHTS, "insight_cta_button", "Article: enquiry box button", "Speak with our team"),
    (INSIGHTS, "insight_more_label", "Article: more articles, small label", "Keep reading"),
    (INSIGHTS, "insight_more_title", "Article: more articles, heading", "More *insights.*"),
    (INSIGHTS, "insight_all", "Article: more articles, button", "All insights"),
    (CONTACT, "contact_whatsapp_button", "Banner: WhatsApp button", "WhatsApp us"),
    (CONTACT, "contact_call_label", "Contact details: phone label", "Call toll-free"),
    (CONTACT, "contact_chat", "Contact details: WhatsApp link", "Chat with our team"),
    (CONTACT, "contact_form_title", "Form: heading", "Request a callback"),
    (CONTACT, "contact_form_intro", "Form: intro",
     "Tell us a little about what you’re looking for. Fields marked * are required."),
    (CONTACT, "contact_form_consent", "Form: consent tick box",
     "I agree to be contacted by M3M India about this enquiry. My details will not be used for unrelated marketing."),
    (CONTACT, "contact_form_button", "Form: button", "Request a callback"),
    (CONTACT, "contact_visit_label", "Map: small label", "Visit us"),
    (CONTACT, "contact_visit_title", "Map: heading", "Corporate office"),
    (CONTACT, "contact_directions", "Map: button", "Get directions"),
    (CONTACT, "contact_faq_label", "Questions: small label", "Good to know"),
    (CONTACT, "contact_faq_title", "Questions: heading", "Frequently *asked.*"),
    (NOT_FOUND, "not_found_title", "Heading", "This page could not be found."),
    (NOT_FOUND, "not_found_text", "Text", "The address may have changed, or the page is no longer available."),
    (NOT_FOUND, "not_found_button", "Button", "Explore all M3M projects"),
]

IMAGES = []

LISTS = {
    "menu": (
        "Header menu",
        "Title: the link text. Link: the page address, e.g. /our-journey. Group: “dropdown” opens the "
        "Projects dropdown below; “featured” shows the link in gold.",
    ),
    "project_menu": (
        "Header: Projects dropdown",
        "Title: the project name. Subtitle: the small line under it. Link: the project’s address, e.g. "
        "/projects/m3m-trump-tower-noida. A project that is not published is left out.",
    ),
}

ITEMS = {
    "menu": [
        {"title": title, "link": link, "group": group}
        for title, link, group in (
            ("Projects", "/projects", "dropdown"),
            ("Our Journey", "/our-journey", ""),
            ("Media", "/media-centre", ""),
            ("Insights", "/insights", ""),
            ("Contact Us", "/contact", ""),
            ("Billionaire Block", "/billionaire-block", "featured"),
        )
    ],
    "project_menu": [
        {"title": title, "subtitle": note, "link": link}
        for title, note, link in (
            ("M3M Jacob & Co. Residences", "Sector 97 · 3, 4 & 5 BHK", "/projects/m3m-jacob-co-residences"),
            ("M3M The Cullinan", "Sector 94 · 3, 4 & 5 BHK", "/projects/m3m-the-cullinan-residential"),
            ("M3M Trump Tower Noida", "Sector 94 · 4 & 5 BHK", "/projects/m3m-trump-tower-noida"),
        )
    ],
}
