from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Bookshelf

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_bookshelf(sender, instance, created, **kwargs):
    if created:
        Bookshelf.objects.create(
            owner=instance,
            title=f"{instance.username}'s Bookshelf",
            description="This is your personal bookshelf."
        )
