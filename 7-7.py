class operar():

    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar1(self):
        self.valor1 = int(input("Ingrese un valor: "))

    def cargar2(self):
        self.valor2 = int(input("Ingrese otro valor: "))

    def operar(self):
        pass

    def mostrar_resultado(self):
        print("El resultado es: ", self.resultado)

class suma(operar):

    def operar(self):
        self.resultado = self.valor1 + self.valor2

class resta(operar):

    def operar(self):
        self.resultado = self.valor1 - self.valor2

class division(operar):

    def operar(self):
        self.resultado = self.valor1 / self.valor2

class multiplicacion(operar):

    def operar(self):
        self.resultado = self.valor1 * self.valor2

suma1 = suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
suma1.mostrar_resultado()
print("")

resta1= resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
resta1.mostrar_resultado()
print("")

division1 = division()
division1.cargar1()
division1.cargar2()
division1.operar()
division1.mostrar_resultado()
print("")

multiplicacion1 = multiplicacion()
multiplicacion1.cargar1()
multiplicacion1.cargar2()
multiplicacion1.operar()
multiplicacion1.mostrar_resultado()