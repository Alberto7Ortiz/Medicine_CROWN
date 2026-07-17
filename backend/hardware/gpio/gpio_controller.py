import RPi.GPIO as GPIO

from hardware.gpio.pins import Pins


class GpioController:
    """
    Controlador de entradas y salidas GPIO.
    """

    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        # ==========================
        # OUTPUTS
        # ==========================

        # Carrier inicia LOW
        GPIO.setup(
            Pins.CARRIER,
            GPIO.OUT,
            initial=GPIO.LOW
        )

        # AutoCarrier inicia HIGH
        GPIO.setup(
            Pins.AUTO_CARRIER,
            GPIO.OUT,
            initial=GPIO.HIGH
        )


        # ==========================
        # INPUTS
        # ==========================

        # Fail con pull-up interno
        # Señal activa en LOW
        GPIO.setup(
            Pins.FAIL,
            GPIO.IN,
            pull_up_down=GPIO.PUD_UP
        )


    # ==================================
    # CARRIER
    # ==================================

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


    def get_carrier_status(self):
        """
        Estado actual Carrier.

        True  -> HIGH
        False -> LOW
        """

        return GPIO.input(
            Pins.CARRIER
        ) == GPIO.HIGH



    # ==================================
    # AUTO CARRIER
    # ==================================

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


    def get_auto_carrier_status(self):
        """
        Estado actual AutoCarrier.

        True  -> HIGH
        False -> LOW
        """

        return GPIO.input(
            Pins.AUTO_CARRIER
        ) == GPIO.HIGH



    # ==================================
    # FAIL INPUT
    # ==================================

    def is_fail_active(self):
        """
        FAIL activa en LOW.

        True  -> Existe falla
        False -> Sistema normal
        """

        return GPIO.input(
            Pins.FAIL
        ) == GPIO.LOW



    # ==================================
    # CLEANUP
    # ==================================

    def cleanup(self):
        """
        Libera GPIO.
        """

        GPIO.cleanup()