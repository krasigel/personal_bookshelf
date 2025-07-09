from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField()
    favourite_genres = models.TextField(blank=True)
    published_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username
CustomUser.objects.all()
