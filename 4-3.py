class persona():

    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayor(self):
        if (self.edad >= 18):
            print("Es mayor de edad")
        else:
            print("no es mayor de edad")

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

persona1 = persona()
persona1.inicializar("Alejandro", 45)
persona1.imprimir()
persona1.mayor()

persona1 = persona()
persona1.inicializar("Celeste", 17)
persona1.imprimir()
persona1.mayor()