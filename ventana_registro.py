import tkinter as tk
from tkinter import messagebox
from componentes.campo_radio import CampoRadio
from componentes.campo_texto import CampoTexto
from modelos.empleado import Empleado


class VentanaRegistro(tk.Toplevel):
    cargos = ["Obrero", "Docente", "Administrativo", "Subdirección", "Dirección"]
    nivelesDeInstruccion = ["Bachiller", "Licenciado", "MSc", "Doctor"]

    def __init__(self, master):
        super().__init__(master)

        self.title("Registrar Empleado")

        # Campos de texto
        self.campo_nombre = CampoTexto(self, "Nombre:")
        self.campo_nombre.pack(fill=tk.X)

        self.campo_apellido = CampoTexto(self, "Apellido:")
        self.campo_apellido.pack(fill=tk.X)

        self.campo_ci = CampoTexto(self, "CI:")
        self.campo_ci.pack(fill=tk.X, padx=33)

        # Radio buttons para cargo
        opciones_cargo = self.cargos
        self.campo_cargo = CampoRadio(self, "Cargo:", opciones_cargo)
        self.campo_cargo.pack()

        # Radio buttons para nivel de instrucción
        opciones_nivel = self.nivelesDeInstruccion
        self.campo_nivel = CampoRadio(self, "Nivel de Instrucción:", opciones_nivel)
        self.campo_nivel.pack()

        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar_empleado)
        btn_guardar.pack(pady=10)

    def guardar_empleado(self):

        nombre = self.campo_nombre.obtener_valor()
        apellido = self.campo_apellido.obtener_valor()
        ci = self.campo_ci.obtener_valor()
        cargo = self.campo_cargo.obtener_valor()
        nivel_de_instruccion = self.campo_nivel.obtener_valor()

        nuevo_empleado = Empleado(nombre, apellido, ci, cargo, nivel_de_instruccion)

        # Agregar empleado al sistema
        self.master.sistema_empleados.agregar_empleado(nuevo_empleado)

        messagebox.showinfo("Éxito", "Empleado registrado con éxito.")

        # Limpiar campos después de guardar
        for campo in (
            self.campo_nombre,
            self.campo_apellido,
            self.campo_ci,
            self.campo_cargo,
            self.campo_nivel,
        ):
            campo.limpiar()
