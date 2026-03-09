from django.urls import path

from Uwakili.views import DashboardView
from . import views

urlpatterns=[

    path('', DashboardView.as_view(), name='mhazini_home'),


]