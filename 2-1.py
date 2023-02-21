class Persona():

    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)

    def mayor_18(self):
        if self.edad >= 18:
            print("Es mayor de edad")

persona1 = Persona()
persona1.inicializar("alejandro", 45)
persona1.imprimir()
persona1.mayor_18()

persona2 = Persona()
persona2.inicializar("pepe", 17)
persona2.imprimir()
persona2.mayor_18()  