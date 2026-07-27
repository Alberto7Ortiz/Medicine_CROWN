#!/usr/bin/env python3

import sqlite3
import os


# =====================================================
# Ruta de la base de datos
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE_FILE = os.path.join(
    BASE_DIR,
    "crown.db"
)



# =====================================================
# Crear conexión
# =====================================================

def get_connection():

    connection = sqlite3.connect(
        DATABASE_FILE
    )

    # Permite acceder a las columnas
    # por nombre además de índice

    connection.row_factory = sqlite3.Row


    # Activar relaciones entre tablas

    connection.execute(
        "PRAGMA foreign_keys = ON;"
    )


    return connection



# =====================================================
# Ejecutar consulta SELECT
# =====================================================

def fetch_all(query, params=()):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        query,
        params
    )


    result = cursor.fetchall()


    connection.close()


    return result



# =====================================================
# Obtener un solo registro
# =====================================================

def fetch_one(query, params=()):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        query,
        params
    )


    result = cursor.fetchone()


    connection.close()


    return result



# =====================================================
# Insertar / actualizar / eliminar
# =====================================================

def execute(query, params=()):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        query,
        params
    )


    connection.commit()


    last_id = cursor.lastrowid


    connection.close()


    return last_id



# =====================================================
# Prueba de conexión
# =====================================================

def test_connection():

    try:

        connection = get_connection()


        cursor = connection.cursor()


        cursor.execute(
            "SELECT sqlite_version();"
        )


        version = cursor.fetchone()[0]


        connection.close()


        print(
            "SQLite funcionando:",
            version
        )


        return True


    except Exception as error:

        print(
            "Error de conexión:",
            error
        )

        return False



# =====================================================
# Ejecución directa
# =====================================================

if __name__ == "__main__":

    test_connection()