from django.db.migrations import serializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarModel
from .serializers import CarListSerializer, CarSerializer


class CarsListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarsRetrieveUpdateDestroyView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=kwargs['pk'])
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarListSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=kwargs['pk'])
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(car, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=kwargs['pk'])
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(car, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=kwargs['pk'])
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()
        return Response(status=status.HTTP_204_NO_CONTENT)
