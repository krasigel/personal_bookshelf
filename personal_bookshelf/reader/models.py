from django.db import models
from django.contrib.auth.models import AbstractUser

from personal_bookshelf.bookshelf.validators import validate_image_extension


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    favourite_genres = models.TextField(blank=True)
    published_reviews = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default_avatar.png',
        blank=True,
        null=True,
        validators=[validate_image_extension]
    )

    def __str__(self):
        return self.username

