from django.urls import path
from . import views

urlpatterns = [

    path('Mashemasi/', views.MashemasiDashboard.as_view(), name='mashemasi_home'),
    path('Mchungaji/', views.MchungajiDashboard.as_view(), name='mchungaji_home'),
    path('Uwakili/', views.UwakiliDashboard.as_view(), name='uwakili_home'),
    path('Mhazini/', views.MhaziniDashboard.as_view(), name='mhazini_home'),

]
