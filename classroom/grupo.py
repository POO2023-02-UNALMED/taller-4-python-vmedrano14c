from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas or []
        self.listadoAlumnos = estudiantes or []

    def listadoAsignaturas(self, **kwargs):
        for asignatura_nombre in kwargs.values():
            self._asignaturas.append(Asignatura(asignatura_nombre))


    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return f"Grupo:{self._grupo}, Asignaturas: {','.join(str(asig) for asig in self._asignaturas)}, Alumnos :{','.join(self.listadoAlumnos)}"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
    


