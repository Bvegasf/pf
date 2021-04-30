from django.shortcuts import render,HttpResponse
from service.models import service







def shop(request):
    return render(request, "proyecto_final/shopp.html")
