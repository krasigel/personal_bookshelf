from django.db import models
from django.conf import settings

from personal_bookshelf.bookshelf.validators import validate_image_extension


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='article_covers/',
        validators=[validate_image_extension],
        default='article_covers/default_article_cover.jpg',
    )
    content = models.TextField()
    published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

