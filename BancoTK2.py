import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.cliente1 = "cliente1"
        self.cliente1Cont = "123"
        self.cliente2 = "cliente2"
        self.cliente2Cont = "124"
        self.cliente3 = "cliente3"
        self.cliente3Cont = "125"

        self.ventana = tk.Tk()
        self.ventana.title("Ingreso")
        
        self.label11 = tk.Label(self.ventana, text="Ingrese su usuario: ")
        self.label11.grid(column=0, row=0)

        self.label12 = tk.Label(self.ventana, text="Ingrese su contraseña: ")
        self.label12.grid(column=0, row=1)

        self.dato4 = tk.StringVar(self.ventana)
        self.entry4 = tk.Entry(self.ventana, width=10, textvariable=self.dato4)
        self.entry4.grid(column=1, row=0)

        self.dato5 = tk.StringVar(self.ventana)
        self.entry5 = tk.Entry(self.ventana, width=10, textvariable=self.dato5, show="*")
        self.entry5.grid(column=1, row=1)

        self.boton7 = tk.Button(self.ventana, text="Confirmar", command=self.confirmar)
        self.boton7.grid(column=1, row=2)

        self.ventana.mainloop()

    def confirmar(self):  

        if (self.dato4.get() == self.cliente1 and self.dato5.get() == self.cliente1Cont):
            self.ventana2("cliente1")
        elif (self.dato4.get() == self.cliente2 and self.dato5.get() == self.cliente2Cont):
            self.ventana2("cliente2")
        elif (self.dato4.get() == self.cliente3 and self.dato5.get() == self.cliente3Cont):
            self.ventana2("cliente3")
        else:
            self.ventana3 = tk.Tk()
            self.ventana3.title("Error")
            self.label13 = tk.Label(self.ventana3, text="ERROR AL INGRESAR USUARIO O CONTRASEÑA")
            self.label13.grid(column=0, row=0)
            self.ventana3.mainloop()     

    def ventana2(self, cliente):

        self.cliente = cliente

        self.resultado1 = 0
        
              
        self.ventana1 = tk.Tk()
        self.ventana1.title("Banco")

        self.label1 = tk.Label(self.ventana1, text=self.cliente)
        self.label1.grid(column=0, row=0)

        self.dato1 = tk.IntVar(self.ventana1)
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.boton1 = tk.Button(self.ventana1, text="Depositar", command=self.sumarCliente1)
        self.boton1.grid(column=2, row=0)

        self.boton4 = tk.Button(self.ventana1, text="  Retirar  ", command=self.restarCliente1)
        self.boton4.grid(column=3, row=0)

        self.label4 = tk.Label(self.ventana1, text="saldo =")
        self.label4.grid(column=0, row=4)

        self.label8 = tk.Label(self.ventana1, text="Saldo 0")
        self.label8.grid(column=1, row=4)

        self.ventana1.mainloop()

    def sumarCliente1(self):
        
        self.resultado1 = self.resultado1 + self.dato1.get()
        self.label8.config(text=self.resultado1)

    def restarCliente1(self):

        self.resultado1 = self.resultado1 - self.dato1.get()
        self.label8.config(text=self.resultado1)

app = Aplicacion()