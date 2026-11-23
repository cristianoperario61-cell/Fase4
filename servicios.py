from abc import abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError


class Servicio(Entidad):

    def __init__(self, identificador, nombre, precio):
        super().__init__(identificador)

        if precio <= 0:
            raise DatosInvalidosError("El precio debe ser mayor que cero.")

        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    def describir(self):
        return f"Servicio: {self._nombre} | Precio: ${self._precio}"


class ReservaSala(Servicio):

    def calcular_costo(self, cantidad):
        if cantidad <= 0:
            raise DatosInvalidosError("Las horas deben ser mayores que cero.")
        return self._precio * cantidad


class AlquilerEquipo(Servicio):

    def calcular_costo(self, cantidad):
        if cantidad <= 0:
            raise DatosInvalidosError("Los días deben ser mayores que cero.")
        return self._precio * cantidad


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, cantidad):
        if cantidad <= 0:
            raise DatosInvalidosError("Las horas de asesoría deben ser mayores que cero.")
        return self._precio * cantidad


    def calcular_costo_sobrecargado(self, cantidad, descuento=0):
        if cantidad <= 0:
            raise DatosInvalidosError("La cantidad debe ser mayor que cero.")

        if descuento < 0 or descuento > 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        total = self._precio * cantidad
        return total - (total * descuento / 100)