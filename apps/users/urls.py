from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView,UserAddAutoParkView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    path('/<int:pk>/auto_parks', UserAddAutoParkView.as_view(), name='user_add_auto_parks'),

]
