from django.urls import path

from content import views

urlpatterns = [
    path("insights", views.insight_list, name="insights"),
    path("insights/<slug:slug>", views.insight_detail, name="insight_detail"),
]
