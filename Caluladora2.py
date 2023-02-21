import tkinter as tk, re
from tkinter import Text, ttk, END, Button

class Calculadora ():

    def __init__(self):

        self.dato1 = ""
        self.igual = False
        
        
        self.ventana1 = tk.Tk()
        self.ventana1.title("Calculadora")

        self.labelFrame1 = ttk.LabelFrame(self.ventana1, text="Calculadora 2000")
        self.labelFrame1.grid(column=0, row=0, padx=5, pady=5)

        self.texto1 = Text (self.labelFrame1, state="disabled", width=20, height=2, background="gray83", foreground="black", font=("helvetica", 15))
        self.texto1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.labelFrame2 = ttk.LabelFrame(self.ventana1)
        self.labelFrame2.grid(column=0, row=1, padx=5, pady=5)

        self.boton7 = tk.Button(self.labelFrame2, text="7", width=7, height=2, command=self.presionar7)
        self.boton7.grid(column=0, row=0)

        self.boton8 = tk.Button(self.labelFrame2, text="8", width=7, height=2, command=self.presionar8)
        self.boton8.grid(column=1, row=0)

        self.boton9 = tk.Button(self.labelFrame2, text="9", width=7, height=2, command=self.presionar9)
        self.boton9.grid(column=2, row=0)

        self.boton4 = tk.Button(self.labelFrame2, text="4", width=7, height=2, command=self.presionar4)
        self.boton4.grid(column=0, row=1)

        self.boton5 = tk.Button(self.labelFrame2, text="5", width=7, height=2, command=self.presionar5)
        self.boton5.grid(column=1, row=1)

        self.boton6 = tk.Button(self.labelFrame2, text="6", width=7, height=2, command=self.presionar6)
        self.boton6.grid(column=2, row=1)

        self.boton1 = tk.Button(self.labelFrame2, text="1", width=7, height=2, command=self.presionar1)
        self.boton1.grid(column=0, row=2)

        self.boton2 = tk.Button(self.labelFrame2, text="2", width=7, height=2, command=self.presionar2)
        self.boton2.grid(column=1, row=2)

        self.boton3 = tk.Button(self.labelFrame2, text="3", width=7, height=2, command=self.presionar3)
        self.boton3.grid(column=2, row=2)

        self.botonPunto = tk.Button(self.labelFrame2, text=".", width=7, height=2, command=self.presionarPunto)
        self.botonPunto.grid(column=0, row=3)

        self.boton0 = tk.Button(self.labelFrame2, text="0", width=7, height=2, command=self.presionar0)
        self.boton0.grid(column=1, row=3)

        self.botonMas = tk.Button(self.labelFrame2, text="+", width=7, height=2, command=self.presionarMas)
        self.botonMas.grid(column=2, row=3)
        
        self.botonRetro = tk.Button(self.labelFrame2, text="=", width=7, height=2, command=self.presionarResultado)
        self.botonRetro.grid(column=3, row=0)

        self.botonDiv = tk.Button(self.labelFrame2, text="/", width=7, height=2, command=self.presionarDiv)
        self.botonDiv.grid(column=3, row=1)

        self.boton0 = tk.Button(self.labelFrame2, text="*", width=7, height=2, command=self.presionarMult)
        self.boton0.grid(column=3, row=2)

        self.botonMenos = tk.Button(self.labelFrame2, text="-", width=7, height=2, command=self.presionarRestar)
        self.botonMenos.grid(column=3, row=3)

        self.botonBorrar = tk.Button(self.labelFrame2, text="Borrar", width=30, height=2, command=self.borrarPantalla)
        self.botonBorrar.grid(column=0,row=4, columnspan=4)        

        self.ventana1.mainloop()

    def presionar(self, numero):

        self.dato1 += str(numero)
        self.mostrarEnPantalla(numero)
        self.presionarIgual(self.igual)      

    def presionar1(self):

        self.presionar("1")

    def presionar2(self):

        self.presionar("2")

    def presionar0(self):

        self.presionar("0")

    def presionar3(self):

        self.presionar("3")

    def presionar3(self):

        self.presionar("3")

    def presionar4(self):

        self.presionar("4")

    def presionar5(self):

        self.presionar("5")

    def presionar6(self):

        self.presionar("6")

    def presionar7(self):

        self.presionar("7")

    def presionar8(self):

        self.presionar("8")

    def presionar9(self):

        self.presionar("9")

    def presionarPunto(self):

        self.presionar(".")

    def presionarMas(self):

        self.presionar("+")

    def presionarRestar(self):

        self.presionar("-")

    def presionarMult(self):

        self.presionar("*")

    def presionarDiv(self):

        self.presionar("/")

    def presionarResultado(self):

        self.igual = True
        self.presionarIgual(self.igual)

    def presionarIgual(self, condicion):

        if condicion == True:

            resultado = str(eval(self.dato1))
            self.dato1 = ""
            self.borrarPantalla()
            self.mostrarEnPantalla(resultado)
            self.igual = False

    def mostrarEnPantalla(self, valor):

        self.texto1.configure(state="normal")
        self.texto1.insert(END, valor)
        self.texto1.configure(state="disabled")
        return

    def borrarPantalla(self):

        self.texto1.configure(state="normal")        
        self.texto1.delete("1.0",END)
        self.texto1.configure(state="disabled")

calculadora1 = Calculadora()