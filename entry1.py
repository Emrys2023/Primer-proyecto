import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.ventana1 = tk.Tk()

        self.dato1 = tk.IntVar(self.ventana1)
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=0, padx=10, pady=10)

        self.label1 = tk.Label(self.ventana1, text="+")
        self.label1.grid(column=1, row=0)

        self.dato2 = tk.IntVar(self.ventana1)
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=2, row=0, padx=10, pady=10)

        self.boton1 = tk.Button(self.ventana1, text="Sumar", command=self.sumar)
        self.boton1.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

        self.label2 = tk.Label(self.ventana1, text="Resultado", font=("arial", 20))
        self.label2.grid(column=0, row=4, columnspan=3, padx=10, pady=10)

        self.ventana1.mainloop()    

    def sumar(self):

        resultado = self.dato1.get() + self.dato2.get()
        self.label2.config(text=resultado)

app = Aplicacion()        