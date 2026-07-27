from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "station.db"


engine = create_engine(
    f"sqlite:///{DB_PATH}",
    echo=False
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


def get_session():
    return SessionLocal()