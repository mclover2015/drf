from django.urls import path

from apps.users.views import UserAddAvatarView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_lists_create'),
    path('/avatar', UserAddAvatarView.as_view(), name='user_add_avatar'),

]
