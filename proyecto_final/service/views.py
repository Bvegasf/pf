from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from service.models import service


# Create your views here.
def services(request):


    serv = service.objects.all()


    return render(request, "service.html", {"serv":serv})