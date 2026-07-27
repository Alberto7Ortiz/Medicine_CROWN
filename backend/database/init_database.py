#!/usr/bin/env python3

import sqlite3
import os


# =====================================================
# Rutas
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_FILE = os.path.join(
    BASE_DIR,
    "crown.db"
)

SCHEMA_FILE = os.path.join(
    BASE_DIR,
    "schema.sql"
)

SEED_FILE = os.path.join(
    BASE_DIR,
    "seed.sql"
)



# =====================================================
# Crear base de datos
# =====================================================

def create_database():

    # Si existe, no la recrea
    if os.path.exists(DATABASE_FILE):

        print("La base de datos ya existe:")
        print(DATABASE_FILE)

        return



    print("Creando base de datos...")


    connection = sqlite3.connect(
        DATABASE_FILE
    )


    cursor = connection.cursor()



    # Activar llaves foráneas
    cursor.execute(
        "PRAGMA foreign_keys = ON;"
    )



    # Ejecutar schema.sql

    with open(
        SCHEMA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        schema = file.read()

        cursor.executescript(schema)



    print("Tablas creadas correctamente")



    # Ejecutar seed.sql

    with open(
        SEED_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        seed = file.read()

        cursor.executescript(seed)



    print("Datos iniciales cargados correctamente")



    connection.commit()

    connection.close()



    print("")
    print("================================")
    print("CROWN DATABASE LISTA")
    print("================================")
    print(DATABASE_FILE)



# =====================================================
# Programa principal
# =====================================================

if __name__ == "__main__":

    create_database()