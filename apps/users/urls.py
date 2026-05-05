from django.urls import path

from apps.users.views import (
    AdminToUserView,
    BlockUserView,
    UnblockUserView,
    UserAddAvatarView,
    UserListCreateView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_lists_create'),
    path('/avatar', UserAddAvatarView.as_view(), name='user_add_avatar'),
    path('/<int:pk>/admin_to_user', AdminToUserView.as_view(), name='user_admin_to_user'),
    path('/<int:pk>/user_to_admin', UserToAdminView.as_view(), name='user_user_to_admin'),
    path('/<int:pk>/block', BlockUserView.as_view(), name='user_block'),
    path('/<int:pk>/unblock', UnblockUserView.as_view(), name='user_unblock'),

]
