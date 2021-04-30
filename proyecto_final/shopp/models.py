from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class CategoryProduct(models.Model):
    name=models.CharField('nombre', max_length = 100)
    
    class Meta:
        db_table="Category_Product"
        verbose_name="Category"
        verbose_name_plural="Categorys"

    def __str__(self):
        return self.name





class Tag(models.Model):
    name=models.CharField('nombre',max_length= 80)
    image=models.ImageField(upload_to="shopp", null= True)

    class Meta:
        db_table="Tag_Product"
        verbose_name="Tag"
        verbose_name_plural="Tags"

    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField('name', max_length=200)
    image=models.ImageField('image', upload_to="shopp", null=True)
    price=models.FloatField('price', max_length=200)
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, blank=True, null=True )
    tag=models.ForeignKey(Tag,on_delete=CASCADE, blank=True, null=True)


    class Meta:
        db_table="Products"
        verbose_name="Product"
        verbose_name_plural="Products"


    def __str__(self):
        return f'Producto: {self.name}  Precio: {self.price} Disponibilidad: {self.is_available}'

