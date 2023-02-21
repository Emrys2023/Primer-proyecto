class ejes():

    def __init__(self):
        self.x = int(input("Ingrese el valor de X: "))
        self.y = int(input("Ingrese el valor de Y: "))

    def cuadrante(self):
        if (self.x > 0 and self.y > 0):
            print("Pertenece al cuadrante 1")
        elif (self.x < 0 and self.y > 0):
            print("Pertenece al cuadrante 2")
        elif (self.x < 0 and self.y < 0):
            print("Pertenece al cuadrante 3")
        else:
            print("Pertenece al cuadrante 4")

ejes1 = ejes()
ejes1.cuadrante()