class Persona():

    def inicializar(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print("nombre: ",self.nombre)

persona1 = Persona()
persona1.inicializar("Eliam")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Adrian")
persona2.imprimir()