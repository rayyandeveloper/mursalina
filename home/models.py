from django.db import models
from django.contrib import admin


class People(models.Model):
    full_name = models.CharField(max_length=256)
    birthday =  models.DateField()
    phone = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.full_name

