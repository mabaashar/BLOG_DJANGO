from django.urls import path

from . import views

urlpatterns = [
    path("category/", views.categories, name="category"),
    path("chosen_category/<int:chosen_category>", views.posts_by_category, name="posts_by_category"),
    path("blog_post<int:chosen_post>", views.blog_post, name="blog_post"),
    path("write/", views.write, name="write"),
]