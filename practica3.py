import tkinter as tk

class Apliacion():

    def __init__(self):
        
        self.ventana1 = tk.Tk()

        self.valor1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana1, text="1", variable=self.valor1, command=self.cambiar)               
        self.check1.grid(column=0, row=0)

        self.valor2 = tk.IntVar()
        self.check2 = tk.Checkbutton(self.ventana1, text="2", variable=self.valor2, command=self.cambiar)               
        self.check2.grid(column=0, row=1)

        self.valor3 = tk.IntVar()
        self.check3 = tk.Checkbutton(self.ventana1, text="3", variable=self.valor3, command=self.cambiar)               
        self.check3.grid(column=0, row=2)

        self.ventana1.mainloop()

    def cambiar(self):

        titulo = ""

        if self.valor1.get() == 1:
            titulo += "1"
        if self.valor2.get() == 1:
            titulo += "2"
        if self.valor3.get() == 1:
            titulo += "3"

        self.ventana1.title(titulo)
            

app = Apliacion()