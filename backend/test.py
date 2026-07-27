import time


from hardware.ads1256.driver import ADS1256Controller

from services.gpio_service import GpioService

from services.acquisition_service import AcquisitionService

from database.repository import Repository



def main():


    print("================================")
    print(" TEST ACQUISITION SERVICE")
    print("================================")


    # -------------------------------
    # Hardware
    # -------------------------------

    adc = ADS1256Controller()


    gpio = GpioService()



    # -------------------------------
    # Database
    # -------------------------------

    repository = Repository()



    # Verificar parámetros

    parameters = repository.get_parameters()


    print("\nParametros cargados:")

    for parameter in parameters:

        print(
            parameter.name,
            hex(parameter.channel)
        )


    # -------------------------------
    # Servicio lectura
    # -------------------------------

    acquisition = AcquisitionService(

        adc_controller=adc,

        gpio_service=gpio,

        repository=repository

    )



    try:


        acquisition.start()


        print("\nAdquisicion iniciada...")


        while True:


            measurement = (
                acquisition.get_last()
            )


            if measurement:


                print("\n==============================")

                print(
                    "Timestamp:"
                )

                print(
                    measurement["timestamp"]
                )


                print("\nANALOG")


                for name, data in measurement["analog"].items():


                    print(
                        name,
                        data
                    )


                print("\nDIGITAL")


                print(
                    measurement["digital"]
                )



            time.sleep(2)



    except KeyboardInterrupt:


        print("\nDeteniendo...")


    finally:


        acquisition.stop()

        gpio.cleanup()



if __name__ == "__main__":

    main()