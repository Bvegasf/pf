from django.db import models
from typing_extensions import Required

# Create your models here.


class CategoryProduct(models.Model):
    name=models.CharField('nombre', max_length = 100, required = True)
    
    class Meta:
        db_table="Category_Product"
        verbose_name="Category_Product"
        verbose_name_plural="Category_Products"

    def __str__(self):
        return self.name





class Tag(models.Model):
    name=models.CharField('nombre',max_length= 80 , required = True)
    image=models.ImageField(upload_to="shopp")

    class Meta:
        db_table="Tag_Product"
        verbose_name="Tag_Product"
        verbose_name_plural="Tag_Products"
