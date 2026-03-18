from django.urls import path
from . import views


urlpatterns=[
    path('',views.ReportsHome.as_view() ,name='mshiriki_home'),
]