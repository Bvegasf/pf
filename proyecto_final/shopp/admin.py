from django.contrib import admin
from shopp.models import CategoryProduct,Tag,Products

# Register your models here.
admin.site.register(CategoryProduct)
admin.site.register(Tag)
admin.site.register(Products)