import random

class dado():

    def tirar(self):
        self.valor = random.randint(1,6)

    def imprimir(self):
        print("valor del dado: ", self.valor)

    def retornar(self):
        return self.valor

class juego_de_dados():

    def __init__(self):
        self.dado1 = dado()
        self.dado2 = dado()
        self.dado3 = dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()

        self.dado2.tirar()
        self.dado2.imprimir()

        self.dado3.tirar()
        self.dado3.imprimir()

        if (self.dado1.retornar() == self.dado2.retornar() and self.dado1.retornar() == self.dado3.retornar()):
            print("\ngano!!!\n")
        else:
            print("\nPerdio!!!\n")
juego1 = juego_de_dados()
juego1.jugar()
