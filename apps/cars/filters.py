from idlelib.query import Query

from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel


def car_filter(query: Query) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'brand_end':
                qs_filter = qs.filter(brand__iendswith=v)
                qs = qs_filter
            case _:
                raise ValidationError({'details': f'{k} is not allowed here'})
    return qs
