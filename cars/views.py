from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarModel
from django.forms import model_to_dict
from .serializers import CarSerializer


# class CarsView(APIView):
#     def get(self, *args, **kwargs):
#         return Response({'message': 'OK'})
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         pk = kwargs['pk']
#         print(data)
#         print(pk)
#         print(self.request.query_params.dict())
#         return Response({'message': 'OK'})
#
#     def put(self, *args, **kwargs):
#         return Response({'message': 'OK'})
#     def delete(self, *args, **kwargs):
#         return Response({'message': 'OK'})
#     def patch(self, *args, **kwargs):
#         return Response({'message': 'OK'})


# class CarsListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         res = [model_to_dict(item) for item in cars]
#         return Response(res)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         car = CarModel.objects.create(**data)
#         car_dict = model_to_dict(car)
#         print(car_dict)
#         return Response(car_dict)
#
#
# class CarsRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         try:
#             car = CarModel.objects.get(pk=self.kwargs.get('pk'))
#         except CarModel.DoesNotExist:
#             raise Http404()
#         car_dict = model_to_dict(car)
#         return Response(car_dict)
#
#     def put(self, *args, **kwargs):
#         try:
#             car = CarModel.objects.get(pk=self.kwargs.get('pk'))
#         except CarModel.DoesNotExist:
#             raise Http404()
#         data = self.request.data
#         car.brand = data['brand']
#         car.price = data['price']
#         car.year = data['year']
#         car.save()
#         car_dict = model_to_dict(car)
#         return Response(car_dict)
#
#     def delete(self, *args, **kwargs):
#         try:
#             car = CarModel.objects.get(pk=self.kwargs.get('pk'))
#             car.delete()
#         except CarModel.DoesNotExist:
#             raise Http404()
#         return Response('deleted')


class CarsListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(instance=cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # print(dict(serializer.validated_data))
        # car = CarModel.objects.create(**data)
        # car_dict = model_to_dict(car)
        # print(car_dict)
        # return Response(car_dict)


class CarsRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=self.kwargs.get('pk'))
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializer(instance=car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=self.kwargs.get('pk'))
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(instance=car, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=self.kwargs.get('pk'))
        except CarModel.DoesNotExist:
            raise Http404()
        data = self.request.data
        serializer = CarSerializer(instance=car, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        try:
            car = CarModel.objects.get(pk=self.kwargs.get('pk'))
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()
        return Response(status=status.HTTP_204_NO_CONTENT)
