from django.forms import ModelForm
from django import forms
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) < 10:
            raise forms.ValidationError("Содержимое должно содержать как минимум 10 символов.")
        return body