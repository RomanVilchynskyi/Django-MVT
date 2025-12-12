from django.urls import path
from . import views

import cars.views

urlpatterns = [
    path("", views.cars_index),
    path("<int:pk>/", views.cars_detail),
    # path("create/", views.cars_create),
    # path("<int:car_id>/edit/", views.cars_edit),
    path("delete/<int:pk>/", views.cars_delete),
]
