from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('''Добро пожаловать в Hexlet Django Blog.
                               Это главная страница блога.''')

# def index(request):
#     return render(request, 'articles/index.html', context={
#         'app_name': 'Hexlet Django Blog'
#     })