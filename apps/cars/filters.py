from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel
from apps.cars.serializer import CarSerializer


def cars_filter(query_dict):
    qs = CarModel.objects.all()
    for k, v in query_dict.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price__gte':
                qs = qs.filter(price__gte=v)
            case 'price__lte':
                qs = qs.filter(price__lte=v)

            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)

            case 'brand_startswith':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_endswith':
                qs = qs.filter(brand__iendswith=v)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=v)

            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]
                if v not in fields:
                    raise ValidationError(f'Invalid field: {v}, choose from {fields}')
                qs = qs.order_by(v)
            case _:
                raise ValidationError(f'{k} is not a valid filter')

    return qs
