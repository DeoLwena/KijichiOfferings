from django.urls import path
from . import views

urlpatterns=[
    path('matoleo/', views.matoleo),
    path('',views.Home),
]