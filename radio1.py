import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.ventana1 = tk.Tk()
        
        self.seleccion = tk.IntVar(self.ventana1)
        self.ventana1.geometry("320x240")

        self.seleccion.set(2)
        self.radio1 = tk.Radiobutton(self.ventana1, text="Alejandro", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0, padx=5, pady=2)

        self.radio2 = tk.Radiobutton(self.ventana1, text="Mariano", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1, padx=5, pady=2)

        self.boton1 = tk.Button(self.ventana1, text="seleccionar nombre", command=self.confirmar)
        self.boton1.grid(column=0, row=2)

        self.ventana1.mainloop()

    def confirmar(self):
        if self.seleccion.get() == 1:
            self.ventana1.title("Alejandro")
        if self.seleccion.get() == 2:
            self.ventana1.title("Mariano")

app = Aplicacion()
