import re
from datetime import date
from sqlalchemy import select
from database import Session
from modelos import Reserva, Sala

#VALIDACIONES 
def validar_texto(texto, campo):
    texto = texto.strip()

    if not texto:
        raise ValueError(f"{campo} no puede estar vacío.")

    if len(texto) > 100:
        raise ValueError(
            f"{campo} no puede superar los 100 caracteres."
        )

    return texto

def validar_fecha(fecha):
    fecha = fecha.strip()

    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha):
        raise ValueError(
            "La fecha debe tener el formato AAAA-MM-DD."
        )

    try:
        date.fromisoformat(fecha)
    except ValueError:
        raise ValueError(
            "La fecha ingresada no existe."
        ) from None

    return fecha

#REGISTRAR SALAS
def insertar_sala(nombre, capacidad):
    nombre = validar_texto(nombre, "El nombre de la sala")

    if capacidad <= 0:
        raise ValueError(
            "La capacidad debe ser mayor que cero."
        )

    with Session.begin() as session:
        sala = Sala(
            nombre=nombre,
            capacidad=capacidad,
            disponible=True,
        )

        session.add(sala)

    print("Sala registrada correctamente.")

#CONSULTAR SALAS
def consultar_salas():
    with Session() as session:
        consulta = select(Sala).order_by(Sala.id)
        salas = session.scalars(consulta).all()

        if not salas:
            print("No hay salas registradas.")
            return

        print("\n--- SALAS REGISTRADAS ---")

        for sala in salas:
            estado = (
                "Disponible"
                if sala.disponible
                else "Ocupada"
            )

            print(
                f"ID: {sala.id} | "
                f"Nombre: {sala.nombre} | "
                f"Capacidad: {sala.capacidad} | "
                f"Estado: {estado}"
            )

#RESERVAR SALA
def registrar_reserva(estudiante, sala_id, fecha):
    estudiante = validar_texto(
        estudiante,
        "El nombre del estudiante",
    )

    fecha = validar_fecha(fecha)

    with Session.begin() as session:
        sala = session.get(Sala, sala_id)

        if sala is None:
            raise ValueError(
                "No existe una sala con ese ID."
            )

        if not sala.disponible:
            raise ValueError(
                "La sala ya tiene una reserva activa."
            )

        reserva = Reserva(
            estudiante=estudiante,
            sala=sala,
            fecha=fecha,
        )

        session.add(reserva)

        sala.disponible = False

    print("Reserva registrada correctamente.")

#CONSULTAR RESERVAS 
def consultar_reservas():
    with Session() as session:
        consulta = select(Reserva).order_by(Reserva.id)
        reservas = session.scalars(consulta).all()

        if not reservas:
            print("No hay reservas registradas.")
            return

        print("\n--- RESERVAS REGISTRADAS ---")

        for reserva in reservas:
            print(
                f"ID: {reserva.id} | "
                f"Estudiante: {reserva.estudiante} | "
                f"Sala: {reserva.sala.nombre} | "
                f"Fecha: {reserva.fecha}"
            )

#CANCELAR RESERVA
def cancelar_reserva(id_reserva):
    with Session.begin() as session:
        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            raise ValueError(
                "No existe una reserva con ese ID."
            )

        reserva.sala.disponible = True

        session.delete(reserva)

    print("Reserva cancelada. La sala queda disponible.")
    #OPERACIONES TERMINADAS, POR VER.