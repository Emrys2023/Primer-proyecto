""" confeccionar un programa que permita ingresar el nombre del usuario en un control entry y cuando 
presionamos el boton mostrar el nombre ingresado en el titulo de la ventana"""

import tkinter as tk

class aplicacion():

    def __init__(self):

        

        self.ventana1 = tk.Tk()
        self.ventana1.title("Nombre")
        self.ventana1.geometry('500x500')        
        self.label1 = tk.Label(self.ventana1, text="Ingrese el nombre: ")
        self.label1.grid(column=0, row=0)

        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.boton1 = tk.Button(self.ventana1, text="cambiar nombre", command=self.mostrar_nombre)
        self.boton1.grid(column=0, row=2)

        self.ventana1.mainloop()

    def mostrar_nombre(self):
        dato = str(self.dato1.get())
        self.ventana1.title(dato)

app = aplicacion()