# confeccionar una clase que administre una agenda personal. se debe almacenar
# el nombre de la personal, telefono, mail
# debe mostrar un menu con las siguientes opciones:
# 1- carga de un contacto en la agenda
# 2-listado completo de la agenda
# 3-consulta ingresando el nombre de la persona
# 4- modificacion de un telefono y mail
# 5- finalizar programa

import time

class agenda():

    def __init__(self):
        self.nombre = []
        self.telefono = []
        self.mail = []

    def menu(self):
        self.opcion = 0

        while(self.opcion != 5):
            print("\n")
            print("1- Cargar contactos")
            print("2- Listado completo de la agenda")
            print("3- Consultar el telefono y mail")
            print("4- Modificar telefono y mail")
            print("5- Finalizar programa")
            print("\n")

            self.opcion = int(input("ingrese una opcion: "))

            if self.opcion == 1:
                self.cargar()
            elif self.opcion == 2:
                self.listado()
                time.sleep(5)
            elif self.opcion == 3:
                self.consultar()
                time.sleep(5)
            elif self.opcion == 4:
                self.modificar()

    def cargar(self):
        for x in range(5):
            print("\n")
            nombre = input("ingrese un nombre: ")
            self.nombre.append(nombre)
            telefono = int(input("Ingrese numero de telefono: "))
            self.telefono.append(telefono)
            mail = input("Ingrese direccion de mail: ")
            self.mail.append(mail)

    def listado(self):
        print("\n")
        for x in range(5):
            print(self.nombre[x],"--", self.telefono[x],"--", self.mail[x])
            

    def consultar(self):
        print("\n")
        nombre = input("ingrese el nombre a buscar: ")
        for x in range(5):
            if nombre == self.nombre[x]:
                print("\n")
                print(self.nombre[x])
                print(self.telefono[x])
                print(self.mail[x])

    def modificar(self):
        print("\n")
        nombre = input("ingrese el nombre a buscar: ")
        for x in range(5):
            if nombre == self.nombre[x]:
                self.telefono[x] = int(input("ingrese el nuevo numero de telefono: "))
                self.mail[x] = input("Ingrese el nuevo mail: ")

agenda1 = agenda()
agenda1.menu()

