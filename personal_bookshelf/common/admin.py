from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'author', 'created_at')
    list_filter = ('published',)
    search_fields = ('title', 'content')

