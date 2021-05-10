


def importe_total_carro(request):
    total=15
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total + ( float(value ["product_precio"] ) * value["product_cantidad"] )
            
    return {"total":total}

    
