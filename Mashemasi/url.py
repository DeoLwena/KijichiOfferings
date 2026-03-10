from django.urls import path
from Mashemasi.views import DashboardView


urlpatterns=[

    path('', DashboardView.as_view(), name='Mashemasi_home'),


]