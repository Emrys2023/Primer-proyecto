class persona():

    def __init__(self):
        self.nombre = input("ingrese el nombre: ")

    def imprimir(self):
        print("nombre: ", self.nombre)

persona1 = persona()
persona1.imprimir()