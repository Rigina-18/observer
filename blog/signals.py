from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Like


# @receiver(post_save, sender=Like)
# def update_like(sender, instance, **kwargs):
#     review = instance.review
#     likes = review.like_set.count()
#     review.total_like = likes
#     review.save()
