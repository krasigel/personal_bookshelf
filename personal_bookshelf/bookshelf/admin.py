from django.contrib import admin
from .models import Book, Bookshelf, BookshelfItem, BookRating


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'is_recommended', 'owner', 'created_at')
    list_filter = ('genre', 'is_recommended')
    search_fields = ('title', 'author', 'review')
    autocomplete_fields = ['owner']
    list_editable = ('is_recommended',)


@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'description', 'created_at')
    list_editable = ('description',)
    search_fields = ('title', 'description')
    autocomplete_fields = ['owner']


@admin.register(BookshelfItem)
class BookshelfItemAdmin(admin.ModelAdmin):
    list_display = ('bookshelf', 'book', 'added_at')
    autocomplete_fields = ['bookshelf', 'book']


@admin.register(BookRating)
class BookRatingAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    autocomplete_fields = ['book', 'user']

