#!/usr/bin/env python3

import time


from database.init_database import create_database

from services.acquisition_service import AcquisitionService

from core.acquisition_thread import AcquisitionThread



def print_sample(sample):

    print("")
    print("==============================")
    print(" ACQUISITION SAMPLE ")
    print("==============================")


    if sample.rf_power:
        print(
            f"RF Power: {sample.rf_power.value}"
        )


    if sample.swr:
        print(
            f"SWR: {sample.swr.value}"
        )


    if sample.alc:
        print(
            f"ALC: {sample.alc.value}"
        )


    if sample.pa_dc_volts:
        print(
            f"PA DC Volts: {sample.pa_dc_volts.value}"
        )


    if sample.pa_dc_amps:
        print(
            f"PA DC Amps: {sample.pa_dc_amps.value}"
        )


    if sample.pa_temperature:
        print(
            f"PA Temperature: {sample.pa_temperature.value}"
        )


    if sample.supply_dc_volts:
        print(
            f"Supply DC Volts: {sample.supply_dc_volts.value}"
        )


    print("------------------------------")

    print(
        f"Carrier: {sample.carrier}"
    )

    print(
        f"Auto Carrier: {sample.auto_carrier}"
    )

    print(
        f"Fail: {sample.fail}"
    )



def main():

    print("")
    print("==============================")
    print(" CROWN ACQUISITION TEST ")
    print("==============================")
    print("")


    # ==================================
    # DATABASE
    # ==================================

    print("Initializing database...")

    create_database()



    # ==================================
    # ACQUISITION SERVICE
    # ==================================

    print("Creating AcquisitionService...")

    acquisition_service = AcquisitionService()



    # ==================================
    # HARDWARE
    # ==================================

    print("Initializing hardware...")

    acquisition_service.initialize()



    # ==================================
    # ACQUISITION THREAD
    # ==================================

    print("Starting acquisition thread...")

    acquisition_thread = AcquisitionThread(
        acquisition_service,
        interval=1.0
    )


    acquisition_thread.start()



    print("")
    print("Acquisition running...")
    print("Press CTRL+C to stop")
    print("")



    try:

        while True:

            sample = acquisition_service.get_last()


            if sample:

                print_sample(
                    sample
                )


            time.sleep(2)



    except KeyboardInterrupt:

        print("")
        print("Stopping acquisition...")



    finally:

        acquisition_thread.stop()

        print("Acquisition stopped")



if __name__ == "__main__":

    main()