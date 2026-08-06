from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import MeView

from .views import SocketTokenView, UserActivateView

urlpatterns = [
    path('',TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/me', MeView.as_view(), name='auth_me'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='auth_activate'),
    path('/socket', SocketTokenView.as_view(), name='auth_socket_token'),
]