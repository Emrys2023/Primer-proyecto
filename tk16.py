"""Disponer dos controles de tipo Entry para el ingreso de enteros. 
Mediante dos controles Radiobutton permitir seleccionar si queremos 
sumarlos o restarlos. Al presionar un botón mostrar el resultado de 
la operación seleccionada."""

import tkinter as tk

class aplicacion():

    def __init__(self):

                
        self.ventana1 = tk.Tk()
        self.ventana1.title("Suma y Resta")
        self.ventana1.geometry('500x500')

        self.label1 = tk.Label(self.ventana1, text="Ingrese el primer numero:  ")
        self.label1.grid(column=0, row=0)

        self.label2 = tk.Label(self.ventana1, text="Ingrese el segundo numero: ")
        self.label2.grid(column=0, row=1)
        
        self.dato1 = tk.IntVar(self.ventana1)
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.dato2 = tk.IntVar(self.ventana1)
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        self.seleccion = tk.IntVar(self.ventana1)
        self.seleccion.set(2)
        self.radio1 = tk.Radiobutton(self.ventana1, text="sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column= 0 , row= 2)

        self.radio2 = tk.Radiobutton(self.ventana1, text="Restar", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=3)

        self.boton1 = tk.Button(self.ventana1, text = "Operar", command=self.operar)
        self.boton1.grid(column=0, row=4)

        self.label3 = tk.Label(self.ventana1, text="")
        self.label3.grid(column=0, row=5)

        self.ventana1.mainloop()

    def operar(self):
        dato1 = self.dato1.get()
        dato2 = self.dato2.get()
        
        if (self.seleccion.get() == 1):
            self.resulatdo = dato1 + dato2
            self.label3.config(text=self.resulatdo)
            
        if (self.seleccion.get() == 2):
            self.resulatdo = dato1 - dato2
            self.label3.config(text=self.resulatdo)
               
        
app = aplicacion()