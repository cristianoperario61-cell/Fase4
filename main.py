from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from gestor import GestorSoftwareFJ
from excepciones import ErrorSistema


def ejecutar_sistema():
    gestor = GestorSoftwareFJ()

    print("====================================")
    print("       SISTEMA SOFTWARE FJ")
    print("====================================")

    try:
        cliente1 = Cliente("C001", "Carlos Pérez", "carlos@gmail.com", "3101234567")
        gestor.registrar_cliente(cliente1)
        print("1. Cliente registrado correctamente.")

    except ErrorSistema as error:
        print("1. Error al registrar cliente:", error)

    try:
        cliente2 = Cliente("C002", "Ana López", "ana@gmail.com", "3009876543")
        gestor.registrar_cliente(cliente2)
        print("2. Segundo cliente registrado correctamente.")

    except ErrorSistema as error:
        print("2. Error:", error)

    try:
        Cliente("C003", "Lu", "correo_invalido", "123")
    except ErrorSistema as error:
        print("3. Error controlado al crear cliente:", error)

    try:
        sala = ReservaSala("S001", "Sala de reuniones", 50000)
        gestor.registrar_servicio(sala)
        print("4. Sala registrada correctamente.")

    except ErrorSistema as error:
        print("4. Error:", error)

    try:
        equipo = AlquilerEquipo("S002", "Computador portátil", 30000)
        gestor.registrar_servicio(equipo)
        print("5. Equipo registrado correctamente.")

    except ErrorSistema as error:
        print("5. Error:", error)

    try:
        asesoria = AsesoriaEspecializada("S003", "Asesoría informática", 80000)
        gestor.registrar_servicio(asesoria)
        print("6. Asesoría registrada correctamente.")

    except ErrorSistema as error:
        print("6. Error:", error)

    try:
        total = asesoria.calcular_costo_sobrecargado(3, 10)
        print("7. Costo de asesoría con descuento:", total)

    except ErrorSistema as error:
        print("7. Error:", error)

    try:
        reserva1 = Reserva("R001", cliente1, sala, 2)
        gestor.registrar_reserva(reserva1)
        print("8. Reserva creada correctamente.")

    except ErrorSistema as error:
        print("8. Error:", error)

    try:
        reserva1.confirmar()
        print("9. Reserva confirmada correctamente.")

    except ErrorSistema as error:
        print("9. Error:", error)

    try:
        reserva1.procesar()
        print("10. Reserva procesada correctamente.")

    except ErrorSistema as error:
        print("10. Error:", error)

    try:
        reserva1.cancelar()
        print("11. Intento de cancelar reserva procesada.")

    except ErrorSistema as error:
        print("11. Error controlado:", error)

    try:
        gestor.buscar_cliente("C999")

    except ErrorSistema as error:
        print("12. Búsqueda fallida controlada:", error)

    try:
        reserva2 = Reserva("R002", cliente2, equipo, 0)
        gestor.registrar_reserva(reserva2)

    except ErrorSistema as error:
        print("13. Error al crear reserva:", error)

    else:
        print("13. Reserva creada correctamente.")

    finally:
        print("Finalizó el intento de creación de reserva.")

    print("\n========== RESUMEN DEL SISTEMA ==========")

    print("\nCLIENTES:")
    for cliente in gestor.listar_clientes():
        print(cliente.describir())

    print("\nSERVICIOS:")
    for servicio in gestor.listar_servicios():
        print(servicio.describir())

    print("\nRESERVAS:")
    for reserva in gestor.listar_reservas():
        print(reserva.describir())

    print("\nSistema finalizado.")
    print("Revisa el archivo logs.txt para consultar el registro de operaciones.")


if __name__ == "__main__":
    ejecutar_sistema()