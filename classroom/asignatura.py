class Asignatura:

    def __init__(self, nombre: str, salon: str = None):
        self._nombre = nombre
        self._salon = salon if salon is not None else "remoto"

    def __str__(self) -> str:
        if self._salon:
            return f"Asignatura: {self._nombre}, Salon: {self._salon}"
        else:
            return f"Asignatura: {self._nombre}"
