from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/',default='default.png')
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',default='default_2.png')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0,null=False)
    shares = models.IntegerField(default=0,null=False)
    def __str__(self):
        return self.title

