

# clase de funcionalidad del carrito

class Carro:

    # constructor que maneja sesiones del carrito de compra
    # si el carrito no ha sio creado, se crea, si existe, se iguala al carro existente.


    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")

        if not carro:
            carro=self.session["carro"]={}


        else:
            carro=carro

    #funcion para agregar productos

    def add_product(self,product):

        #si el producto no existe en el carro ve agrega

        if (str(product.id) not in self.carro.keys()):
            self.carro[product.id]={
                "product_id":product.id,
                "product_nombre":product.name,
                "product_precio":product.price,
                "product_cantidad":1,
                "product_image":product.image.url



            }

        #si el producto exite, se suma una cantidad.

        else:
            for key , value in self.carro.items():
                if key==str(product.id):
                    value["product_cantidad"]=value["product_cantidad"] + 1
                    break

        self.save_carro()

    #guardar estado del carrito

    def save_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True


    #eliminar producto(toda la cantidad guardada)

    def delete_product(self, product):
        product.id=str(product.id)
        if product.id in self.carro:
            del self.carro[product.id]
            self.save_carro()

    #restar una unidad del producto

    def rest_product(self,product):
        for key, value in self.carro.items():
            if key==str(product.id):
                value["product_cantidad"]=value["product_caantidad"]-1
                if value["product_cantidad"] < 1:
                    self.delete_product(product)
                break

        self.save.carro()

    def clean_kart(self,product):
        self.session["carro"]={}
        self.session.modified=True


