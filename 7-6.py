class operaciones():
    
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar1(self):
        self.valor1 = int(input("ingrese el primer valor: "))

    def cargar2(self):
        self.valor2 = int(input("ingrese el segundo valor: "))

    def mostrar_resultado(self):
        print("El resultado es: ", self.resultado)

class Suma(operaciones):
    
    def operar(self):
        self.resultado = self.valor1 + self.valor2

class Resta(operaciones):
    
    def operar(self):
        self.resultado = self.valor1 - self.valor2

suma1 = Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
suma1.mostrar_resultado()

resta1 = Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
resta1.mostrar_resultado()