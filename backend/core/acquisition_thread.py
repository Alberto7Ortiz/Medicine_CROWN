import threading
import time


class AcquisitionThread:
    """
    Hilo encargado de ejecutar periódicamente
    el servicio de adquisición.
    """


    def __init__(self, acquisition_service, interval=1.0):

        self._service = acquisition_service

        # Tiempo entre adquisiciones en segundos
        self._interval = interval

        self._running = False

        self._thread = None



    # ==================================
    # START
    # ==================================

    def start(self):
        """
        Inicia el hilo de adquisición.
        """

        if self._running:
            return


        self._running = True


        self._thread = threading.Thread(
            target=self._run,
            daemon=True
        )


        self._thread.start()



    # ==================================
    # LOOP DEL HILO
    # ==================================

    def _run(self):

        while self._running:

            try:

                self._service.acquire()


            except Exception as error:

                print(
                    "Error en adquisición:",
                    error
                )


            time.sleep(
                self._interval
            )



    # ==================================
    # STOP
    # ==================================

    def stop(self):
        """
        Detiene el hilo.
        """

        self._running = False


        if self._thread:

            self._thread.join()



    # ==================================
    # ESTADO
    # ==================================

    def is_running(self):

        return self._running