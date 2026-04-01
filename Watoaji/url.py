from django.urls import path, include

from matoleo.views import IdaraViewset
from .views import MtoajiViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('mtoaji', MtoajiViewSet)
router.register('idara',IdaraViewset)

urlpatterns=[

    path('',include(router.urls)),
]