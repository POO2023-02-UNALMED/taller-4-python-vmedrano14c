class Asignatura:

    def __init__(self, nombre: str, salon: str = None):
        self._nombre = nombre
        self._salon = salon if salon is not None else "remoto"

    def __str__(self) -> str:
        return f"Asignatura: {self._nombre} {'Salon: ' + self._salon if self._salon != 'remoto' else 'remoto'}" 
