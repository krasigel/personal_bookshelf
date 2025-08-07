from django.urls import path

from personal_bookshelf.common import views
from personal_bookshelf.common.views import news_view, ArticleDetailView, test_404_view

urlpatterns = [
    path("", views.index, name="home"),
    path("news/", news_view, name="news"),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('test-404/', test_404_view, name='test_404'),
]