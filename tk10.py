import tkinter as tk

class aplicacion():

    def __init__(self):
        self.valor = 1
        self.ventana = tk.Tk()
        self.ventana.title("boton y etiqueta")
        self.label1 = tk.Label(self.ventana, text=self.valor)
        self.label1.grid(column = 0, row = 0)
        self.boton = tk.Button(self.ventana, text = "incrementar", command=self.incrementar)
        self.boton.grid(column=0, row=1)
        self.boton2 = tk.Button(self.ventana, text="decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana.mainloop()

    def incrementar(self):
        self.valor = self.valor + 1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor = self.valor - 1
        self.label1.config(text=self.valor)

app = aplicacion()
