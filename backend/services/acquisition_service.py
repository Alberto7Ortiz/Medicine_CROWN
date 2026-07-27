from collections import deque
from datetime import datetime
from threading import Thread, Lock
import time


class AcquisitionService:
    """
    Servicio encargado de adquirir las lecturas
    del transmisor y mantenerlas en memoria.
    """

    def __init__(
        self,
        adc_controller,
        gpio_service,
        repository
    ):

        self._adc = adc_controller

        self._gpio = gpio_service

        self._repository = repository


        # Buffer circular de 10000 elementos
        self._buffer = deque(
            maxlen=10000
        )


        self._lock = Lock()


        # Configuración de parámetros
        self._parameters = []


        self._running = False

        self._thread = None



    # ==================================
    # START SERVICE
    # ==================================

    def start(self):

        # Inicializar ADS1256
        self._adc.initialize()


        # Obtener configuración desde DB
        self._parameters = (
            self._repository
            .get_parameters()
        )


        self._running = True


        self._thread = Thread(
            target=self._run,
            daemon=True
        )


        self._thread.start()



    # ==================================
    # STOP SERVICE
    # ==================================

    def stop(self):

        self._running = False


        if self._thread:

            self._thread.join(
                timeout=2
            )


        self._adc.close()



    # ==================================
    # HILO DE ADQUISICIÓN
    # ==================================

    def _run(self):

        while self._running:


            measurement = (
                self._create_measurement()
            )


            with self._lock:

                self._buffer.append(
                    measurement
                )


            # frecuencia de lectura
            time.sleep(0.1)



    # ==================================
    # CREAR UNA LECTURA COMPLETA
    # ==================================

    def _create_measurement(self):

        measurement = {

            "timestamp":
                datetime.now(),


            "analog": {},


            "digital": {}

        }



        # ------------------------------
        # Lecturas ADS1256
        # ------------------------------

        for parameter in self._parameters:


            measurement["analog"][
                parameter.name
            ] = (

                self._read_analog(
                    parameter
                )

            )



        # ------------------------------
        # Estados GPIO
        # ------------------------------

        measurement["digital"] = {

            "carrier":
                self._gpio
                .get_carrier_status(),


            "auto_carrier":
                self._gpio
                .get_auto_carrier_status(),


            "failure":
                self._gpio
                .is_fail_active()

        }


        return measurement



    # ==================================
    # LECTURA DE PARAMETRO ANALOGICO
    # ==================================

    def _read_analog(
        self,
        parameter
    ):


        # Selecciona canal ADS1256
        self._adc.channel(
            parameter.channel
        )


        # Lee ADC
        raw_adc = (
            self._adc.read()
        )



        # Conversión ADC -> voltaje
        voltage = (
            self._adc_to_voltage(
                raw_adc
            )
        )



        # Aplicación de calibración
        value = (

            voltage *
            parameter.gain

            +

            parameter.offset

        )



        # Evaluación de estado
        status = (
            self._check_status(
                value,
                parameter
            )
        )



        return {

            "raw_adc": raw_adc,

            "voltage": voltage,

            "value": value,

            "status": status

        }



    # ==================================
    # ADC -> VOLTAJE
    # ==================================

    def _adc_to_voltage(
        self,
        raw_adc
    ):

        # Esta ecuación depende
        # de referencia y PGA

        return raw_adc * (
            2.5 / 8388607
        )



    # ==================================
    # COMPARACION DE LIMITES
    # ==================================

    def _check_status(
        self,
        value,
        parameter
    ):


        if value <= parameter.alarm_low:

            return "ALARM_LOW"



        if value <= parameter.warning_low:

            return "WARNING_LOW"



        if value >= parameter.alarm_high:

            return "ALARM_HIGH"



        if value >= parameter.warning_high:

            return "WARNING_HIGH"



        return "NORMAL"



    # ==================================
    # BUFFER
    # ==================================

    def get_last(self):

        with self._lock:

            if len(self._buffer) == 0:

                return None


            return self._buffer[-1]



    def get_buffer(self):

        with self._lock:

            return list(
                self._buffer
            )



    # ==================================
    # ACTUALIZAR CONFIGURACION
    # ==================================

    def reload_configuration(self):

        self._parameters = (
            self._repository
            .get_parameters()
        )