from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("our-journey", views.journey, name="journey"),
    # /media/ is taken by uploaded files, so the Media page lives here.
    path("media-centre", views.media, name="media"),
    path("contact", views.contact, name="contact"),
    path("styleguide", views.styleguide, name="styleguide"),
    # Keep last: catches simple pages such as /privacy and /disclaimer.
    path("<slug:slug>", views.page, name="page"),
]
