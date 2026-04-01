from .models import Mtoaji
from .serializers import MtoajiSerializer
from rest_framework import viewsets

class MtoajiViewSet(viewsets.ModelViewSet):
    queryset = Mtoaji.objects.all()
    serializer_class = MtoajiSerializer