import tkinter as tk
from tkinter import messagebox
from typing import List


class Empleado:
    salarioBasePorHora = 2.5

    bonosPorNivelDeInstruccion = {
        "bachiller": 1.05,
        "licenciado": 1.15,
        "msc": 1.3,
        "doctor": 1.5,
    }
    
    bonosPorCargo = {
        "obrero": 1.1,
        "docente": 1.2,
        "administrativo": 1.3,
        "subdireccion": 1.5,
        "direccion": 1.7,
    }

    def __init__(self, nombre: str, apellido: str, ci: str, cargo: str, nivelDeInstruccion: str):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.cargo = cargo
        self.nivelDeInstruccion = nivelDeInstruccion

    def calcSueldo(self, horasTrabajadas: float) -> float:
        bono_cargo = self.bonoPorCargo()
        bono_nivel = self.bonoPorNivelDeInstruccion()
        
        return (
            self.salarioBasePorHora
            * horasTrabajadas
            * bono_cargo
            * bono_nivel
        )

    def bonoPorNivelDeInstruccion(self) -> float:
        return self.bonosPorNivelDeInstruccion.get(self.nivelDeInstruccion, 1)

    def bonoPorCargo(self) -> float:
        return self.bonosPorCargo.get(self.cargo, 1)


class SistemaEmpleados:
    def __init__(self):
        self.empleados: List[Empleado] = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def buscar_empleado(self, ci):
        for empleado in self.empleados:
            if empleado.ci == ci:
                return empleado
        return None


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


class VentanaRegistro(tk.Toplevel):
    def __init__(self, master):
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


class VentanaBusqueda(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("Buscar Empleado")
        
        tk.Label(self, text="Ingrese CI del empleado").grid(row=0, column=0)
        
        self.entry_ci_busqueda = tk.Entry(self)
        self.entry_ci_busqueda.grid(row=0, column=1)

        btn_buscar = tk.Button(self, text="Buscar", command=self.buscar_empleado)
        btn_buscar.grid(row=1, columnspan=2)

    def buscar_empleado(self):
        ci_buscar = self.entry_ci_busqueda.get()
        
        empleado_encontrado = self.master.sistema_empleados.buscar_empleado(ci_buscar)
        
        if empleado_encontrado:
            messagebox.showinfo("Empleado Encontrado", f"{empleado_encontrado.nombre}")
            # Aquí puedes agregar más información o funcionalidades si lo deseas.
            # Por ejemplo: calcular sueldo.
            sueldo_estimado = empleado_encontrado.calcSueldo(40)  # Suponiendo 40 horas trabajadas.
            messagebox.showinfo("Sueldo Estimado", f"Sueldo por 40 horas: ${sueldo_estimado:.2f}")
            
            # Limpiar campo después de buscar
            self.entry_ci_busqueda.delete(0, tk.END)
            
            return
        
        messagebox.showerror("No encontrado", "Empleado no encontrado.")


# Ejemplo de uso
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()