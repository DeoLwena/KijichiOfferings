from django.urls import path
from . import views


urlpatterns=[
    path('',views.MshirikiHome.as_view() ,name='mshiriki_home'),
]