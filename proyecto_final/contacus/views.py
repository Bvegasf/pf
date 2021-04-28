from django.shortcuts import render
from contacus.forms import FormcContact


# Create your views here.
def contacus(request):

    forms_contacus=FormcContact()

    return render(request, "proyecto_final/contacus.html",{"Formulario":forms_contacus})