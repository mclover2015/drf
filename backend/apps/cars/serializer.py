from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.services.file_service import FileService

from .managers import CarManager
from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'body_type', 'year', 'created_at', 'updated_at', 'car_photo')

    # def validate_brand(self, value):
    #     if value == 'RIO':
    #         raise ValidationError('RIO is blocked to create')
    #     return value
    #
    # def validate(self, item):
    #     if item['brand'] == item['price']:
    #         raise ValidationError('brand cant equal price')
    #     return item


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('car_photo',)
        extra_kwargs = {'car_photo': {'required': True}}
