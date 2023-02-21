"""Un banco tiene 3 clientes que pueden hacer depósitos y extracciones.
También el banco requiere que al final del día calcule la cantidad de 
dinero que hay depositado."""

class cliente():
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
    
    def depositar(self, monto):
        self.monto = self.monto + monto

    def extraer(self, monto):
        self.monto = self.monto - monto

    def dev_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre,"Tiene en su cuenta: ", self.monto)


class banco():
    
    def __init__(self):
        self.cliente1 = cliente("Ale")
        self.cliente2 = cliente("Mecha")
        self.cliente3 = cliente("Celes")

    def operar(self):
        self.cliente1.depositar(200)
        self.cliente2.depositar(150)
        self.cliente3.depositar(100)
        self.cliente1.extraer(200)

    def depos_totales(self):
        self.total = self.cliente1.dev_monto() + self.cliente2.dev_monto() + self.cliente3.dev_monto()
        print("\nTotal de dinero en el banco: ", self.total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

banco1 = banco()
banco1.operar()
banco1.depos_totales()