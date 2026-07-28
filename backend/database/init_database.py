#!/usr/bin/env python3

import sqlite3
import os


# =====================================================
# Paths
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
# Create Database
# =====================================================

def create_database():

    # If database exists, do not recreate it
    if os.path.exists(DATABASE_FILE):

        print("Database already exists:")
        print(DATABASE_FILE)

        return



    print("Creating database...")


    connection = sqlite3.connect(
        DATABASE_FILE
    )


    cursor = connection.cursor()



    # Enable foreign key support
    cursor.execute(
        "PRAGMA foreign_keys = ON;"
    )



    # Execute schema.sql

    with open(
        SCHEMA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        schema = file.read()

        cursor.executescript(schema)



    print("Database tables created successfully")



    # Execute seed.sql

    with open(
        SEED_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        seed = file.read()

        cursor.executescript(seed)



    print("Initial data loaded successfully")



    connection.commit()

    connection.close()



    print("")
    print("================================")
    print("CROWN DATABASE READY")
    print("================================")
    print(DATABASE_FILE)



# =====================================================
# Main Program
# =====================================================

if __name__ == "__main__":

    create_database()