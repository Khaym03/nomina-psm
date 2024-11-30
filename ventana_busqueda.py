import tkinter as tk
from tkinter import messagebox


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

            sueldo_estimado = empleado_encontrado.calcSueldo(
                40
            )  # Suponiendo 40 horas trabajadas.
            messagebox.showinfo(
                "Sueldo Estimado", f"Sueldo por 40 horas: ${sueldo_estimado:.2f}"
            )

            # Limpiar campo después de buscar
            self.entry_ci_busqueda.delete(0, tk.END)

            return

        messagebox.showerror("No encontrado", "Empleado no encontrado.")
