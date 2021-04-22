from django.db import models
from django.db.models.base import Model

# Create your models here.

class service(models.Model):
    title = models.CharField(max_length=50, unique = True )
    description= models.CharField(max_length= 10)
    image= models.ImageField()
    created= models.DateTimeField(auto_now_add= True)
    update= models.DateTimeField(auto_now_add= True)

    class Meta:
        db_table= 'max_store_service'
        verbose_name= 'service'
        verbose_name= 'services'

    def __str__(self):
        return self.title

        

