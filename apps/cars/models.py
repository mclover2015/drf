from django.db import models

from apps.auto_parks.models import AutoPark
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    price = models.IntegerField()
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoPark, on_delete=models.CASCADE, related_name='cars')
