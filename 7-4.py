"""
Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad 
en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre 
y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor 
antigüedad en el club."""


class socio():
    
    def __init__(self):
        self.nombre = input("ingrese el nombre: ")
        self.antiguedad = int(input("ingrese la antiguedad: "))

    def retorno(self):
        return self.antiguedad

    def imprimir(self):
        print("\n",self.nombre,"tiene una antiguedad de ",self.antiguedad, "años, es el socio/a con mayor antiguedad\n")

class club():

    def __init__(self):
        self.socio1 = socio()
        self.socio2 = socio()
        self.socio3 = socio()

    def mayor(self):
        if self.socio1.retorno() > self.socio2.retorno() and self.socio1.retorno() > self.socio3.retorno():
            self.socio1.imprimir()
        elif self.socio2.retorno() > self.socio1.retorno() and self.socio2.retorno() > self.socio3.retorno():
            self.socio2.imprimir()
        else:
            self.socio3.imprimir()

club1 = club()
club1.mayor()