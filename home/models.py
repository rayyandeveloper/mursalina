from django.db import models
from django.contrib import admin


class People(models.Model):
    full_name = models.CharField(max_length=256)
    birthday =  models.DateField()
    phone = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.full_name

class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    peoples = models.ManyToManyField(People, blank=False)
    start_time = models.TimeField()

    def __str__(self) -> str:
        return self.title


        