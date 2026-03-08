from django.urls import path
from . import views

urlpatterns=[

    path('', views.Dashboard, name='mhazini_home'),


]