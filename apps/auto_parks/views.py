from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.auto_parks.models import AutoPark
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializer import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoPark.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (AllowAny,)


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AutoPark.objects.all()
    serializer_class = AutoParkSerializer



class AutoParkAddCar(GenericAPIView):
    queryset = AutoPark.objects.all()

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer_cars = CarSerializer(auto_park.cars, many=True)
        return Response(serializer_cars.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParkSerializer(auto_park)
        return Response(ap_serializer.data, status=status.HTTP_201_CREATED)
