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
        self.posicionar_ventana()

        self.encabezado = tk.Label(
            self, text="Formulario de Registro", font=("Arial", 16)
        )
        self.encabezado.pack(pady=10)

        # Campos de texto
        self.campo_nombre = CampoTexto(self, "Nombre:")
        self.campo_nombre.pack(fill=tk.X, pady=(10, 0))

        self.campo_apellido = CampoTexto(self, "Apellido:")
        self.campo_apellido.pack(fill=tk.X)

        self.campo_ci = CampoTexto(self, "CI:")
        self.campo_ci.pack(fill=tk.X, padx=33)

        # Opciones para cargo
        opciones_cargo = self.cargos
        self.campo_cargo = CampoRadio(self, "Cargo:", opciones_cargo)
        self.campo_cargo.pack(padx=10, pady=(20, 0))

        # Opciones para nivel de instrucción
        opciones_nivel = self.nivelesDeInstruccion
        self.campo_nivel = CampoRadio(self, "Nivel de Instrucción:", opciones_nivel)
        self.campo_nivel.pack(padx=10, pady=(20, 0))

        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar_empleado)
        btn_guardar.pack(pady=10)

    def guardar_empleado(self):
        nombre = self.campo_nombre.obtener_valor()
        apellido = self.campo_apellido.obtener_valor()
        ci = self.campo_ci.obtener_valor()
        cargo = self.campo_cargo.obtener_valor()
        nivel_de_instruccion = self.campo_nivel.obtener_valor()

        if not self.formulario_valido():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        nuevo_empleado = Empleado(nombre, apellido, ci, cargo, nivel_de_instruccion)

        # Agregar empleado al sistema
        self.master.sistema_empleados.agregar_empleado(nuevo_empleado)

        messagebox.showinfo("Éxito", "Empleado registrado con éxito.")

        for campo in (
            self.campo_nombre,
            self.campo_apellido,
            self.campo_ci,
            self.campo_cargo,
            self.campo_nivel,
        ):
            campo.limpiar()

    def posicionar_ventana(self):
        ancho = 450
        alto = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(screen_width * 0.8) - (ancho)
        y = int(screen_height // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def formulario_valido(self):
        return (
            self.campo_nombre.obtener_valor()
            and self.campo_apellido.obtener_valor()
            and self.campo_ci.obtener_valor()
            and self.campo_cargo.obtener_valor()
            and self.campo_nivel.obtener_valor()
        )
