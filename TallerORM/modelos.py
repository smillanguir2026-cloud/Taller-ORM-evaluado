from sqlalchemy import (
    Boolean,
    CheckConstraint,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Sala(Base): #ENTIDAD SALA 
    __tablename__ = "salas"

    __table_args__ = (
        CheckConstraint(
            "capacidad > 0",
            name="capacidad_positiva",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    capacidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    disponible: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    reservas: Mapped[list["Reserva"]] = relationship(
        back_populates="sala",
    )

class Reserva(Base): #ENTIDAD RESERVA
    __tablename__ = "reservas"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    estudiante: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    sala_id: Mapped[int] = mapped_column(
        ForeignKey("salas.id"),
        nullable=False,
    )

    fecha: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    sala: Mapped["Sala"] = relationship(
        back_populates="reservas",
    )

    #TERMINADO MODELO DE DATOS REQUERIDOS.