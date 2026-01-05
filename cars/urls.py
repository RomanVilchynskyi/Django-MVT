from django.urls import path
from . import views

import cars.views

urlpatterns = [
    path("", views.cars_index, name='cars_index'),
    path("list/", views.cars_list, name='cars_list'),
    path("<int:pk>/", views.cars_detail),
    path("create/", views.cars_create, name='cars_create'),
    path("edit/<int:pk>/", views.cars_edit, name='cars_edit'),
    path("delete/<int:pk>/", views.cars_delete),
]
