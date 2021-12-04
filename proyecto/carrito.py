
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito


    def agregar(self, paquete):
        id = str(paquete.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "paquete_id": paquete.id,
                "descripcion": paquete.descripcion,
                "precio": paquete.precio,
                "acumulado": paquete.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += paquete.precio
        
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, paquete):
        id = str(paquete.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, paquete):
        id = str(paquete.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -=1
            self.carrito[id]["acumulado"] -=paquete.precio

            if self.carrito[id]["cantidad"] <= 0: self.eliminar(paquete)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

