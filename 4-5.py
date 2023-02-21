class empleado():

    def __init__(self):
        self.nombre = input("ingrese el nombre: ")
        self.sueldo = float(input("ingrese el sueldo"))

    def imprimir(self):
        print("")
        print("Nombre: ", self.nombre)
        print("Sueldo: ", self.sueldo)
        print("")

    def impuesto(self):
        if (self.sueldo > 3000):
            print("Debe Pagar impuesto")

empleado1 = empleado()
empleado1.imprimir()
empleado1.impuesto()
