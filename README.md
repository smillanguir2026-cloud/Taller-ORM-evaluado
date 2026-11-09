# Taller ORM evaluado

Evaluación de Programación II: sistema de reservas de salas de estudio.

**Estudiante:** Simón Pedro Millanguir Zambrano
## Objetivo

Aplicar el mapeo objeto-relacional (ORM) para definir entidades relacionadas,
crear tablas, insertar, consultar y eliminar registros, y modificar el estado
de una sala mediante transacciones.

La interacción se realiza mediante un menú por consola.

## Situación problemática

La biblioteca universitaria necesita administrar salas de estudio y sus
reservas. La aplicación permite registrar salas, reservar una sala disponible,
consultar las reservas y cancelar una reserva, liberando nuevamente la sala.

La información se almacena de forma persistente en la base de datos SQLite
`reservas.db`.

## Tecnologías utilizadas

- Python 3.10 o superior.
- SQLAlchemy 2.x.
- SQLite.
- Visual Studio Code como editor de código.

## Estructura del proyecto

```text
Taller-ORM-evaluado/
├── TallerORM/
│   ├── .gitignore
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   └── modelos.py
└── README.md
```

El archivo `reservas.db` se crea automáticamente dentro de `TallerORM`
al ejecutar el programa por primera vez.

### Descripción de los archivos

- `database.py`: configura la conexión a SQLite y las sesiones de SQLAlchemy.
- `modelos.py`: define las entidades Sala y Reserva y su relación.
- `crud.py`: contiene las validaciones y operaciones sobre la base de datos.
- `main.py`: inicia el programa, crea las tablas y muestra el menú.
- `.gitignore`: excluye archivos temporales y carpetas del entorno virtual.

## Instalación y ejecución

### 1. Descargar o clonar el repositorio

Descargar el proyecto desde GitHub o ejecutar:

```bash
git clone https://github.com/smillanguir2026-cloud/Taller-ORM-evaluado.git
```

### 2. Abrir el proyecto en Visual Studio Code

Seleccionar **Archivo → Abrir carpeta** y abrir la carpeta
`Taller-ORM-evaluado`.

### 3. Instalar SQLAlchemy

Abrir la terminal integrada de Visual Studio Code y ejecutar:

```bash
python -m pip install "SQLAlchemy>=2.0,<3.0"
```

Para comprobar la instalación:

```bash
python -m pip show SQLAlchemy
```

### 4. Ejecutar el programa

Desde la carpeta raíz del repositorio, ingresar a la carpeta del programa:

```bash
cd TallerORM
```

Luego ejecutar:

```bash
python main.py
```

Si la terminal ya está dentro de `TallerORM`, ejecutar solamente
`python main.py`.

No es necesario crear la base de datos manualmente. El programa crea
`reservas.db` y sus tablas si todavía no existen.

## Menú principal

```text
1. Registrar sala
2. Consultar salas
3. Registrar reserva
4. Consultar reservas
5. Cancelar reserva
0. Salir
```

## Modelo de datos

### Sala

- `id`: clave primaria.
- `nombre`: nombre obligatorio, de hasta 100 caracteres.
- `capacidad`: número entero mayor que cero.
- `disponible`: indica si la sala está disponible; inicialmente es verdadero.

### Reserva

- `id`: clave primaria.
- `estudiante`: nombre obligatorio, de hasta 100 caracteres.
- `sala_id`: clave foránea que identifica la sala.
- `fecha`: fecha válida en formato `AAAA-MM-DD`.

La relación es de uno a muchos: una sala puede tener muchas reservas a lo
largo del tiempo y cada reserva pertenece a una sala.

Para este taller, una sala admite una sola reserva activa a la vez,
independientemente de la fecha ingresada. Al cancelar una reserva,
el registro se elimina; no se conserva un historial de cancelaciones.

## Operaciones CRUD

| Operación | Implementación |
|---|---|
| Crear | Registrar salas y reservas. |
| Consultar | Mostrar salas y reservas. |
| Actualizar | Cambiar la disponibilidad de una sala al reservar o cancelar. |
| Eliminar | Eliminar una reserva al cancelarla. |

El registro de una reserva y el cambio de disponibilidad se realizan
en una misma transacción. Lo mismo ocurre al cancelar una reserva
y liberar la sala.

## Validaciones

- Rechazo de nombres vacíos.
- Rechazo de textos de más de 100 caracteres.
- Capacidad mayor que cero.
- Fecha válida en formato `AAAA-MM-DD`.
- Comprobación de que la sala exista y esté disponible.
- Comprobación de que la reserva exista antes de cancelarla.
- Control de errores cuando se ingresan letras en campos numéricos.

## Casos de prueba

Ejecutar la siguiente secuencia usando los IDs que muestra el programa:

| Caso | Acción | Resultado esperado |
|---|---|---|
| CP-01 | Crear Sala A con 6 cupos y Sala B con 4 cupos. | Ambas disponibles. |
| CP-02 | Reservar Sala A para Ana. | Reserva registrada y Sala A ocupada. |
| CP-03 | Intentar reservar Sala A para Pedro. | Operación rechazada. |
| CP-04 | Consultar reservas. | Se muestra la reserva de Ana. |
| CP-05 | Cancelar la reserva de Ana. | Sala A vuelve a estar disponible. |
| CP-06 | Reservar Sala A para Pedro. | Reserva aceptada. |

Para las reservas se puede utilizar la fecha `2026-11-10`.

Si las salas ya están registradas, consultar sus IDs y reutilizarlas
sin crear duplicados. Antes de comenzar la secuencia, comprobar que
no tengan reservas activas.

## Persistencia

Los datos se guardan en `TallerORM/reservas.db`.

Para comprobar la persistencia, salir con la opción `0`, ejecutar
nuevamente el programa y consultar las salas y reservas. Los datos
registrados deben mantenerse.

PARA VER LAS PRUEBAS, TIENES QUE SUBIR EN LA TERMINAL, LOS MENSAJES DE ERRORES Y COMANDOS SE ENCUENTRAN ARRIBA DEL MENU.
    