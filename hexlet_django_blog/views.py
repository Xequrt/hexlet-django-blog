from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views import View


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context
# class IndexView(View):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html')
        # return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def about(request):
    return render(request, 'about.html')