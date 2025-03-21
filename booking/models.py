# booking/models.py
from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя мастера")
    experience = models.IntegerField(verbose_name="Опыт работы")

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название услуги")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name

class Review(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    comment = models.TextField(verbose_name="Комментарий")
    rating = models.IntegerField(verbose_name="Рейтинг")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата отзыва")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.client_name} для {self.master.name}"