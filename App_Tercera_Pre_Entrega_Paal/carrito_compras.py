import uuid 

class Carrito_Compras:
    def __init__(self, req):
        self.req = req
        self.session = req.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    
    def agregar(self, producto):

        id_1 = str(producto.id)

        if id_1 not in self.carrito.keys():
                self.carrito[id_1] = {
                    "producto_id": producto.id,
                    "titulo": producto.titulo,
                    "precio": producto.precio,
                    "acumulado": producto.precio,
                    "cantidad": 1,
                    "imagen": producto.imagen.url
                }

        else:
                self.carrito[id_1]["cantidad"] += 1
                self.carrito[id_1]["acumulado"] += producto.precio
        self.guardar_carrito()

    def eliminar(self, producto):
        id_1 = str(producto.id)
        if id_1 in self.carrito:
            del self.carrito[id_1]
            self.guardar_carrito()

    def restar(self, producto):
        id_1 = str(producto.id)
        if id_1 in self.carrito.keys():
            self.carrito[id_1]["cantidad"] -= 1
            self.carrito[id_1]["acumulado"] -= producto.precio
            if self.carrito[id_1]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

        

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def limpiar_carrito(self):
        self.session["carrito"] = {}
        self.session.modified = True

     