from pathlib import Path
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

RUTA_BD = Path(__file__).resolve().parent / "reservas.db"

engine = create_engine(
    URL.create("sqlite", database=str(RUTA_BD))
)

Session = sessionmaker(bind=engine)