from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.views import View
from .forms import ArticleForm

from hexlet_django_blog.article.models import Article

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        messages.success(request, 'Данные получены!')
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные обновлены!')
            return redirect('article_index')
        messages.error(request, 'Произошла ошибка при валидации данных!')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormCreateView(View):

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные отправлены!')
            return redirect(reverse('article_index'))
        messages.error(request, 'Произошла ошибка при валидации данных!')
        return render(request, 'articles/create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        messages.success(request, 'Данные получены!')
        return render(request, 'articles/create.html', {'form': form})

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })