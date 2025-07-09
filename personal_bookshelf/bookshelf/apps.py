from django.apps import AppConfig

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal_bookshelf.bookshelf'

    def ready(self):
        import personal_bookshelf.bookshelf.signals
