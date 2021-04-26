from django.contrib import admin
from blog.models import Category, Post

class AdminPost(admin.ModelAdmin):
    readonly_fields=('created','update')

# Register your models here.

admin.site.register(Post,AdminPost)
admin.site.register(Category)