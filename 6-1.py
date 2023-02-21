# Desarrollar una clase que represente un cuadrado y tenga los siguientes
# metodos: inicializar el valor del lado llegando como parametro el metodo
# __init__ (definir un atributo llamado lado), imprimir su metodo y su 
# superficie.

class cuadrado():

    def __init__(self, ):
        self.lado = int(input("Ingrese el valor del lado: "))

    def perimetro(self):
        self.perimetro = self.lado * 4
        print("El perimetro es: ", self.perimetro)

    def superficie(self):
        self.superficie = self.lado * self.lado
        print("El superficie es: ", self.superficie)

cuadrado1 = cuadrado()
cuadrado1.perimetro()
cuadrado1.superficie() 