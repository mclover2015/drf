from rest_framework import serializers
from apps.users.models import UserModel
from apps.auto_parks.serializers import AutoParkSerializer, AutoParkWithoutCarsSerializer


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkWithoutCarsSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'age', 'created_at', 'updated_at', 'auto_parks')

