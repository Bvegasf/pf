from django.shortcuts import render,HttpResponse
from service.models import service


# Create your views here.

def home(request):

    return render(request, "proyecto_final/home.html")







def shop(request):
    return render(request, "proyecto_final/shopp.html")


def blog(request):
    return render(request, "proyecto_final/blog.html")


def contacus(request):
    return render(request, "proyecto_final/contacus.html")
    