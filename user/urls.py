from django.urls import path

from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='log in'),
    path('logout/', views.log_out, name='log out'),
]
