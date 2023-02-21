import tkinter as tk

class VentanaOper():

    def __init__(self, operador, textoBoton):

        self.operador = operador
        self.textoBoton = textoBoton        

        self.ventana2 = tk.Tk()
        self.ventana2.geometry('200x100')

        self.dato1 = tk.IntVar(self.ventana2)
        self.entry1 = tk.Entry(self.ventana2, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=0)

        self.dato2 = tk.IntVar(self.ventana2)
        self.entry2 = tk.Entry(self.ventana2, width=10, textvariable=self.dato2)
        self.entry2.grid(column=2, row=0)
        
        self.label2 = tk.Label(self.ventana2, text="Resultado")
        self.label2.grid(column=1, row=2)        

        self.label1 = tk.Label(self.ventana2, text=self.operador)
        self.label1.grid(column=1, row=0)

        self.boton1 = tk.Button(self.ventana2, text=self.textoBoton, command=self.operar)
        self.boton1.grid(column=1, row=1)

        self.ventana2.mainloop()

    def operar(self):

        if self.operador == "+":

            dato1 = self.dato1.get()
            dato2 = self.dato2.get()
        
            self.resulatdo = dato1 + dato2
            self.label2.config(text = self.resulatdo)

        elif self.operador == "-":
            dato1 = self.dato1.get()
            dato2 = self.dato2.get()
        
            self.resulatdo = dato1 - dato2
            self.label2.config(text = self.resulatdo)

        elif self.operador == "*":
            dato1 = self.dato1.get()
            dato2 = self.dato2.get()
        
            self.resulatdo = dato1 * dato2
            self.label2.config(text = self.resulatdo)

        elif self.operador == "/":
            dato1 = self.dato1.get()
            dato2 = self.dato2.get()
        
            self.resulatdo = dato1 / dato2
            self.label2.config(text = self.resulatdo)        


class Aplicacion(VentanaOper):

    def __init__(self):

        self.ventana1 = tk.Tk()
        self.ventana1.title("Principal")
        self.ventana1.geometry('200x100')

        self.botonSumar = tk.Button(self.ventana1, text="Sumar", command=self.ventanaSuma)
        self.botonSumar.grid(column=0, row=0)

        self.botonRestar = tk.Button(self.ventana1, text="Restar", command=self.ventanaResta)
        self.botonRestar.grid(column=1, row=0)

        self.botonMult = tk.Button(self.ventana1, text="Multiplicar", command=self.ventanaMulti)
        self.botonMult.grid(column=2, row=0)

        self.botonDiv = tk.Button(self.ventana1, text="Dividir", command=self.ventanaDiv)
        self.botonDiv.grid(column=3, row=0)
        
        self.ventana1.mainloop()

    def ventanaSuma(self):
            
        super().__init__("+", "Sumar")                      

    def ventanaResta(self):

        super().__init__("-", "Restar")
        
    def ventanaMulti(self):

        super().__init__("*", "Multiplicar")        

    def ventanaDiv(self):

        super().__init__("/", "Dividir")
        

app = Aplicacion()