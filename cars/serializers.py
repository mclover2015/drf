from rest_framework import serializers
from .models import CarModel


class BaseCarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()


class CarListSerializer(BaseCarSerializer):
    pass


class CarSerializer(BaseCarSerializer):
    seat_count = serializers.IntegerField()
    body_type = serializers.CharField(max_length=20)
    engine_volume = serializers.FloatField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance
