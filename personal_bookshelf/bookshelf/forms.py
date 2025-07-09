from django import forms
from .models import Book
from .widgets import NoLinkClearableFileInput


class BookForm(forms.ModelForm):
    image = forms.ImageField(
        required=True,
        widget=NoLinkClearableFileInput()
    )

    class Meta:
        model = Book
        fields = ['image', 'title', 'author', 'genre', 'review', 'is_recommended']

