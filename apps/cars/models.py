from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoPark


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=20)
    price = models.IntegerField()
    year = models.IntegerField(validators=[V.MinValueValidator(2000), V.MaxValueValidator(2026)])
    auto_park = models.ForeignKey(AutoPark, on_delete=models.CASCADE, related_name='cars')
