from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from .models import CarModel
from .serializer import CarSerializer

from .filters import car_filter


# class CarsListCreateView(ListCreateAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer

class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


        # qs = super().get_queryset()
        # query = self.request.query_params
        # for k, v in query.items():
        #     match k:
        #         case 'price_gt':
        #             qs = qs.filter(price__gt=v)
        #         case 'brand_end':
        #             qs_filter = qs.filter(brand__iendswith=v)
        #             qs = qs_filter
        #         case _:
        #             raise ValidationError({'details': f'{k} is not allowed here'})
        # return qs

        # class CarListCreateView(GenericAPIView):
        #     def get(self, *args, **kwargs):
        #         # cars = CarModel.objects.filter(price__range=(0, 1000000)).order_by('-brand','-year').reverse()
        #         # qs = CarModel.objects.filter(price__gt=5000).exclude(price__lte=5000).count()
        #         # qs = CarModel.objects.filter(brand='oka', year=2022)
        #         # qs = CarModel.objects.filter(Q(brand='oka') | Q(year=2020) & Q(price=103333))
        #         query = self.request.query_params
        #         qs = CarModel.objects.all()
        #         for k, v in query.items():
        #             match k:
        #                 case 'price_gt':
        #                     qs = qs.filter(price__gt=v)
        #                 case 'brand_end':
        #                     qs_filter = qs.filter(brand__iendswith=v)
        #                     qs = qs_filter
        #                 case _:
        #                     raise ValidationError({'details': f'{k} is not allowed here'})
        #         serializer = CarSerializer(qs, many=True)
        #         return Response(serializer.data)

    # serializer = CarSerializer(qs, many=True)
    # return Response(serializer.data, status=status.HTTP_200_OK)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

# class CarsListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

# def get(self, *args, **kwargs):
#     cars = CarModel.objects.all()
#     serializer = CarSerializer(cars, many=True)
#     return Response(serializer.data, status.HTTP_200_OK)
#
# def post(self, request, *args, **kwargs):
#     data = self.request.data
#     serializer = CarSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status.HTTP_201_CREATED)


# class CarsRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

# def get(self, *args, **kwargs):
#     # pk = kwargs['pk']
#     # car = get_object_or_404(CarModel, pk=pk)
#     car = self.get_object()
#     serializer = CarSerializer(car)
#     return Response(serializer.data, status.HTTP_200_OK)
#
# def put(self, request, *args, **kwargs):
#     # pk = kwargs['pk']
#     # car = get_object_or_404(CarModel, pk=pk)
#     car = self.get_object()
#     data = self.request.data
#     serializer = CarSerializer(car, data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status.HTTP_200_OK)
#
# def patch(self, request, *args, **kwargs):
#     # pk = kwargs['pk']
#     # car = get_object_or_404(CarModel, pk=pk)
#     car = self.get_object()
#     data = self.request.data
#     serializer = CarSerializer(car, data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status.HTTP_200_OK)
#
# def delete(self, *args, **kwargs):
#     self.get_object().delete()
#     return Response(status.HTTP_204_NO_CONTENT)
