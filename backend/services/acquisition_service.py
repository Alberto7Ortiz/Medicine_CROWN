from hardware.ads1256.ads1256_controller import ADS1256Controller

from services.parameter_service import ParameterService
from services.alarm_evaluator import AlarmEvaluator
from services.gpio_service import GpioService

from models.analog_value import AnalogValue
from models.acquisition_sample import AcquisitionSample

from core.buffer import Buffer
from core.config import ACQUISITION_BUFFER_SIZE


class AcquisitionService:
    """
    Servicio encargado de adquirir y procesar
    las lecturas del sistema.
    """


    ADC_MAX_VALUE = 8388607
    ADC_VREF = 2.5



    def __init__(self):

        # Hardware
        self._adc = ADS1256Controller()

        # Servicios
        self._parameter_service = ParameterService()
        self._alarm_evaluator = AlarmEvaluator()
        self._gpio_service = GpioService()

        # Memoria circular
        self._buffer = Buffer(
            ACQUISITION_BUFFER_SIZE
        )



    # ==================================
    # CONVERSION ADC
    # ==================================

    def _calculate_voltage(self, raw_adc):
        """
        Convierte la lectura del ADC
        a voltaje.
        """

        return (
            raw_adc /
            self.ADC_MAX_VALUE
        ) * self.ADC_VREF



    # ==================================
    # LEER CANAL ANALOGICO
    # ==================================

    def _read_channel(self, channel, config):
        """
        Lee un canal del ADS1256
        y genera un AnalogValue.
        """

        # Seleccionar canal
        self._adc.channel(
            int(channel, 16)
        )


        # Leer ADC
        raw_adc = self._adc.read()


        # Crear valor analógico
        analog = AnalogValue()


        analog.raw_adc = raw_adc


        # Calcular voltaje
        analog.voltage = self._calculate_voltage(
            raw_adc
        )


        # Aplicar gain y offset
        analog.value = (
            analog.voltage *
            config["gain"]
        ) + config["offset"]



        # Evaluar alarma
        analog.status = self._alarm_evaluator.evaluate(
            analog.value,
            config
        )


        return analog



    # ==================================
    # CREAR MUESTRA COMPLETA
    # ==================================

    def create_sample(self):
        """
        Realiza una adquisición completa.
        """

        sample = AcquisitionSample()


        parameters = self._parameter_service.get_all()



        for channel, config in parameters.items():

            analog_value = self._read_channel(
                channel,
                config
            )


            name = config["display_name"]


            # Asignar al modelo correspondiente

            if name == "RF Power":
                sample.rf_power = analog_value


            elif name == "SWR":
                sample.swr = analog_value


            elif name == "ALC":
                sample.alc = analog_value


            elif name == "PA DC Volts":
                sample.pa_dc_volts = analog_value


            elif name == "PA DC Amps":
                sample.pa_dc_amps = analog_value


            elif name == "PA Temperature":
                sample.pa_temperature = analog_value


            elif name == "Supply DC Volts":
                sample.supply_dc_volts = analog_value



        # Lecturas digitales

        sample.carrier = (
            self._gpio_service.get_carrier_status()
        )


        sample.auto_carrier = (
            self._gpio_service.get_auto_carrier_status()
        )


        sample.fail = (
            self._gpio_service.is_fail_active()
        )


        return sample



    # ==================================
    # ADQUIRIR Y GUARDAR
    # ==================================

    def acquire(self):
        """
        Realiza una lectura completa
        y la guarda en el buffer.
        """

        sample = self.create_sample()


        self._buffer.push(
            sample
        )


        return sample



    # ==================================
    # BUFFER
    # ==================================

    def get_last(self):

        return self._buffer.get_last()



    def get_all(self):

        return self._buffer.get_all()