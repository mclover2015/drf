from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.auto_cars.models import AutoParkModel
from apps.cars.serializer import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id','name','created_at','updated_at','cars')



        