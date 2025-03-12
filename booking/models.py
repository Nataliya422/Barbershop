from django.db import models

# Create your models here.
from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name