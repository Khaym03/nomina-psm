import tkinter as tk
from tkinter import ttk


class CampoTexto(ttk.Frame):
    def __init__(self, master, etiqueta):
        super().__init__(master)
        self.etiqueta = ttk.Label(self, text=etiqueta)
        self.etiqueta.pack(side=tk.LEFT, padx=5, pady=5)
        self.entrada = ttk.Entry(self)
        self.entrada.pack(side=tk.LEFT, padx=5, pady=5)

    def obtener_valor(self):
        return self.entrada.get()