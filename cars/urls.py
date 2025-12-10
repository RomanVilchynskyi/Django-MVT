from django.urls import path
from . import views

urlpatterns = [
    path("", views.cars_index),
    path("<int:car_id>/", views.cars_detail),
    # path("create/", views.cars_create),
    # path("<int:car_id>/edit/", views.cars_edit),
    # path("<int:car_id>/delete/", views.cars_delete),
]
