from django.urls import path
from Uwakili.views import DashboardView


urlpatterns=[

    path('', DashboardView.as_view(), name='mhazini_home'),


]