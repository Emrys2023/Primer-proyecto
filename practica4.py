import tkinter as tk
from tkinter import ttk

class Aplicacion():

    def __init__(self):

        #self.total = 0
        self.usuario1 = "Cliente 1"
        self.usuario2 = "Cliente 2"
        self.usuario3 = "Cliente 3"
        self.contrasenia1 = "123"
        self.contrasenia2 = "124"
        self.contrasenia3 = "125"

        self.ventanaLogin = tk.Tk()
        self.ventanaLogin.title("Login")

        self.frame1 = ttk.LabelFrame(self.ventanaLogin, text="Login")
        self.frame1.grid(column=0, row=0, padx=40, pady=20)

        self.labelUsuario = ttk.Label(self.frame1, text="Ingrese Usuario ")
        self.labelUsuario.grid(column=0, row=0, padx=4, pady=2)

        self.labelPassword = ttk.Label(self.frame1, text="Ingrese Contraseña ")
        self.labelPassword.grid(column=0, row=1, padx=4, pady=2)

        self.dato1 = tk.StringVar(self.frame1)
        self.entryUsuario = ttk.Entry(self.frame1, width=15, textvariable=self.dato1)
        self.entryUsuario.grid(column=1, row=0, padx=4, pady=2)

        self.dato2 = tk.StringVar(self.frame1)
        self.entryPassword = ttk.Entry(self.frame1, width=15, textvariable=self.dato2, show="•")
        self.entryPassword.grid(column=1, row=1, padx=4, pady=2)

        self.botonLogin = ttk.Button(self.frame1, text="Ingresar", command=self.ingresar)     
        self.botonLogin.grid(column=0, row=2, columnspan=2, padx=4, pady=15)  

        self.ventanaLogin.mainloop()

    def ingresar(self):

        if self.dato1.get() == self.usuario1 and self.dato2.get() == self.contrasenia1:
            self.operar(self.usuario1)
        elif self.dato1.get() == self.usuario2 and self.dato2.get() == self.contrasenia2:
            self.operar(self.usuario2)
        elif self.dato1.get() == self.usuario3 and self.dato2.get() == self.contrasenia3:
            self.operar(self.usuario3)
        else:
            self.ventanaError = tk.Tk()
            self.ventanaError.title("Error")

            self.frame3 = ttk.LabelFrame(self.ventanaError, text="Error")
            self.frame3.grid(column=0, row=0, padx=10, pady=5)

            self.labelError = ttk.Label(self.frame3, text="Ingreso de Usuario y Contraseña incorrecto", font=("Arial" ,14))
            self.labelError.grid(column=0, row=0, padx=10, pady=5)
            self.labelError.configure(foreground="red")

            self.ventanaError.mainloop()            

    def operar(self, usuario):

        self.total = 0
        
        self.ventanaOperar = tk.Tk()
        self.ventanaOperar.title("Operar")                
        
        self.frame2 = ttk.LabelFrame(self.ventanaOperar, text=usuario)
        self.frame2.grid(column=0, row=0, padx=40, pady=20)

        self.label1 = ttk.Label(self.frame2, text="Ingrese el monto")
        self.label1.grid(column=0, row=0, padx=20, pady=10)

        self.valor1 = tk.IntVar(self.frame2)
        self.entryOperar = ttk.Entry(self.frame2, width=15, textvariable=self.valor1)
        self.entryOperar.grid(column=1, row=0, padx=20, pady=10)

        self.botonDepositar = ttk.Button(self.frame2, text="Depositar", command=self.depositar)
        self.botonDepositar.grid(column=0, row=1, padx=20, pady=10)

        self.botonExtraer = ttk.Button(self.frame2, text="Extraer", command=self.extraer)
        self.botonExtraer.grid(column=1, row=1, padx=20, pady=10)

        self.frame4 = ttk.LabelFrame(self.ventanaOperar, text="Saldo")
        self.frame4.grid(column=0, row=1, padx=20, pady=10)

        self.label2 = ttk.Label(self.frame4, text="Saldo 0", font=("arial", 30))
        self.label2.grid(column=0, row=0, padx=10, pady=5)

        self.ventanaOperar.mainloop()

    def depositar(self):
        self.total += self.valor1.get()
        self.imprimir()

    def extraer(self):
        self.total -= self.valor1.get()
        self.imprimir()

    def imprimir(self):
        if self.total < 0:
            self.label2.configure(foreground="red")

        self.label2.config(text=self.total)

app = Aplicacion()