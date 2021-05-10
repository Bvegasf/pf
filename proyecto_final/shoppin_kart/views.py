from django.shortcuts import render
from shoppin_kart.shopping import Carro
from shopp.models import Products
from django.shortcuts import redirect

# Create your views here.


#class agregar productos al carro de compras

def add(request,product_id):
    carro=Carro(request)

    producto=Products.objects.get(id= product_id)

    carro.add_product(product=producto)

    return redirect("shop")


def delette(request,product_id):

    carro=Carro(request)

    producto=Products.objects.get(id=product_id)


    carro.delete_product(product=producto)

    return redirect("shop")



def rest(request,product_id):

    carro=Carro(request)

    producto=Products.objects.get(id=product_id)

    carro.rest_product(product=producto)

    return redirect("shop")

def clean(request, product_id):
    carro=Carro(request)

    carro.clean_kart()

    return redirect("shop")