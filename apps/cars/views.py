from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .filters import CarFilter
from .models import CarModel
from .serializer import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.get_only_audi()
    serializer_class = CarSerializer
    filterset_class = CarFilter




class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


