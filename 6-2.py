#Implementar la clase operaciones, se deben cargar dos valores enteros por
#teclado en el metodo __init__, calcular su suma, resta, multiplicacion y 
#division, cada uno en un metodo, imprimir los resultados.

class operaciones():

    def __init__(self):
        self.valor1 = int(input("Ingrese un valor: "))
        self.valor2 = int(input("Ingrese otro valor: "))
        

    def suma(self):
        self.suma = self.valor1 + self.valor2
        print("Suma: ", self.suma)

    def resta(self):
        self.resta = self.valor1 - self.valor2
        print("Resta: ", self.resta)

    def multiplicacion(self):
        self.multiplicacion = self.valor1 * self.valor2
        print("Multiplicacion: ", self.multiplicacion)

    def division(self):
        self.division = self.valor1 / self.valor2
        print("division: ", self.division)

operaciones1 = operaciones()
operaciones1.suma()
operaciones1.resta()
operaciones1.multiplicacion()
operaciones1.division()    