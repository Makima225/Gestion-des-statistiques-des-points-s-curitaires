from django.db import models


# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CategoryEvent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_of_additions = models.DateTimeField(auto_now_add=True)
    date_of_event = models.DateTimeField(auto_now_add=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    category_event = models.ForeignKey(CategoryEvent, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
