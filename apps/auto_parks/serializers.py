from rest_framework import serializers

from apps.auto_parks.models import AutoPark
from apps.cars.serializer import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoPark
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')


class AutoParkWithoutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoPark
        fields = ('id', 'name', 'created_at', 'updated_at')
