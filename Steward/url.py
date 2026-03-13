from django.urls import path
from .views import StewardHome

urlpatterns = [
    path('', StewardHome.as_view(), name='steward_home'),
]