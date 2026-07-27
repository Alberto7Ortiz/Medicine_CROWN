from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)



# ==================================
# Database path
# ==================================

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "medicion_crown.db"



# ==================================
# Engine
# ==================================

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    echo=False
)



# ==================================
# Session
# ==================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)



# ==================================
# Base class
# ==================================

Base = declarative_base()



# ==================================
# Session generator
# ==================================

def get_session():

    return SessionLocal()