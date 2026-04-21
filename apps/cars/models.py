from core.models import BaseModel
from django.db import models

class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=20)
    price = models.IntegerField()
    year = models.IntegerField()
