from datetime import datetime

from database.repository import Repository

from database.database import engine

from database.models import (
    Station,
    AntennaSystem,
    Parameter,
    Measurement,
    Alarm
)



def test_database():


    print("\n==============================")
    print(" DATABASE TEST")
    print("==============================\n")



    repository = Repository()



    # ==================================
    # Test Station
    # ==================================

    print("Checking station...")


    station = (
        repository.get_station()
    )


    assert station is not None, \
        "Station not found"


    print(
        "Station OK:",
        station.name
    )



    # ==================================
    # Test Antenna
    # ==================================

    print("\nChecking antenna...")


    antenna = (
        repository.get_antenna()
    )


    assert antenna is not None, \
        "Antenna not found"


    print(
        "Antenna OK"
    )



    # ==================================
    # Test Parameters
    # ==================================

    print("\nChecking parameters...")


    parameters = (
        repository.get_parameters()
    )


    assert len(parameters) > 0, \
        "No parameters found"



    for parameter in parameters:

        print(
            " -",
            parameter.name,
            "channel:",
            hex(parameter.channel)
        )



    print(
        "Parameters OK:",
        len(parameters)
    )



    # ==================================
    # Save Measurement
    # ==================================

    print("\nSaving measurement...")


    measurement = {


        "timestamp":
            datetime.now(),


        "analog": {


            "rf_power": {
                "value": 100.0
            },


            "swr": {
                "value": 1.2
            },


            "alc": {
                "value": 50.0
            },


            "pa_dc_volts": {
                "value": 48.0
            },


            "pa_dc_amps": {
                "value": 10.0
            },


            "pa_temperature": {
                "value": 35.0
            },


            "supply_dc_volts": {
                "value": 50.0
            }

        }

    }



    repository.save_measurement(
        measurement
    )


    print(
        "Measurement saved"
    )



    # ==================================
    # Read Measurement
    # ==================================

    print("\nReading measurements...")


    measurements = (
        repository.get_measurements()
    )


    assert len(measurements) > 0, \
        "No measurements found"



    last = measurements[0]


    print(
        "Last RF Power:",
        last.rf_power
    )


    print(
        "Measurement OK"
    )



    # ==================================
    # Alarm Test
    # ==================================

    print("\nCreating alarm...")


    alarm_data = {


        "station_id":
            station.id,


        "start_time":
            datetime.now(),


        "alarm_source":
            "TEST",


        "alarm_level":
            "WARNING",


        "alarm_description":
            "Database test alarm",


        "status":
            "ACTIVE"

    }



    alarm = (
        repository.create_alarm(
            alarm_data
        )
    )


    assert alarm.id is not None


    print(
        "Alarm OK:",
        alarm.id
    )



    # ==================================
    # Close
    # ==================================

    repository.close()


    print("\n==============================")
    print(" DATABASE TEST PASSED")
    print("==============================\n")




if __name__ == "__main__":

    test_database()