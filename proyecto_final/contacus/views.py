from django.shortcuts import redirect, render
from contacus.forms import FormcContact


# Create your views here.
def contacus(request):

    forms_contacus=FormcContact()

    if request.method=="POST":
        forms_contacus=FormcContact(data=request.POST)
        if forms_contacus.is_valid():
            nombre=request.POST.get("name")
            apellido=request.POST.get("last_name")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")

            return redirect("/contacus/?Correcto")

    return render(request, "proyecto_final/contacus.html",{"Formulario":forms_contacus})