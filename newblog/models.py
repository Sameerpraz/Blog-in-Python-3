from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date,datetime
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return f"{self.id}: {self.name}"

    def get_absolute_url(self):
        # return reverse('path',args) 
        return reverse('home')
        
        

class Post(models.Model):
    title=models.CharField(max_length=25)
    title_tag=models.CharField(max_length=25,default='Hot News')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    post_date=models.DateField(auto_now_add=True)
    body=models.TextField()

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author} {self.body}"
        # return {{self.id}} self.title +'by'+ str(self.author)

    def get_absolute_url(self):
        # return reverse('path',args)
        return reverse('view_article', args=[str(self.id)])
        
        
