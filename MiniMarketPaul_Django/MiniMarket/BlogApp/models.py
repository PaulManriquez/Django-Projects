from django.db import models

from django.contrib.auth.models import User 
# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=50)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.Name     
    
class Post(models.Model):
    Title = models.CharField(max_length=50)
    Content = models.CharField(max_length=500)
    Image = models.ImageField(upload_to='BlogApp',null=True,blank=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Categories = models.ManyToManyField(Category)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.Title         