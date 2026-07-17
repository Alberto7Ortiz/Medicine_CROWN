from gpiozero import DigitalOutputDevice, DigitalInputDevice

from hardware.gpio.pins import Pins


class GpioController:
    """
    Controlador de entradas y salidas GPIO.
    """

    def __init__(self):

        # Carrier inicia LOW
        self.carrier = DigitalOutputDevice(
            Pins.CARRIER,
            initial_value=False
        )

        # AutoCarrier inicia HIGH
        self.auto_carrier = DigitalOutputDevice(
            Pins.AUTO_CARRIER,
            initial_value=True
        )

        # Fail utiliza pull-up interno de Raspberry
        self.fail = DigitalInputDevice(
            Pins.FAIL,
            pull_up=True
        )


    def carrier_enable(self):
        """
        Activa Carrier.
        """

        self.carrier.on()


    def carrier_disable(self):
        """
        Desactiva Carrier.
        """

        self.carrier.off()


    def auto_carrier_enable(self):
        """
        Activa AutoCarrier.
        """

        self.auto_carrier.on()


    def auto_carrier_disable(self):
        """
        Desactiva AutoCarrier.
        """

        self.auto_carrier.off()


    def is_fail_active(self):
        """
        True  -> existe falla
        False -> sistema normal

        La señal es activa en LOW.
        """

        return not self.fail.value