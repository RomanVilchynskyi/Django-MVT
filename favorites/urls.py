from django.urls import path
from . import views

import cars.views

import favorites

urlpatterns = [
    path("", favorites.views.index, name='favs_index'),
    path('add/<int:car_id>/<str:return_url>/', favorites.views.add_car, name='add_fav_car'),
    path('remove/<int:car_id>/<str:return_url>/', favorites.views.remove_car, name='remove_fav_car'),
]
