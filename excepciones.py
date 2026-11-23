class ErrorSistema(Exception):
    pass


class DatosInvalidosError(ErrorSistema):
    pass


class OperacionNoPermitidaError(ErrorSistema):
    pass


class ServicioNoDisponibleError(ErrorSistema):
    pass


class ReservaInvalidaError(ErrorSistema):
    pass


class ElementoNoEncontradoError(ErrorSistema):
    pass