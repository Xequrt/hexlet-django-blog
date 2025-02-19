from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='article_index'),
    path('<int:id>/', ArticleView.as_view(), name='article_id'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]