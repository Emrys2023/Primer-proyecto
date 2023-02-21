class operaciones():

    def __init__(self):
        self.num1 = float(input("ingrese un numero: "))
        self.num2 = float(input("ingrese otro numero: "))

    def suma(self):
        print("Suma: ",self.num1 + self.num2)

    def producto(self):
        print("Producto: ",self.num1 * self.num2)

    def resta(self):
        print("Resta: ",self.num1 - self.num2)

    def division(self):
        print("Division: ",self.num1 / self.num2)

operacion = operaciones()
operacion.suma()
operacion.resta()
operacion.producto()
operacion.division()