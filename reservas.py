from entidades import Entidad
from excepciones import ReservaInvalidaError, OperacionNoPermitidaError


class Reserva(Entidad):

    def __init__(self, identificador, cliente, servicio, cantidad):
        super().__init__(identificador)

        if cantidad <= 0:
            raise ReservaInvalidaError("La cantidad debe ser mayor que cero.")

        self._cliente = cliente
        self._servicio = servicio
        self._cantidad = cantidad
        self._estado = "PENDIENTE"

        try:
            self._total = servicio.calcular_costo(cantidad)
        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

    @property
    def estado(self):
        return self._estado

    @property
    def total(self):
        return self._total

    def confirmar(self):
        if self._estado != "PENDIENTE":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "CONFIRMADA"

    def cancelar(self):
        if self._estado not in ["PENDIENTE", "CONFIRMADA"]:
            raise OperacionNoPermitidaError(
                "No se puede cancelar esta reserva."
            )

        self._estado = "CANCELADA"

    def procesar(self):
        if self._estado != "CONFIRMADA":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        self._estado = "PROCESADA"

    def describir(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Estado: {self._estado} | "
            f"Total: ${self._total}"
        )