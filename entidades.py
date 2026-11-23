from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):

    def __init__(self, identificador):
        self._identificador = identificador
        self._fecha_creacion = datetime.now()

    @property
    def identificador(self):
        return self._identificador

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @abstractmethod
    def describir(self):
        pass