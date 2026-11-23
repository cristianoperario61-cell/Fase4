import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        if len(nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres.")

        if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", correo):
            raise DatosInvalidosError("El correo electrónico no es válido.")

        if not telefono.isdigit() or not 7 <= len(telefono) <= 15:
            raise DatosInvalidosError("El teléfono debe tener entre 7 y 15 dígitos.")

        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    def describir(self):
        return f"Cliente: {self._nombre} | Correo: {self._correo} | Teléfono: {self._telefono}"