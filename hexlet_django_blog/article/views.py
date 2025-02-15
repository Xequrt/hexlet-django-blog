from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        tags = kwargs.get('tags') if kwargs.get('tags') else 'python'
        article = kwargs.get('article_id') if kwargs.get('article_id') else 42
        return HttpResponse(f'Статья номер {article}. Тег {tags}')

# def index(request):
#     return render(request, 'articles/index.html', context={
#         'app_name': 'Hexlet Django Blog'
#     })