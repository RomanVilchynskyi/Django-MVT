from django.contrib import admin
from django.urls import path

import api.views as views 

urlpatterns = [
    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>', views.CarDetail.as_view()),
    path('cars/create', views.CarList.as_view()),
]