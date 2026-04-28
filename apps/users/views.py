from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from .serializers import ProfileSerializer, UserSerializer

UserModel = get_user_model()

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer



