import logging
from excepciones import ElementoNoEncontradoError


logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


class GestorSoftwareFJ:

    def __init__(self):
        self._clientes = []
        self._servicios = []
        self._reservas = []

    def registrar_cliente(self, cliente):
        self._clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.nombre)

    def registrar_servicio(self, servicio):
        self._servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.nombre)

    def registrar_reserva(self, reserva):
        self._reservas.append(reserva)
        logging.info("Reserva registrada: %s", reserva.identificador)

    def buscar_cliente(self, identificador):
        for cliente in self._clientes:
            if cliente.identificador == identificador:
                return cliente

        raise ElementoNoEncontradoError("No se encontró el cliente.")

    def buscar_servicio(self, identificador):
        for servicio in self._servicios:
            if servicio.identificador == identificador:
                return servicio

        raise ElementoNoEncontradoError("No se encontró el servicio.")

    def buscar_reserva(self, identificador):
        for reserva in self._reservas:
            if reserva.identificador == identificador:
                return reserva

        raise ElementoNoEncontradoError("No se encontró la reserva.")

    def listar_clientes(self):
        return self._clientes

    def listar_servicios(self):
        return self._servicios

    def listar_reservas(self):
        return self._reservas