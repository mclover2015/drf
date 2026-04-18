from django.db import models

class CarModel(models.Model):
    class Meta:
        db_table = 'cars_hm1'
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seat_count = models.IntegerField()
    body_type = models.CharField(max_length=20)
    engine_volume = models.FloatField()