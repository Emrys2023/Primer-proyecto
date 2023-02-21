class inicio():
    
    def inicializar(self, nom, edad):
        self.nombre = nom
        self.edad = edad

    def imprimir(self):
        print("Nombre: ", self.nombre, self.edad)

persona = inicio()
persona.inicializar("Alejandro", 45)
persona.imprimir()