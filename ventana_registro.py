import tkinter as tk
from tkinter import messagebox
from app import Aplicacion
from modelos.empleado import Empleado

class VentanaRegistro(tk.Toplevel):
    def __init__(self, master: Aplicacion):
        super().__init__(master)
        
        self.title("Registrar Empleado")
        
        
        
        # Campos de entrada
        tk.Label(self, text="Nombre").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(self, text="Apellido").grid(row=1, column=0)
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.grid(row=1, column=1)

        tk.Label(self, text="CI").grid(row=2, column=0)
        self.entry_ci = tk.Entry(self)
        self.entry_ci.grid(row=2, column=1)

        tk.Label(self, text="Cargo").grid(row=3, column=0)
        self.entry_cargo = tk.Entry(self)
        self.entry_cargo.grid(row=3, column=1)

        tk.Label(self, text="Nivel de Instrucción").grid(row=4, column=0)
        self.entry_nivel = tk.Entry(self)
        self.entry_nivel.grid(row=4, column=1)

        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar_empleado)
        btn_guardar.grid(row=5, columnspan=2)

    def guardar_empleado(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        ci = self.entry_ci.get()
        cargo = self.entry_cargo.get()
        nivel_de_instruccion = self.entry_nivel.get()

        nuevo_empleado = Empleado(nombre, apellido, ci, cargo, nivel_de_instruccion)
        
        # Agregar empleado al sistema
        self.master.sistema_empleados.agregar_empleado(nuevo_empleado)
        
        messagebox.showinfo("Éxito", "Empleado registrado con éxito.")
        
        # Limpiar campos después de guardar
        for entry in (self.entry_nombre, self.entry_apellido, self.entry_ci,
                      self.entry_cargo, self.entry_nivel):
            entry.delete(0, tk.END)