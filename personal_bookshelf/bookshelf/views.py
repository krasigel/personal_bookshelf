from django.db.models import Avg, Q
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Book, Bookshelf, BookshelfItem, BookRating
from .forms import BookForm
from django.contrib.auth.decorators import login_required


class BookCreateView(LoginRequiredMixin, CreateView):

    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('bookshelf')

    def form_valid(self, form):

        form.instance.owner = self.request.user
        response = super().form_valid(form)
        bookshelf, created = Bookshelf.objects.get_or_create(
            owner=self.request.user,
            defaults={
                "title": f"{self.request.user.username}'s Bookshelf",
                "description": f"The reviews and images are the property of {self.request.user.username}."
            }
        )
        BookshelfItem.objects.create(
            bookshelf=bookshelf,
            book=self.object
        )

        return response


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('bookshelf')

    def test_func(self):
        return self.get_object().owner == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('bookshelf')

    def test_func(self):
        return self.get_object().owner == self.request.user


class BookDetailView(DetailView):

    model = Book
    template_name = 'bookshelf/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # изчисляваме средния рейтинг

        avg_rating = self.object.ratings.aggregate(Avg('rating'))['rating__avg']
        context['avg_rating'] = avg_rating

        # ако потребителят е логнат, да му покажем неговата оценка

        if self.request.user.is_authenticated:
            user_rating = self.object.ratings.filter(user=self.request.user).first()
            context['user_rating'] = user_rating

        return context


class MyBookshelfView(LoginRequiredMixin, ListView):

    model = Book
    template_name = 'bookshelf/bookshelf.html'
    context_object_name = 'books'

    def get_queryset(self):
        return (
            Book.objects
            .filter(owner=self.request.user)
            .annotate(avg_rating=Avg('ratings__rating'))
        )


def all_bookshelves(request):
    bookshelves = Bookshelf.objects.select_related('owner')

    return render(request, 'bookshelf/all_bookshelves.html', {'bookshelves': bookshelves})


class SpecificBookshelfView(ListView):

    model = BookshelfItem
    template_name = 'bookshelf/bookshelf.html'
    context_object_name = 'books'

    def get_queryset(self):
        bookshelf = get_object_or_404(Bookshelf, pk=self.kwargs['pk'])
        return (
            BookshelfItem.objects
            .filter(bookshelf=bookshelf)
            .select_related('book')
            .annotate(avg_rating=Avg('book__ratings__rating'))

        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookshelf = get_object_or_404(Bookshelf, pk=self.kwargs['pk'])
        context['bookshelf_owner'] = bookshelf.owner
        context['bookshelf'] = bookshelf
        return context


@login_required
def rate_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        rating_value = int(request.POST.get("rating", 0))
        if 1 <= rating_value <= 5:
            BookRating.objects.update_or_create(
                book=book,
                user=request.user,
                defaults={"rating": rating_value},
            )

            # Проверяваме дали книгата е в чужд bookshelf

        bookshelf_item = (
            BookshelfItem.objects
            .filter(book=book)
            .select_related("bookshelf")
            .first()
        )
        if bookshelf_item:
            return redirect("bookshelf_detail", pk=bookshelf_item.bookshelf.pk)
        else:
            return redirect("bookshelf")

    user_rating = BookRating.objects.filter(book=book, user=request.user).first()
    avg_rating = book.ratings.aggregate(Avg("rating"))["rating__avg"]

    return render(request, "bookshelf/rate_book.html", {
        "book": book,
        "user_rating": user_rating,
        "avg_rating": avg_rating,
    })


def search_bookshelves(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = (
            BookshelfItem.objects
            .filter(
                Q(book__title__icontains=query) |
                Q(book__author__icontains=query)
            )
            .select_related('book', 'bookshelf', 'bookshelf__owner')
            .annotate(avg_rating=Avg('book__ratings__rating'))
        )

    return render(request, 'bookshelf/search_results.html', {
        'query': query,
        'results': results,
    })
