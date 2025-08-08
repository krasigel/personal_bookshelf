from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.db.models import UniqueConstraint

from personal_bookshelf.bookshelf.validators import validate_image_extension


class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('mystery', 'Mystery'),
        ('fantasy', 'Fantasy'),
        ('sci-fi', 'Science Fiction'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('self-help', 'Self-help'),
        ('other', 'Other'),
    ]

    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1)],
    )
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, verbose_name='Genre')
    image = models.ImageField(
        upload_to='book_covers/',
        validators=[validate_image_extension],
        default='book_covers/default_cover.jpg',
    )
    review = models.TextField()
    is_recommended = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Bookshelf(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookshelves')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.owner}"


class BookshelfItem(models.Model):
    bookshelf = models.ForeignKey('Bookshelf', on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} in {self.bookshelf.title}"


class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['book', 'user'],
                name='unique_book_user_rating')
        ]


