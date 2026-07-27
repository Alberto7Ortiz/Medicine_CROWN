#!/usr/bin/env python3

import sqlite3
import os
from datetime import datetime



# =====================================================
# Rutas
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


DATABASE_FILE = os.path.join(
    BASE_DIR,
    "crown.db"
)


BACKUP_DIR = os.path.join(
    BASE_DIR,
    "backup"
)



# =====================================================
# Crear respaldo
# =====================================================

def create_backup():


    if not os.path.exists(DATABASE_FILE):

        print(
            "Error: No existe crown.db"
        )

        return False



    # Crear carpeta backup

    if not os.path.exists(BACKUP_DIR):

        os.makedirs(BACKUP_DIR)



    # Nombre del archivo

    timestamp = datetime.now().strftime(
        "%Y_%m_%d_%H_%M_%S"
    )


    backup_file = os.path.join(
        BACKUP_DIR,
        f"crown_backup_{timestamp}.db"
    )



    try:

        source = sqlite3.connect(
            DATABASE_FILE
        )


        destination = sqlite3.connect(
            backup_file
        )


        # Copia segura de SQLite

        with destination:

            source.backup(
                destination
            )


        source.close()

        destination.close()



        print(
            "Backup creado correctamente:"
        )

        print(
            backup_file
        )


        return True



    except Exception as error:


        print(
            "Error creando backup:"
        )

        print(error)


        return False



# =====================================================
# Ejecución directa
# =====================================================

if __name__ == "__main__":

    create_backup()