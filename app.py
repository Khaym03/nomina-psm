from componentes.campo_texto import CampoTexto
from modelos.sistema_empleados import SistemaEmpleados
import tkinter as tk
from tkinter import messagebox
from ventana_registro import VentanaRegistro


class Aplicacion(tk.Tk):
    ventana_registro = None

    def __init__(self):
        super().__init__()
        self.posicionar_ventana()

        self.sistema_empleados = SistemaEmpleados()

        # Configuración de la ventana principal
        self.title("Sistema de Empleados")

        self.encabezado = tk.Label(
            self, text="Sistema de Gestión de Empleados", font=("Arial", 16)
        )
        self.encabezado.pack(pady=10)

        btn_registrar = tk.Button(
            self, text="Registrar Empleado", command=self.abrir_registro
        )
        btn_registrar.pack(pady=10)

        self.encabezado = tk.Label(self, text="Consulta el sueldo", font=("Arial", 14))
        self.encabezado.pack(pady=(28, 0))

        self.campo_ci = CampoTexto(self, "CI:")
        self.campo_ci.pack(pady=10)

        btn_buscar = tk.Button(self, text="Buscar", command=self.buscar_empleado)
        btn_buscar.pack(pady=10)

    def abrir_registro(self):
        if self.ventana_registro is None:
            self.ventana_registro = VentanaRegistro(self)

    def buscar_empleado(self):
        ci_buscar = self.campo_ci.obtener_valor()

        empleado_encontrado = self.sistema_empleados.buscar_empleado(ci_buscar)

        if empleado_encontrado:
            sueldo_estimado = empleado_encontrado.calcSueldo(
                40
            )  # Suponiendo 40 horas trabajadas.

            messagebox.showinfo(
                "Sueldo Estimado",
                f"""
                Nombre: {empleado_encontrado.nombre}
                Apellido: {empleado_encontrado.apellido}
                Cédula de Identidad: {empleado_encontrado.ci}
                Cargo: {empleado_encontrado.cargo}
                Nivel de Instrucción: {empleado_encontrado.nivelDeInstruccion}
                Sueldo por hora: {empleado_encontrado.salarioBasePorHora}
                Sueldo por 40 horas: ${sueldo_estimado:.2f}
                """,
            )

            # Limpiar campo después de buscar
            self.campo_ci.limpiar()

            return

        messagebox.showerror("No encontrado", "Empleado no encontrado.")

    def posicionar_ventana(self):
        ancho = 400
        alto = 400
        ancho_ventana = self.winfo_screenwidth()
        alto_ventana = self.winfo_screenheight()
        x = int(ancho_ventana * 0.5) - (ancho)
        y = int(alto_ventana // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")
