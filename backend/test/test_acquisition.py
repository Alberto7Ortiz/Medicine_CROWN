#!/usr/bin/env python3

import time

from database.init_database import create_database

from services.acquisition_service import AcquisitionService

from core.acquisition_thread import AcquisitionThread



def main():

    print("")
    print("==============================")
    print(" TEST ACQUISITION SYSTEM ")
    print("==============================")
    print("")


    # ==================================
    # DATABASE
    # ==================================

    print("Inicializando base de datos...")

    create_database()



    # ==================================
    # ACQUISITION SERVICE
    # ==================================

    print("Creando AcquisitionService...")

    acquisition_service = AcquisitionService()



    # ==================================
    # HARDWARE INITIALIZE
    # ==================================

    print("Inicializando ADS1256...")

    acquisition_service.initialize()



    # ==================================
    # THREAD
    # ==================================

    print("Iniciando hilo de adquisición...")


    acquisition_thread = AcquisitionThread(
        acquisition_service,
        interval=1.0
    )


    acquisition_thread.start()



    # ==================================
    # MONITOR BUFFER
    # ==================================

    try:

        while True:

            sample = acquisition_service.get_last()


            if sample:

                print("")
                print("==============================")
                print(" ULTIMA MUESTRA ")
                print("==============================")

                print(sample)



            time.sleep(2)



    except KeyboardInterrupt:


        print("")
        print("Deteniendo adquisición...")


        acquisition_thread.stop()



if __name__ == "__main__":

    main()