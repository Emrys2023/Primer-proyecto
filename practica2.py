import tkinter as tk

class Aplicacion():

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Colores")
        self.ventana1.geometry("640x480")

        self.seleccion = tk.IntVar()
        self.seleccion.set(3)
        self.radio1 = tk.Radiobutton(self.ventana1, variable=self.seleccion, text="rojo", value=1)
        self.radio1.grid(column=0, row=0)

        self.radio2 = tk.Radiobutton(self.ventana1, variable=self.seleccion, text="azul", value=2)
        self.radio2.grid(column=0, row=1)

        self.radio1 = tk.Radiobutton(self.ventana1, variable=self.seleccion, text="verde", value=3)
        self.radio1.grid(column=0, row=2)

        self.boton1 = tk.Button(self.ventana1, text="Cambiar", command=self.seleccionButton)
        self.boton1.grid(column=0, row=3)

        self.ventana1.mainloop()

    def seleccionButton(self):

        if self.seleccion.get() == 1:
            self.ventana1.configure(bg="red")
        elif self.seleccion.get() == 2:
            self.ventana1.configure(bg="green")
        elif self.seleccion.get() == 3:
            self.ventana1.configure(bg="blue")        

app = Aplicacion()