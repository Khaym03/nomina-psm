from typing import List
from .empleado import Empleado

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