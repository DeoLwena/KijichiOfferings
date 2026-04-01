from rest_framework import serializers
from .models import Idara,Matoleo


class IdaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idara
        fields = '__all__'

class MatoleoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matoleo
        fields = '__all__'