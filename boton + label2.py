import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.valor = 0

        self.ventana1 = tk.Tk()

        self.boton1 = tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=0, padx=10, pady=10)

        self.boton2 = tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=1, row=0, padx=10, pady=10)

        self.label1 = tk.Label(self.ventana1, text="0",)
        self.label1.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        self.ventana1.mainloop()

    def incrementar(self):

        self.valor = self.valor + 1
        self.label1.config(text=str(self.valor))

    def decrementar(self):

        self.valor = self.valor - 1
        self.label1.config(text=str(self.valor))

app = Aplicacion()