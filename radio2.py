import tkinter as tk

class Aplicacion():

    def __init__(self):

        self.ventana1 = tk.Tk()
        
        self.label1 = tk.Label(self.ventana1, text="ingrese un numero")
        self.label1.grid(column=0, row=0, padx=10, pady=5)
        
        self.dato1 = tk.IntVar(self.ventana1)
        self.entry1 = tk.Entry(self.ventana1, width=15, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=10, pady=5)

        self.label2 = tk.Label(self.ventana1, text="ingrese otro numero")
        self.label2.grid(column=0, row=1, padx=10, pady=5)
        
        self.dato2 = tk.IntVar(self.ventana1)
        self.entry2 = tk.Entry(self.ventana1, width=15, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=10, pady=5)

        self.seleccion = tk.IntVar(self.ventana1)
        self.seleccion.set(4)
        self.radio1 = tk.Radiobutton(self.ventana1, text="sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=2)
        self.radio2 = tk.Radiobutton(self.ventana1, text="restar", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=3)
        self.radio3 = tk.Radiobutton(self.ventana1, text="multiplicar", variable=self.seleccion, value=3)
        self.radio3.grid(column=1, row=2)
        self.radio4 = tk.Radiobutton(self.ventana1, text="dividir", variable=self.seleccion, value=4)
        self.radio4.grid(column=1, row=3)

        self.boton1 = tk.Button(self.ventana1, text="Resultado", command=self.resultado)
        self.boton1.grid(column=0, row=4, columnspan=2)  

        self.label3 = tk.Label(self.ventana1, text="Resultado", font=("arial", 20))
        self.label3.configure(foreground="red")
        self.label3.grid(column=0, row=5, columnspan=2)      

        self.ventana1.mainloop()

    def resultado(self):

        if self.seleccion.get() == 1:
            resultado = self.dato1.get() + self.dato2.get()
            self.label3.config(text=resultado)
        if self.seleccion.get() == 2:
            resultado = self.dato1.get() - self.dato2.get()
            self.label3.config(text=resultado)
        if self.seleccion.get() == 3:
            resultado = self.dato1.get() * self.dato2.get()
            self.label3.config(text=resultado)
        if self.seleccion.get() == 4:
            resultado = self.dato1.get() / self.dato2.get()
            self.label3.config(text=resultado)

app = Aplicacion()