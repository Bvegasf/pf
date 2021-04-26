from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    name = models.CharField(unique = True, max_length= 100 )
    image = models.ImageField(upload_to = "blog")


    class Meta:
        db_table='max_store_category_blog'
        verbose_name='category'
        verbose_name_plural= 'categorys'


    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length= 200)
    content=models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to = "blog", null=True, blank= True)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    category =models.ManyToManyField(Category)
    created= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now_add= True)

    class Meta:
        db_table='max_store_post'
        verbose_name= 'post'
        verbose_name_plural= 'posts'

    def __str__(self):
        return self.title
