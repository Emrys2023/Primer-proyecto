import tkinter as tk

class Apliacion():

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Suma")

        self.frame1 = tk.LabelFrame(self.ventana1, text="Suma")
        self.frame1.grid(column=0, row=0, padx=80, pady=40)

        self.labelUsuario = tk.Label(self.frame1, text="Ingrese Usuario: ")
        self.labelUsuario.grid(column=0, row=0)

        self.labelContrasenia = tk.Label(self.frame1, text="Ingrese contraseña")
        self.labelContrasenia.grid(column=0, row=1)

        self.usuario = tk.StringVar(self.frame1)
        self.entryUsuario = tk.Entry(self.frame1, width=10, textvariable=self.usuario)
        self.entryUsuario.grid(column=1, row=0)

        self.contrasenia = tk.StringVar(self.frame1)
        self.entrycontrasenia = tk.Entry(self.frame1, width=10, textvariable=self.contrasenia, show="*")
        self.entrycontrasenia.grid(column=1, row=1)

        self.boton1 = tk.Button(self.frame1, text="Verificar", command=self.verificar)
        self.boton1.grid(column=0, row=2, columnspan=2)

        self.frame2 = tk.Frame(self.ventana1)
        self.frame2.grid(column=0, row=1, padx=80, pady=10)

        self.labelVerificar = tk.Label(self.frame2, text="Ingrese usuario y contraseña")
        self.labelVerificar.grid(column=0, row=0, padx=5, pady=5)

        self.ventana1.mainloop()

    def verificar(self):

        if self.usuario.get() == "juan" and self.contrasenia.get() == "abc123":
            self.labelVerificar.config(text="Usuario y contraseña correcta")
        else:
            self.labelVerificar.config(text="Usuario y contraseña incorrecta")


app = Apliacion()