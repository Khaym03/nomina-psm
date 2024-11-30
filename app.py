from modelos.sistema_empleados import SistemaEmpleados
import tkinter as tk

from ventana_busqueda import VentanaBusqueda
from ventana_registro import VentanaRegistro

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.sistema_empleados = SistemaEmpleados()
        
        # Configuración de la ventana principal
        self.title("Sistema de Empleados")
        
        btn_registrar = tk.Button(self, text="Registrar Empleado", command=self.abrir_registro)
        btn_registrar.pack(pady=10)

        btn_buscar = tk.Button(self, text="Buscar Empleado", command=self.abrir_busqueda)
        btn_buscar.pack(pady=10)

    def abrir_registro(self):
        ventana_registro = VentanaRegistro(self)
        
    def abrir_busqueda(self):
        ventana_busqueda = VentanaBusqueda(self)