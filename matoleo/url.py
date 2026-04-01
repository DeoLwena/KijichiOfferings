from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatoleoViewset,IdaraViewset

router = DefaultRouter()
router.register('utoaji', MatoleoViewset)
router.register('Idara', IdaraViewset)
urlpatterns = [
    path('', include(router.urls)),
]