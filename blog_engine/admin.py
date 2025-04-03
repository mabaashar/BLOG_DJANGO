from django.contrib import admin
from blog_engine.models import Category, Post

# Register your models here.

class Category_admin(admin.ModelAdmin):
 list_display = ('name','image')

class Post_admin(admin.ModelAdmin):
 list_display = ('title','author','body','created_on','last_modified','categories','likes','shares',)

admin.site.register(Category,Category_admin)
admin.site.register(Post,Post_admin)
