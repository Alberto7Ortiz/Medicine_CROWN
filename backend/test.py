#!/usr/bin/env python3

import os
import sqlite3


# =====================================================
# Ruta de la base de datos
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


DATABASE_FILE = os.path.join(
    BASE_DIR,
    "database",
    "crown.db"
)



# =====================================================
# Conexión
# =====================================================

def connect():

    if not os.path.exists(DATABASE_FILE):

        print("ERROR: No existe crown.db")
        return None


    connection = sqlite3.connect(
        DATABASE_FILE
    )

    connection.row_factory = sqlite3.Row

    return connection



# =====================================================
# Verificar tablas
# =====================================================

def test_tables(connection):

    print("\n[1] Verificando tablas...")


    cursor = connection.cursor()


    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
    """)


    tables = [
        row["name"]
        for row in cursor.fetchall()
    ]


    expected = [
        "system_config",
        "station",
        "tower_antenna_info",
        "parameters",
        "measurements",
        "alarms",
        "alarm_recipients",
        "email_config"
    ]


    for table in expected:

        if table in tables:
            print(f" OK  {table}")

        else:
            print(f" FAIL {table}")


# =====================================================
# Verificar parametros
# =====================================================

def test_parameters(connection):

    print("\n[2] Verificando parametros...")


    cursor = connection.cursor()


    cursor.execute("""
        SELECT
            name,
            channel
        FROM parameters
        ORDER BY id;
    """)


    parameters = cursor.fetchall()


    expected = {
        "rf_power": "0x10",
        "swr": "0x20",
        "alc": "0x30",
        "pa_dc_volts": "0x40",
        "pa_dc_amps": "0x50",
        "pa_temperature": "0x60",
        "supply_dc_volts": "0x70"
    }


    for row in parameters:

        name = row["name"]
        channel = row["channel"]


        if name in expected and expected[name] == channel:

            print(
                f" OK  {name} -> {channel}"
            )

        else:

            print(
                f" FAIL {name} -> {channel}"
            )



# =====================================================
# Verificar configuración inicial
# =====================================================

def test_system_config(connection):

    print("\n[3] Verificando system_config...")


    cursor = connection.cursor()


    cursor.execute("""
        SELECT *
        FROM system_config
        LIMIT 1;
    """)


    config = cursor.fetchone()


    if config is None:

        print(
            " FAIL No existe configuración inicial"
        )

        return


    print(
        " configured:",
        config["configured"]
    )

    print(
        " alarm_enabled:",
        config["alarm_enabled"]
    )

    print(
        " max_measurements:",
        config["max_measurements"]
    )



# =====================================================
# Prueba principal
# =====================================================

def main():

    print("==============================")
    print(" TEST CROWN DATABASE")
    print("==============================")


    connection = connect()


    if connection is None:

        return


    print("\nBase encontrada:")
    print(DATABASE_FILE)


    test_tables(connection)

    test_parameters(connection)

    test_system_config(connection)


    connection.close()


    print("\n==============================")
    print(" TEST FINALIZADO")
    print("==============================")



if __name__ == "__main__":

    main()