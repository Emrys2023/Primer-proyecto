class Cuenta():
    
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto

    def imprimir(self):
        print("nombre: ", self.nombre)
        print("monto", self.monto)

    

class Caja_Ahorro(Cuenta):
    
    def mostrar_datos(self):
        super().imprimir()


class Plazo_Fijo(Cuenta):
    
    def __init__(self,nombre, monto, plazo, interes):
        super().__init__(nombre, monto)
        self.plazo = plazo
        self.interes = interes

    def total(self):
        self.total = self.monto+(self.monto*((self.interes/365)*self.plazo)/100)
        super().imprimir()
        print("Total con interes: ", self.total)

ahorro1 = Caja_Ahorro("Ale", 200)
ahorro1.mostrar_datos()

plazo1 = Plazo_Fijo("Ale", 200, 30, 50)
plazo1.total()


