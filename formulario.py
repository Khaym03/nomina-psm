import tkinter as tk
from tkinter import ttk
from componentes.campo_texto import CampoTexto
from componentes.campo_radio import CampoRadio



class Formulario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario de Registro")

        # Campos de texto
        self.campo_nombre = CampoTexto(self, "Nombre:")
        self.campo_nombre.pack(fill=tk.X)

        self.campo_apellido = CampoTexto(self, "Apellido:")
        self.campo_apellido.pack(fill=tk.X)

        self.campo_ci = CampoTexto(self, "CI:")
        self.campo_ci.pack(fill=tk.X, padx=33)

        # Radio buttons para cargo
        opciones_cargo = ["Administrativo", "Técnico"]
        self.campo_cargo = CampoRadio(self, "Cargo:", opciones_cargo)
        self.campo_cargo.pack()

        # Radio buttons para nivel de instrucción
        opciones_nivel = ["Básico", "Medio", "Superior"]
        self.campo_nivel = CampoRadio(self, "Nivel de Instrucción:", opciones_nivel)
        self.campo_nivel.pack()

        # Botón para enviar datos
        self.boton_enviar = ttk.Button(self, text="Enviar", command=self.enviar_datos)
        self.boton_enviar.pack(pady=10)

    def enviar_datos(self):
        nombre = self.campo_nombre.obtener_valor()
        apellido = self.campo_apellido.obtener_valor()
        ci = self.campo_ci.obtener_valor()
        cargo = self.campo_cargo.obtener_valor()
        nivel = self.campo_nivel.obtener_valor()

        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"Cédula de Identidad: {ci}")
        print(f"Cargo: {cargo}")
        print(f"Nivel de Instrucción: {nivel}")

if __name__ == "__main__":
    app = Formulario()
    app.mainloop()