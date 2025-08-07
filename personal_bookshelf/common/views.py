from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Article


def index(request):
    return render(request, 'common/index.html')


def news_view(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'common/news.html', {'articles': articles})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'common/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def test_404_view(request):
    return HttpResponseNotFound(render(request, 'common/404.html'))