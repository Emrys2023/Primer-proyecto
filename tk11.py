""" Disponer dos objetos de la clase Button con la etiqueta "varon" y "Mujer"
al presionarse mostrar en la barra de titulo "boton presionado". """

import tkinter as tk

class genero():

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Genero")
        self.boton1 = tk.Button(self.ventana1, text = "Varon", command= self.varon)
        self.boton1.grid(column=0, row=0)
        self.boton2 = tk.Button(self.ventana1, text = "Mujer", command= self.mujer)
        self.boton2.grid(column=0, row=1)
        self.ventana1.mainloop()

    def varon(self):
        self.ventana1.title("Varon")

    def mujer(self):
        self.ventana1.title("Mujer")

gen = genero()
