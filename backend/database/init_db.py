from database.database import Base, engine
from database.models import Station, Parameter
from database.database import get_session



def initialize_database():


    # Crear tablas

    Base.metadata.create_all(
        engine
    )


    session = get_session()



    # -------------------------------
    # Crear estación
    # -------------------------------

    station = Station(

        name="",

        callsign="",

        location="",

        frequency=0,

        tpo=0,

        timezone="",

        description=""

    )


    session.add(station)

    session.commit()



    # -------------------------------
    # Crear parámetros
    # -------------------------------

    parameters = [


        {
            "name": "rf_power",
            "display_name": "RF Power",
            "channel": 0x10,
            "unit": "W"
        },


        {
            "name": "swr",
            "display_name": "SWR",
            "channel": 0x20,
            "unit": ""
        },


        {
            "name": "alc",
            "display_name": "ALC",
            "channel": 0x30,
            "unit": "%"
        },


        {
            "name": "pa_dc_volts",
            "display_name": "PA DC Volts",
            "channel": 0x40,
            "unit": "V"
        },


        {
            "name": "pa_dc_amps",
            "display_name": "PA DC Amps",
            "channel": 0x50,
            "unit": "A"
        },


        {
            "name": "pa_temperature",
            "display_name": "PA Temperature",
            "channel": 0x60,
            "unit": "°C"
        },


        {
            "name": "supply_dc_volts",
            "display_name": "Supply DC Volts",
            "channel": 0x70,
            "unit": "V"
        }

    ]



    for item in parameters:


        parameter = Parameter(

            station_id=station.id,


            name=item["name"],

            display_name=item["display_name"],

            channel=item["channel"],

            unit=item["unit"],


            gain=1.0,

            offset=0.0,


            nominal_value=0,


            warning_low=0,

            warning_high=0,


            alarm_low=0,

            alarm_high=0,


            configured=False


        )


        session.add(parameter)



    session.commit()


    session.close()



if __name__ == "__main__":

    initialize_database()