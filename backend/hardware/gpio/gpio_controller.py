import RPi.GPIO as GPIO

from hardware.gpio.pins import Pins


class GpioController:
    """
    Controlador de entradas y salidas GPIO.
    """

    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        # Carrier
        GPIO.setup(
            Pins.CARRIER,
            GPIO.OUT,
            initial=GPIO.LOW
        )

        # Auto Carrier
        GPIO.setup(
            Pins.AUTO_CARRIER,
            GPIO.OUT,
            initial=GPIO.HIGH
        )

        # Fail con resistencia pull-up interna
        GPIO.setup(
            Pins.FAIL,
            GPIO.IN,
            pull_up_down=GPIO.PUD_UP
        )


    def carrier_enable(self):
        """
        Activa Carrier.
        """
        GPIO.output(
            Pins.CARRIER,
            GPIO.HIGH
        )


    def carrier_disable(self):
        """
        Desactiva Carrier.
        """
        GPIO.output(
            Pins.CARRIER,
            GPIO.LOW
        )


    def auto_carrier_enable(self):
        """
        Activa AutoCarrier.
        """
        GPIO.output(
            Pins.AUTO_CARRIER,
            GPIO.HIGH
        )


    def auto_carrier_disable(self):
        """
        Desactiva AutoCarrier.
        """
        GPIO.output(
            Pins.AUTO_CARRIER,
            GPIO.LOW
        )


    def is_fail_active(self):
        """
        La entrada FAIL es activa en LOW.
        """
        return GPIO.input(Pins.FAIL) == GPIO.LOW


    def cleanup(self):
        """
        Libera GPIO.
        """
        GPIO.cleanup()