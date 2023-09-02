class Asignatura:

    def __init__(self, nombre, salon=None):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        if self._salon:
            return f"Asignatura: {self._nombre}, Salon: {self._salon}"
        else:
            return f"Asignatura: {self._nombre}"
