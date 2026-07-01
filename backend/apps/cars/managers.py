from django.db import models


class CarManager(models.Manager):
    def get_only_audi(self):
        return self.filter(brand='audi')
