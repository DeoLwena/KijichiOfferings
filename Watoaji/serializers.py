from .models import Mtoaji
from rest_framework import serializers

class MtoajiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mtoaji
        fields = '__all__'