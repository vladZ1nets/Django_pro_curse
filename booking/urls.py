from django.urls import path

from . import views

urlpatterns = [
    path("<booking_id>", views.booking_page, name="booking_page"),
    path("<booking_id>/cancel", views.booking_cancel, name="booking_cancel"),
    path("<booking_id>/accept", views.booking_acception, name="booking_acception"),
]