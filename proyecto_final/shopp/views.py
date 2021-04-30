from django.shortcuts import render,HttpResponse
from service.models import service
from shopp.models import CategoryProduct,Tag,Products


def shop(request):
    productos=Products.objects.all()





    return render(request, "proyecto_final/shopp.html", {"producto":productos})

