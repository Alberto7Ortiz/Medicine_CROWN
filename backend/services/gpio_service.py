from hardware.gpio.gpio_controller import GpioController


class GpioService:
    """
    Servicio de gestión GPIO.
    """


    def __init__(self):

        self._gpio = GpioController()



    # ==================================
    # CARRIER
    # ==================================

    def carrier_enable(self):
        self._gpio.carrier_enable()


    def carrier_disable(self):
        self._gpio.carrier_disable()


    def get_carrier_status(self):
        return self._gpio.get_carrier_status()



    # ==================================
    # AUTO CARRIER
    # ==================================

    def auto_carrier_enable(self):
        self._gpio.auto_carrier_enable()


    def auto_carrier_disable(self):
        self._gpio.auto_carrier_disable()


    def get_auto_carrier_status(self):
        return self._gpio.get_auto_carrier_status()



    # ==================================
    # INPUT FAIL
    # ==================================

    def is_fail_active(self):
        return self._gpio.is_fail_active()



    # ==================================
    # CLEANUP
    # ==================================

    def cleanup(self):
        self._gpio.cleanup()