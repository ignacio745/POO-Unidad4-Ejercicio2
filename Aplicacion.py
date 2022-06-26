from cgitb import text
from tkinter import messagebox, ttk
import tkinter as tk

from numpy import pad

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        buttonStyle = ttk.Style()
        buttonStyle.configure("Wild.TRadiobutton",
                            background="white",
                            foreground="black")



        self.title("Cálculo de IVA")
        self.resizable(False, False)
        self.geometry("300x300")
        self.__precio = tk.StringVar()
        self.__seleccion = tk.IntVar()
        self.__iva = tk.StringVar()
        self.__precioConIva = tk.StringVar()
        labelFrameSuperior = tk.LabelFrame(self, padx=105, bg="lightblue")
        labelFrameSeleccion = tk.LabelFrame(self, padx=22, pady=30, bg="white")
        labelFrameInferior = tk.LabelFrame(self, padx=75, pady=27, bg="white")
        titulo = tk.Label(labelFrameSuperior, text="Cálculo de IVA", bg="lightblue")
        precioLabel = tk.Label(labelFrameSeleccion, text="Precio sin IVA", bg="white")
        precioEntry = tk.Entry(labelFrameSeleccion, textvariable=self.__precio)
        boton1 = ttk.Radiobutton(labelFrameSeleccion, text="IVA 21 %", value=0, variable=self.__seleccion, style="Wild.TRadiobutton")
        boton2 =ttk.Radiobutton(labelFrameSeleccion, text="IVA 10.5 %", value=1, variable=self.__seleccion, style="Wild.TRadiobutton")
        ivaLabel = tk.Label(labelFrameInferior, text="IVA", bg="white")
        ivaLabel2 = tk.Label(labelFrameInferior, textvariable=self.__iva, bg="white")
        precioConIVALabel = tk.Label(labelFrameInferior, text="Precio Con IVA", bg="white")
        precioConIVALabel2 = tk.Label(labelFrameInferior, textvariable=self.__precioConIva, bg="white")
        botonCalcular = tk.Button(labelFrameInferior, text="Calcular", command=self.calcular, bg="green")
        botonSalir = tk.Button(labelFrameInferior, text="Salir", command=self.destroy, bg="red")
        
        

        labelFrameSuperior.grid(row=0, column=0, columnspan=3)
        labelFrameSeleccion.grid(row=1, column=0)
        labelFrameInferior.grid(row=2, column=0)
        titulo.grid(row=0, column=0, columnspan=3)
        precioLabel.grid(row=0, column=0)
        precioEntry.grid(row=0, column=1)
        boton1.grid(row=1, column=0)
        boton2.grid(row=2, column=0)
        ivaLabel.grid(row=0, column=0)
        ivaLabel2.grid(row=0, column=1)
        precioConIVALabel.grid(row=1, column=0)
        precioConIVALabel2.grid(row=1, column=1)
        botonCalcular.grid(row=2, column=0)
        botonSalir.grid(row=2, column=1)



    def calcular(self):
        try:
            precio = float(self.__precio.get())
        except ValueError:
            messagebox.showerror(title="Error de tipo", message="Precio invalido, ingrese un numero")
            return
        
        else:
            if self.__seleccion.get() == 0:
                iva = 0.21
            
            elif self.__seleccion.get() == 1:
                iva = 0.105
            
            self.__iva.set("{0:.2f}".format(precio * iva))
            self.__precioConIva.set("{0:.2f}".format(precio + precio * iva))
        