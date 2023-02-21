""" Mostrar los botones del 1 al 5. cuando se presiona mostrar en un label todos
los botones presionados hasta el momento"""

import tkinter as tk

class botones():

    def __init__(self):

        self.dato1 = ""

        self.ventana1 = tk.Tk()
        self.ventana1.title("botones")
        self.boton1 = tk.Button(self.ventana1, text = "1", command=self.presionado1)
        self.boton1.grid(column=0, row=0)
        self.boton2 = tk.Button(self.ventana1, text = "2", command=self.presionado2)
        self.boton2.grid(column=1, row=0)
        self.boton3 = tk.Button(self.ventana1, text = "3", command=self.presionado3)
        self.boton3.grid(column=2, row=0)
        self.boton4 = tk.Button(self.ventana1, text = "4", command=self.presionado4)
        self.boton4.grid(column=3, row=0)
        self.boton5 = tk.Button(self.ventana1, text = "5", command=self.presionado5)
        self.boton5.grid(column=4, row=0)
        self.label1 = tk.Label(self.ventana1, text = "" )
        self.label1.grid(column=0, row= 1)

        self.ventana1.mainloop()

    def presionado1(self):
        self.dato1 = self.dato1 + "1"
        self.label1.config(text = self.dato1 )
        

    def presionado2(self):
        self.dato1 = self.dato1 + "2"
        self.label1.config(text = self.dato1 )
        

    def presionado3(self):
        self.dato1 = self.dato1 + "3"
        self.label1.config(text = self.dato1 )
        

    def presionado4(self):
        self.dato1 = self.dato1 + "4"
        self.label1.config(text = self.dato1 )
        

    def presionado5(self):
        self.dato1 = self.dato1 + "5"
        self.label1.config(text = self.dato1 )
        

boton = botones()