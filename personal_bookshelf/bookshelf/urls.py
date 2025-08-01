from django.urls import path

from personal_bookshelf.bookshelf.views import BookDeleteView, BookCreateView, BookUpdateView, MyBookshelfView, \
    BookDetailView, all_bookshelves, SpecificBookshelfView, rate_book, search_bookshelves

urlpatterns = [
    path("",  MyBookshelfView.as_view(), name='bookshelf'),
    path('all/', all_bookshelves, name='all_bookshelves'),
    path('add/', BookCreateView.as_view(), name='book_add'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>/detail/', BookDetailView.as_view(), name='book_detail'),
    path("view/<int:pk>/", SpecificBookshelfView.as_view(), name="bookshelf_detail"),
    path("<int:pk>/rate/", rate_book, name="book_rate"),
    path('bookshelves/search/', search_bookshelves, name='bookshelf_search'),




]