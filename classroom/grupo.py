from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = [Asignatura(asig) if isinstance(asig, str) else asig for asig in asignaturas] if asignaturas else []
        self.listadoAlumnos = estudiantes or []

    def listadoAsignaturas(self, **kwargs):
        for value in kwargs.values():
            self._asignaturas.append(Asignatura(value))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        asignaturas_str = ', '.join(str(asig) for asig in self._asignaturas)
        alumnos_str = ', '.join(self.listadoAlumnos)
        return f"Grupo: {self._grupo}, Asignaturas: {asignaturas_str}, Alumnos: {alumnos_str}"
    @classmethod
    def asignarNombre(cls, nombre ="Grado 6"):
        cls.grado = nombre