from django.core import validators as V
from django.db import models

from core.enums.enum_regex import Regex
from core.models import BaseModel
from core.services.file_service import FileService

from apps.auto_parks.models import AutoPark
from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.BRAND.value)])
    price = models.IntegerField()
    body_type = models.CharField(max_length=9, choices=BodyTypeChoices.choices)
    year = models.IntegerField(validators=[V.MinValueValidator(2000), V.MaxValueValidator(2026)])
    auto_park = models.ForeignKey(AutoPark, on_delete=models.CASCADE, related_name='cars')
    car_photo = models.ImageField(blank=True, upload_to=FileService.upload_car_photo)

    objects = CarManager()
