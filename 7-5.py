class persona():

    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese edad: "))

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

class empleado(persona):

    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese el sueldo: "))

    def imprimir(self):
        super().imprimir()
        print("Sueldo: ", self.sueldo)

    def mayor300(self):
        if (self.sueldo > 3000):
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

persona1 = persona()
persona1.imprimir()
print("----------------------------------------------------")
empleado1 = empleado()
empleado1.imprimir()
empleado1.mayor300()