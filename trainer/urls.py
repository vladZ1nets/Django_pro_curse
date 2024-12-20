from django.urls import path

from . import views

urlpatterns = [
    path("<trainer_id>", views.trainer_page, name="trainer_page"),
    path("<trainer_id>/<service_id>", views.trainer_service_page, name="train_service_page"),
    path("<trainer_id>/<service_id>/booking", views.booking_for_user, name="booking_for_user"),
]