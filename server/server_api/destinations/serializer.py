from rest_framework import serializers
from .models import Destination


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ("city",)


class NearestCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ("city", "country")
