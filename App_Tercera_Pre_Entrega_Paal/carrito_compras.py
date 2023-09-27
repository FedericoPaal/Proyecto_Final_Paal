from .models import Novedad, Libro, Merchandising

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


    def agregar(self, libro):

        id_1 = str(libro.id)

        if id_1 not in self.carrito.keys():
                self.carrito[id_1] = {
                    "producto_id": libro.id,
                    "titulo": libro.titulo,
                    "acumulado": libro.precio,
                    "cantidad": 1,
                    "imagen": libro.imagen.url
                }

        else:
                self.carrito[id_1]["cantidad"] += 1
                self.carrito[id_1]["acumulado"] += libro.precio
        self.guardar_carrito


    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, libro):
        id_1 = str(libro.id)
        if id_1 in self.carrito:
            del self.carrito[id_1]
            self.guardar_carrito()

    def restar_producto(self, libro):
        id_1 = str(libro.id)
        if id_1 in self.carrito.keys():
            self.carrito[id_1]["cantidad"] -= 1
            self.carrito[id_1]["acumulado"] -= libro.precio
            if self.carrito[id_1]["cantidad"] <= 0:
                self.eliminar(libro)
            self.guardar_carrito()

    def limpiar_carrito(self):
        self.session["carrito"] = {}
        self.session.modified = True

     