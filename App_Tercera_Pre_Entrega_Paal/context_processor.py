from .carrito_compras import Carrito_Compras

def importe_total(req):
        
      total = 0
      try:
            if req.user.is_authenticated:
                  if req.session.get("carrito"):
                        for key, value in req.session.get("carrito").items():
                              total += int(value["acumulado"])
      except:
            pass
         
      return {"importe_total": total}