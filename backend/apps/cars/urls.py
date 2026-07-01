from django.urls import path

from .views import CarAddPhotoView, CarListCreateView, CarsRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarsRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
    path('/<int:pk>/photo', CarAddPhotoView.as_view(), name='car_photo_update'),

]
