import tkinter as tk


class Aplicacion():

    def __init__(self):
        
        self.ventana1 = tk.Tk()
        self.label1 = tk.Label(self.ventana1, text= "Ingrese un numero:")
        self.label1.grid(column=0, row=0)

        self.dato = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        
        self.entry1.grid(column=0, row=1)

        self.boton1 = tk.Button(self.ventana1, text="calcular cuadrado", command=self.calcularcuadrado)
        self.boton1.grid(column=0, row=2)
        self.label2 = tk.Label(self.ventana1, text="Resultado")
        self.label2.grid(column=0, row=3)

        self.ventana1.mainloop()

    def calcularcuadrado(self):
        valor = int(self.dato.get())
        cuadrado = valor * valor
        self.label2.config(text=cuadrado)



app = Aplicacion()

