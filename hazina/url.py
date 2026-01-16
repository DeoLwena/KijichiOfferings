from django.urls import path
from . import views

urlpatterns=[

    path('', views.Dashboard, name='dashboard'),
    path('clerks/',views.Clerks),
    path('matoleo/', views.Addofferings),
    path('Reports/',views.Reports),

]