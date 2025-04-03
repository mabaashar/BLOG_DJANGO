#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
import json
import requests
from django.db import connection
from django.core.management.color import no_style

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#paginator
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# models
from blog_engine.models import Category,Post

#forms
from blog_engine.forms import NewBlogForm

#categories page
def categories(request):
    #get post
    categories = Category.objects.all()
    template = loader.get_template('categories.html')
    return HttpResponse(template.render({'categories':categories},request))

#posts by category
def posts_by_category(request,chosen_category):
    #get posts
    chosen_posts = Post.objects.filter(categories_id = chosen_category)
    #get category
    post_category = Category.objects.get(id=chosen_category).name
    template = loader.get_template('posts_by_category.html')
    return HttpResponse(template.render({'chosen_posts':chosen_posts,'category':post_category},request))

#post page
def blog_post(request,chosen_post):
    print("in blog post")
    #get post
    chosen_post = Post.objects.get(id = chosen_post)
    #get category
    post_category = chosen_post.categories
    template = loader.get_template('blog_post.html')
    return HttpResponse(template.render({'chosen_post':chosen_post,'post_category':post_category,},request))

#--blog functions

#new post
@login_required
def write(request):
    #new post form
    form = NewBlogForm()
    if request.POST:
        form = NewBlogForm(request.POST,request.FILES)
        if form.is_valid():
           post = Post()
           post.author = request.user
           post.title = form.cleaned_data["title"]
           post.body = form.cleaned_data["body"]
           post.categories = form.cleaned_data["categories"]
           post.save()
           messages.success(request,"Thank you for your contribution ! topic posted.")
           return HttpResponseRedirect('/')
        else:
            messages.error(request,form.errors)
            print(form.errors.as_data()) # here you print errors to terminal

    template = loader.get_template('write.html')
    return HttpResponse(template.render({'form':form},request))
