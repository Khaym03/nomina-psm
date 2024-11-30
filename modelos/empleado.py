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

    def __init__(
        self, nombre: str, apellido: str, ci: str, cargo: str, nivelDeInstruccion: str
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.cargo = cargo
        self.nivelDeInstruccion = nivelDeInstruccion

    def calcSueldo(self, horasTrabajadas: float) -> float:
        bonoCargo = self.bonoPorCargo()
        bonoNivel = self.bonoPorNivelDeInstruccion()

        return self.salarioBasePorHora * horasTrabajadas * bonoCargo * bonoNivel

    def bonoPorNivelDeInstruccion(self) -> float:
        return self.bonosPorNivelDeInstruccion.get(self.nivelDeInstruccion.lower(), 1)

    def bonoPorCargo(self) -> float:
        return self.bonosPorCargo.get(self.cargo.lower(), 1)
