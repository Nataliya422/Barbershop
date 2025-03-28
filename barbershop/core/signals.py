from django.db.models.signals import post_save
from django.dispatch import receiver
from core.utils import check_review
from booking.models import Review
 
@receiver(post_save, sender=Review)
def review_post_save(sender, instance, created, **kwargs):
     if created:
         review = instance
         review_comment = review.comment
         review.save()