from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import CarFilter
from .models import CarModel
from .serializer import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    """"

        get:
            Create a new car
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarAddPhotoView(UpdateAPIView):
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CarPhotoSerializer
    http_method_names = ('put',)

    def perform_update(self, serializer):
        cars: CarModel = self.get_object()
        cars.car_photo.delete()
        super().perform_update(serializer)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
