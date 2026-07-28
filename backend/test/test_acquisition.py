import time

from services.acquisition_service import AcquisitionService
from core.acquisition_thread import AcquisitionThread



def main():

    print("==============================")
    print(" TEST ACQUISITION SERVICE")
    print("==============================")


    # Crear servicio de adquisición

    acquisition_service = AcquisitionService()



    # Crear hilo continuo

    acquisition_thread = AcquisitionThread(
        acquisition_service,
        interval=0.1
    )



    print("Iniciando adquisición...")


    acquisition_thread.start()



    try:

        while True:

            # Obtener última muestra

            last = acquisition_service.get_last()


            if last:

                print("\n--- ULTIMA MUESTRA ---")


                print(last)



            else:

                print(
                    "Esperando primera muestra..."
                )


            time.sleep(1)



    except KeyboardInterrupt:


        print("\nDeteniendo adquisición...")


        acquisition_thread.stop()


        print("Test finalizado")



if __name__ == "__main__":

    main()