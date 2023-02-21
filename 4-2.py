class triangulos():

#    def lados (self, lado1, lado2, lado3):
#        self.lado1 = lado1
#        self.lado2 = lado2
#        self.lado3 = lado3

    def datos(self):
        self.lado1 = int(input("ingrese el primer lado: "))
        self.lado2 = int(input("ingrese el segundo lado: "))
        self.lado3 = int(input("ingrese el tercer lado: "))

    def mayor(self):
        if (self.lado1 > self.lado2 and self.lado1 > self.lado3):
            print("el lado mayor es: ", self.lado1)
        elif(self.lado2 > self.lado1 and self.lado2 > self.lado3):
            print("el lado mayor es: ", self.lado2)
        else:
            print("el lado mayor es: ", self.lado3)

    def equilatero(self):
        if (self.lado1 == self.lado2 and self.lado1 == self.lado3):
            print("Es equilatero")
        else:
            print("no es equilatero")

triangulo = triangulos()
triangulo.datos()
triangulo.mayor()
triangulo.equilatero()


