from sqlalchemy.exc import SQLAlchemyError
from database import Base, engine
from crud import (
    cancelar_reserva,
    consultar_reservas,
    consultar_salas,
    insertar_sala,
    registrar_reserva,
)

def leer_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError(
            "Debes ingresar un número entero."
        ) from None

def menu(): #MENU AL INICIAR EL PROGRAMA, CON OPCIONES PARA EL USUARIO.
    while True:
        print("\n===== RESERVAS DE SALAS DE ESTUDIO =====")
        print("1. Registrar sala")
        print("2. Consultar salas")
        print("3. Registrar reserva")
        print("4. Consultar reservas")
        print("5. Cancelar reserva")
        print("0. Salir")

        try: #CASOS A OCURRIR.
            opcion = leer_entero("Selecciona una opción: ")

            if opcion == 1:
                nombre = input("Nombre de la sala: ")
                capacidad = leer_entero("Capacidad: ")

                insertar_sala(nombre, capacidad)

            elif opcion == 2:
                consultar_salas()

            elif opcion == 3:
                estudiante = input("Nombre del estudiante: ")
                sala_id = leer_entero("ID de la sala: ")
                fecha = input("Fecha (AAAA-MM-DD): ")

                registrar_reserva(
                    estudiante,
                    sala_id,
                    fecha,
                )

            elif opcion == 4:
                consultar_reservas()

            elif opcion == 5:
                id_reserva = leer_entero(
                    "ID de la reserva a cancelar: "
                )

                cancelar_reserva(id_reserva)

            elif opcion == 0:
                print("Programa finalizado.")
                break

            else:
                print("Opción inválida. Selecciona de 0 a 5.")

        except ValueError as error:
            print(f"Error: {error}")

        except SQLAlchemyError:
            print(
                "Ocurrió un error con la base de datos. "
                "La operación no pudo completarse."
            )

def main():
    try:
        Base.metadata.create_all(engine)
    except SQLAlchemyError:
        print("No se pudo iniciar la base de datos.")
        return

    menu()

if __name__ == "__main__": #FINALIZACIÓN DEL PROGRAMA, SE EJECUTA LA FUNCIÓN PRINCIPAL.
    main()
  #MAIN TERMINADO.