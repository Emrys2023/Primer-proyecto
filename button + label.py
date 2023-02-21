import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.ventana1 = tk.Tk()

        self.boton1 = tk.Button(self.ventana1, text="Juan", command=self.mostrarNombre)
        self.boton1.grid(column=0, row=0, padx=20, pady=10)

        self.label1 = tk.Label(self.ventana1, text="")
        self.label1.grid(column=0, row=1, padx=20, pady=10)

        self.ventana1.mainloop()

    def mostrarNombre(self):

        self.label1.config(text="juan")

app = Aplicacion()