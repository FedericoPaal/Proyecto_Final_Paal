from .carrito_compras import Carrito_Compras

def importe_total(req):
        
      total = 0

      if req.user.is_authenticated:
            if req.session.get("carrito"):
                  for key, value in req.session.get("carrito").items():
                        total += int(value["acumulado"])

         
      return {"importe_total": total}