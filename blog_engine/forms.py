from django.db import models
from django import forms

#model form
from blog_engine.models import Post, Category
from django.forms import ModelForm

class NewBlogForm(ModelForm):
    title = models.CharField(max_length=150)
    categories = forms.ModelChoiceField(queryset=Category.objects.all())
    body = models.CharField(max_length=255)
    class Meta:
        model = Post 
        fields = ['title','categories','body']
    def __str__(self):
        return self.title