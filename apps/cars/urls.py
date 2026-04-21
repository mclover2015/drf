from django.urls import path

from apps import cars
from .views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='car_retrieve_update_destroy'),
]
