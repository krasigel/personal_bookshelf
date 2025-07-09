from personal_bookshelf.bookshelf.widgets import NoLinkClearableFileInput
from personal_bookshelf.common.models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    image = forms.ImageField(
        required=True,
        widget=NoLinkClearableFileInput()
    )

    class Meta:
        model = Article
        fields = ['title', 'image', 'content', 'published', 'author']
