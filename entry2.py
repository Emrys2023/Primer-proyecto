import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.usuario = "yo"
        self.paaword = "123"

        self.ventana1 = tk.Tk()

        self.label1 = tk.Label(self.ventana1, text="Ingrese usuario: ")
        self.label1.grid(column=0, row=0, padx=10, pady=2)

        self.dato1 = tk.StringVar(self.ventana1)
        self.entry1 = tk.Entry(self.ventana1, width=15, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=10, pady=2)

        self.label2 = tk.Label(self.ventana1, text="Ingrese password: ")
        self.label2.grid(column=0, row=1, padx=10, pady=2)

        self.dato2 = tk.StringVar(self.ventana1)
        self.entry2 = tk.Entry(self.ventana1, width=15, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1, padx=10, pady=2)

        self.boton1 = tk.Button(self.ventana1, text="Confirmar", command=self.confirmar)
        self.boton1.grid(column=0, row=2, columnspan=2, padx=10, pady=2) 

        self.ventana1.mainloop()

    def confirmar(self):

        if self.dato1.get() == self.usuario and self.dato2.get() == self.paaword:

            self.ventana2 = tk.Tk()

            self.label3 = tk.Label(self.ventana2, text="acceso perminido", font=("Arial, 30"))
            self.label3.grid(column=0, row=0, padx=10, pady=5)

            self.ventana2.mainloop()
        else:
            self.ventana2 = tk.Tk()

            self.label3 = tk.Label(self.ventana2, text="acceso denegado", font=("Arial, 30"))
            self.label3.grid(column=0, row=0, padx=10, pady=5)

            self.ventana2.mainloop()

app = Aplicacion()