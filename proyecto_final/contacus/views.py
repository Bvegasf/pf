from django.shortcuts import redirect, render
from contacus.forms import FormcContact
from django.core.mail import EmailMessage
from django.conf import settings


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

            correo=EmailMessage("Contacto App Django", "El usuario: {} {} con la direccion de correo electronico {}, escribe el siguiente mensaje: \n\n {} ".format(nombre,apellido,email,mensaje) , "" , ["brayanjovegas@gmail.com"], reply_to=[email])
            try:
                correo.send()
                return redirect("/contacus/?Correcto")

            except:
                return redirect("/contacus/?Incorrecto")


        

            


    return render(request, "proyecto_final/contacus.html",{"Formulario":forms_contacus})