from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.jwt_service import ActivateToken, JWTService

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self,*args,**kwargs):
        token = kwargs['token']
        user:UserModel = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
