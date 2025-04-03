from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
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
#from blog.forms import CommentForm,NewBlogForm


# Homepage view
def blog_index(request,blog_category=None):
    #get all post
    posts = Post.objects.order_by('-created_on')
    #get all categories
    categories = Category.objects.all()

    #if no category is chosen
    if blog_category is None or blog_category=='':
        #posts = Post.objects.filter(categories_id=blog_category).order_by('-created_on')
        print("post category is none")
    else:
        posts = Post.objects.filter(categories__id=blog_category).order_by('-created_on')
        print("post category is ")
        print(blog_category)

    #paginator
    # Paginate items
    items_per_page = 6
    paginator = Paginator(posts, items_per_page)  # Show 6 posts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    template = loader.get_template('index.html')
    return HttpResponse(template.render({'blog_category':blog_category,'categories':categories,'posts':posts,"page_obj": page_obj,'paginator':paginator,'items_per_page':items_per_page},request))


def about(request):
    return render(request, 'about.html', {})