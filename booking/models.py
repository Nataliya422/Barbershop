# booking/models.py
from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()  # Рейтинг от 1 до 5
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client_name} for {self.master.name}"
