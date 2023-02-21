"""Un banco tiene 3 clientes que pueden hacer depósitos y extracciones.
También el banco requiere que al final del día calcule la cantidad de 
dinero que hay depositado."""

class cliente():

    monto = 0

    def __init__(self):
        self.nombre = input("Ingrese nombre: ")   
   
    def deposito(self):
        self.depositar = int(input("Ingrese el monto a depositar: "))
        cliente.monto = cliente.monto + self.depositar

    def extraccion(self):
        self.extraer = int(input("Ingrese el monto a extraer: "))
        cliente.monto = cliente.monto - self.extraer


class operar(cliente):

    def ingresar_dinero(self):
        super().deposito()
        

    def retirar_dinero(self):
        super().extraccion()
          

cliente1 = operar()
cliente1.ingresar_dinero()
cliente1.retirar_dinero()
cliente2 = operar()
cliente2.ingresar_dinero()
cliente3 = operar() 
cliente3.ingresar_dinero()
print("\nSaldo: ", cliente.monto)