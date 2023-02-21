import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.ventana = tk.Tk()

        self.label1 = tk.Label(self.ventana, text="Ingrese nombre")
        self.label1.grid(column=0, row=0, padx=20, pady=10)

        self.dato1 = tk.IntVar(self.ventana)
        self.entry1 = tk.Entry(self.ventana, width=15, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=20, pady=10)

        self.ventana.mainloop()

class Usuario():

    

app = Aplicacion()