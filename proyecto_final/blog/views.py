from django.shortcuts import render
from blog.models import Post, Category

# Create your views here.

def blog(request):
    post=Post.objects.all()
    return render(request, "proyecto_final/blog.html", {"post":post})


def category(request, category_id):

    categorys=Category.objects.get(id = category_id)
    posts= Post.objects.filter(category = categorys)

    return render(request, "proyecto_final/category.html", {"category":categorys, "post":posts})

