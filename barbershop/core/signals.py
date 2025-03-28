from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import check_review
from booking.models import Review

@receiver(post_save, sender=Review)
def review_post_save(sender, instance, created, **kwargs):
    """
    Обработчик сигнала сохранения отзыва.
    Проверяет новые отзывы на корректность и устанавливает флаг is_approved.
    """
    if created:  # Только для новых отзывов
        review = instance
        
        # Отправляем текст отзыва на проверку
        is_approved = check_review(review.comment)
        
        # Если значение is_approved изменилось, сохраняем объект
        if review.is_approved != is_approved:
            review.is_approved = is_approved
            
            # Отключаем отправку сигнала при этом сохранении,
            # чтобы избежать рекурсии (требует Django 2.2+)
            Review.objects.filter(pk=review.pk).update(is_approved=is_approved)
            
            print(f"Отзыв ID={review.id} проверен: {'одобрен' if is_approved else 'отклонен'}")