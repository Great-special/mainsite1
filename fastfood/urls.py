from django.urls import path

from . import views

urlpatterns = [
    path('', views.food, name='index'),
    path('food delivery form/', views.food_delivery_form, name='ordering form'),
]
