import tkinter as tk
from tkinter import ttk


class CampoRadio(ttk.Frame):
    def __init__(self, master, etiqueta, opciones):
        super().__init__(master)
        self.variable = tk.StringVar()
        self.etiqueta = ttk.Label(self, text=etiqueta)
        self.etiqueta.pack(side=tk.TOP, padx=5, pady=5)

        for opcion in opciones:
            radio = ttk.Radiobutton(
                self, text=opcion, variable=self.variable, value=opcion
            )
            radio.pack(side=tk.LEFT)

    def obtener_valor(self):
        return self.variable.get()

    def limpiar(self):
        self.variable.set("")
