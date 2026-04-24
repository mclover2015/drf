from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')

    def validate_brand(self, value):
        if value == 'RIO':
            raise ValidationError('RIO is not available to create')
        return value

    def validate(self, item):
        if item['brand'] == item['year']:
            raise ValidationError('brand value == year value!!!')
        return item
