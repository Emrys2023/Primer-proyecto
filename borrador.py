import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.ventana1 = tk.Tk()
        self.ventana1.title("Principal")
        self.ventana1.geometry('200x100')

        self.botonSumar = tk.Button(self.ventana1, text="Sumar")
        self.botonSumar.grid(column=0, row=0)

        self.botonRestar = tk.Button(self.ventana1, text="Restar" )
        self.botonRestar.grid(column=1, row=0)

        self.botonMult = tk.Button(self.ventana1, text="Multiplicar")
        self.botonMult.grid(column=2, row=0)

        self.botonDiv = tk.Button(self.ventana1, text="Dividir")
        self.botonDiv.grid(column=3, row=0)
        
        self.ventana1.mainloop()

class suma(Aplicacion):

    def __init__(self):
        super().__init__()
        self.ventana2 = tk.Tk()
        self.ventana2.title("Operar")
        self.label1 = tk.Label(self.ventana2, text="Ingrese valor 1")

        self.ventana2.mainloop()

app = Aplicacion()
app2 = suma()