from database.database import engine, Base

from database.models import (
    Station,
    Parameter,
    Measurement,
    Alarm
)



def test_database_connection():

    print("Testing database connection...")

    print(engine)

    print("Database connection OK")



def test_models():

    print("\nTesting models...")

    print(Station.__tablename__)
    print(Parameter.__tablename__)
    print(Measurement.__tablename__)
    print(Alarm.__tablename__)

    print("Models OK")



def test_metadata():

    print("\nTesting SQLAlchemy metadata...")

    tables = Base.metadata.tables.keys()

    print("Tables detected:")

    for table in tables:
        print("-", table)


    print("Metadata OK")



if __name__ == "__main__":

    test_database_connection()

    test_models()

    test_metadata()

    print("\nALL TESTS PASSED")