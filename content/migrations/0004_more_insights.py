"""Five more Insights articles. Each is created only if its address is free, so
articles the content team has edited or deleted are left alone."""

import datetime
from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.files.storage import default_storage
from django.db import migrations

ARTICLES = [
    {
        "slug": "carpet-built-up-and-super-area-explained",
        "category": "Buyer’s guide",
        "title": "Carpet, built-up and super area, explained",
        "description": "Three measurements appear on almost every brochure. Here is what each one counts, and why it matters when you compare homes.",
        "image": "media/m12.jpeg",
        "published_on": datetime.date(2026, 7, 14),
        "body": """Every brochure quotes an area, but not every brochure quotes the same one. Before you compare two homes, or two prices per sq ft, it helps to know exactly which measurement you are looking at.

## Carpet area: the space you actually live in

Carpet area is the net usable floor area of your home: the living room, bedrooms, kitchen and bathrooms. RERA defines it as the area within the apartment excluding the external walls, service shafts and exclusive balconies or terraces, but including internal partition walls. Developers are required to state it, which makes it the most reliable figure for comparing one home with another.

When you walk through a sample flat and imagine where the sofa, the dining table and the beds will go, you are thinking in carpet area.

## Built-up area: adding the walls and balconies

Built-up area adds what sits around and alongside the carpet area: the thickness of the external walls, and usually balconies or utility areas attached to the home. It is a larger number than carpet area, and how much larger depends on the design.

## Super area: a share of everything you use together

Super area, sometimes called super built-up or saleable area, adds a proportionate share of the common spaces: lobbies, lift wells, staircases, corridors and, depending on the project, parts of the clubhouse and other shared facilities. It is the largest of the three figures.

A generous super area is not a bad thing in itself. Wide lobbies, a well-equipped clubhouse and comfortable corridors are part of what you pay for. It simply means that the super area tells you about the building, while the carpet area tells you about your home.

## How to compare fairly

Compare like with like. If one home is quoted on carpet area and another on super area, convert before you compare.

Ask for the carpet area in writing. It should appear in the RERA registration details and in your agreement.

Look at the plan, not only the number. Two homes with the same carpet area can feel very different depending on room proportions, light and how much space is lost to passages.

Check what is counted. Ask whether balconies, utility areas and terraces are included in a figure, and how they are measured.

A few minutes spent on these questions makes every conversation that follows, about price, layout or payment, much clearer.""",
    },
    {
        "slug": "ready-to-move-or-under-construction",
        "category": "Perspective",
        "title": "Ready to move or under construction?",
        "description": "Both routes can lead to the right home. The better choice depends on your timeline, your finances and how much certainty you need.",
        "image": "billionaire_block/towers-day.jpg",
        "published_on": datetime.date(2026, 6, 30),
        "body": """One of the first decisions in any property search is whether to buy a home you can move into now or one that is still being built. Neither is the right answer for everyone. The useful question is which one fits your situation.

## What a ready home offers

With a completed home, what you see is what you get. You can walk through the actual flat, check the view from the balcony, see how the common areas are maintained and talk to people who already live there. You can plan a move date with confidence, and if you are currently paying rent, that cost ends sooner.

The trade-off is choice. In a completed building, the units still available may be limited, and you may have less say over the floor, facing or layout you end up with.

## What an under-construction home offers

Buying earlier usually means a wider selection of floors, views and configurations, and payments that are spread over the construction period rather than due all at once. For buyers who are not in a hurry to move, that flexibility can be valuable.

The trade-off is time and trust. You are committing to a home you cannot yet stand in, so the developer’s track record and the project’s registration details matter more.

## Questions to ask about an under-construction home

What is the committed possession date? Check it against the date stated in the project’s RERA registration.

How are payments linked to progress? In a construction-linked plan, instalments fall due as stages are completed. Ask for the schedule in writing.

What has already been built? A site visit tells you more than any render.

What does the developer’s track record show? Look at projects they have completed and how those buildings feel today.

## Making the call

If you need to move within a fixed window, or you value certainty above everything else, a ready home is often the calmer choice. If you have time, want a particular floor or view, and are comfortable with a staged commitment, an under-construction home can offer more. Our team is happy to talk through both routes with you.""",
    },
    {
        "slug": "what-to-look-for-in-a-clubhouse",
        "category": "Thoughtful living",
        "title": "What to look for in a clubhouse",
        "description": "Amenity lists can run to dozens of items. A few practical questions reveal which ones you will actually use.",
        "image": "media/m7.jpeg",
        "published_on": datetime.date(2026, 6, 16),
        "body": """A clubhouse can become the most-used room in your life, or a beautiful space you visit twice a year. The difference rarely comes down to the number of amenities on the list. It comes down to fit.

## Start with your week, not the brochure

Think about an ordinary week. Do you exercise in the morning before work, or in the evening? Do children need somewhere to play after school? Do you work from home and need a quiet space away from your desk? Do you host family on weekends?

Then look at the amenity list with those routines in mind. A well-equipped gym, a lap pool and a co-working lounge you will use every week are worth more than a long list of occasional features.

## Questions worth asking on a visit

How far is it from the residences? A clubhouse reached by a short, covered walk will be used far more than one that needs planning.

What are the hours? Early opening and late closing make a real difference for working households.

Is the space sized for the community? Ask how many homes share the facilities, and imagine the pool or gym at its busiest hour.

Which spaces need booking? Party halls, courts and theatres are often reserved in advance. It helps to know how that works.

Who maintains it? Well-kept spaces stay inviting. Ask how upkeep is managed and funded.

## Spaces for every age

The best clubhouses work across generations: a safe, supervised area for young children, somewhere teenagers actually want to be, and calm, accessible spaces for older residents. Landscaped walks and seating corners matter as much as any equipment.

## The test of a good amenity

A good amenity is one you stop noticing as a feature, because it has simply become part of how you live. When you tour a clubhouse, picture yourself using it on a Tuesday evening, not only on the day you move in.""",
    },
    {
        "slug": "buying-a-home-in-india-from-overseas",
        "category": "Buyer’s guide",
        "title": "Buying a home in India from overseas",
        "description": "A calm, practical outline for Non-Resident Indians considering a home in India, and the points worth checking with a professional.",
        "image": "billionaire_block/living-room.jpg",
        "published_on": datetime.date(2026, 6, 2),
        "body": """Many families abroad want a home in India: a base for visits, a place to return to, or a home for parents. Buying from a distance is very possible, and a little preparation makes it much smoother.

This article is general information, not legal or tax advice. Rules can change, and your situation is your own, so please confirm the details with a qualified professional before you commit.

## Before you begin

Clarify your residential status. Whether you are treated as a Non-Resident Indian or an Overseas Citizen of India affects the type of property you can buy and how payments must be made.

Plan how funds will move. Purchases by non-residents are generally expected to be paid through the Indian banking system, typically from designated non-resident accounts. Your bank can explain the options.

Speak to a tax adviser. Ask about tax in India and in your country of residence, both when you buy and if you later rent out or sell the home.

## Choosing from a distance

Video walkthroughs, detailed floor plans and a candid conversation with the developer’s team can take you a long way. Ask for the carpet area, the RERA registration details and a clear payment schedule in writing.

If you can, plan one visit before you make a final decision, or ask a trusted family member to visit on your behalf. Seeing the site, the neighbourhood and the approach roads in person answers questions that no brochure can.

## Paperwork and representation

You may not be able to be in India for every signature. Many overseas buyers appoint a trusted person through a power of attorney to act for them on specific matters. A lawyer can advise on how to draft and register it correctly.

Keep copies of every agreement, receipt and bank record in one place. They will matter for registration, for tax and for any future sale.

## Talking to us

Our team regularly speaks with buyers in other time zones and can arrange calls at a time that suits you. Share your city and preferred hours on the contact form, and we will plan around them.""",
    },
    {
        "slug": "life-along-an-expressway-corridor",
        "category": "City perspective",
        "title": "Life along an expressway corridor",
        "description": "Expressway corridors are reshaping how the region lives and works. A few things to weigh when you consider a home along one.",
        "image": "dark_banners/b2.jpeg",
        "published_on": datetime.date(2026, 5, 19),
        "body": """Across the National Capital Region, new neighbourhoods are taking shape along the expressways: the Noida Expressway, the Dwarka Expressway and others. For many buyers, these corridors offer something older city centres find hard to match: newer infrastructure, planned layouts and room to grow.

## Why corridors attract new homes

Expressways connect places that matter in daily life: business districts, airports, schools and established parts of the city. As those connections improve, residential and commercial projects tend to follow, and with them come the shops, clinics, schools and restaurants that turn a stretch of road into a neighbourhood.

Newer developments along these routes are often planned at a larger scale, with landscaped open space, clubhouses and wider internal roads designed in from the start.

## What to weigh on a visit

Your real commute. Drive the route at the times you would actually travel, not only on a quiet weekend afternoon.

The everyday essentials. Note how far you would go for groceries, a pharmacy, a school or a hospital, and what is already open versus planned.

The approach to the building. Service roads, entrances and walkability matter as much as the expressway itself.

Noise and orientation. Homes facing a busy road can be lively; homes facing inward or toward green space can be calmer. Ask which units face which way.

## A neighbourhood in progress

A corridor is rarely finished on the day you visit. Part of the appeal is watching an area mature: new parks, new retail and new connections arriving over time. It helps to understand what is already in place and to treat anything still to come with patience.

The right home on a corridor is one that works for your life today, with the area’s growth as a welcome addition rather than the only reason to move.""",
    },
]


def add_insights(apps, schema_editor):
    Insight = apps.get_model("content", "Insight")
    order = (Insight.objects.order_by("-order").values_list("order", flat=True).first() or 0) + 1
    for article in ARTICLES:
        data = dict(article)
        slug = data.pop("slug")
        if Insight.objects.filter(slug=slug).exists():
            continue
        source = Path(settings.BASE_DIR) / "seed" / "images" / data.pop("image")
        name = f"insights/{source.name}"
        if not default_storage.exists(name):
            with open(source, "rb") as handle:
                name = default_storage.save(name, File(handle))
        Insight.objects.create(slug=slug, image=name, order=order, author="M3M India Editorial", **data)
        order += 1


def remove_insights(apps, schema_editor):
    Insight = apps.get_model("content", "Insight")
    Insight.objects.filter(slug__in=[article["slug"] for article in ARTICLES]).delete()


class Migration(migrations.Migration):
    dependencies = [("content", "0003_publications")]

    operations = [migrations.RunPython(add_insights, remove_insights)]
