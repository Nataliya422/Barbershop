from django.db import models
from django.contrib.auth.models import User

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
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name

class Review(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    comment = models.TextField(max_length=500, verbose_name="Комментарий")
    rating = models.IntegerField(verbose_name="Рейтинг")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата отзыва")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрен")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.client_name} для {self.master.name}"
    
class Signal(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="Отзыв")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")
    signal_type = models.CharField(max_length=50, verbose_name="Тип сигнала")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата сигнала")

    class Meta:
        verbose_name = "Сигнал"
        verbose_name_plural = "Сигналы"

    def __str__(self):
        return f"Сигнал на отзыв {self.review.id} от {self.user.username}"

class Appointment(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"Запись для {self.client_name} на {self.date} в {self.time}"
