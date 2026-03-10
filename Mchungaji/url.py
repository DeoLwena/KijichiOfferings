from django.urls import path
from Mchungaji.views import DashboardView

urlpatterns=[
    path('', DashboardView.as_view(), name='mchungaji_home'),
]