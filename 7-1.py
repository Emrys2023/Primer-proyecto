from re import A


class socio():
    
    def __init__(self, nombre, antiguedad):
        self.nombre = nombre
        self.antiguedad = antiguedad



class club():
    
    def __init__(self):
        self.nombre1 = input("Nombre: ")
        self.nombre2 = input("nombre: ")
        self.nombre3 = input("nombre: ")
        self.antiguedad1 = int(input("Antiguedad: "))
        self.antiguedad2 = int(input("Antiguedad: "))
        self.antiguedad3 = int(input("Antiguedad: ")) 
        

    def mayor_antiguedad(self):
        if (self.antiguedad1 > self.antiguedad2 and self.antiguedad1 > self.antiguedad3):
            print("mayor antiguedad: ", self.nombre1)
        elif (self.antiguedad2 > self.antiguedad1 and self.antiguedad2 > self.antiguedad3):
            print("mayor antiguedad: ", self.nombre2)
        else:
            print("mayor antiguedad: ", self.nombre3)

club1 = club()
club1.mayor_antiguedad()


