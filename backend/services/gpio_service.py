from hardware.gpio.gpio_controller import GpioController


class GpioService:
    """
    Servicio para gestionar las operaciones GPIO.
    Actúa como intermediario entre la API y el controlador de hardware.
    """

    def __init__(self):
        self._gpio = GpioController()

    # ==========================
    # Carrier
    # ==========================

    def carrier_enable(self):
        """
        Activa la salida Carrier.
        """
        self._gpio.carrier_enable()

    def carrier_disable(self):
        """
        Desactiva la salida Carrier.
        """
        self._gpio.carrier_disable()

    # ==========================
    # Auto Carrier
    # ==========================

    def auto_carrier_enable(self):
        """
        Activa la salida Auto Carrier.
        """
        self._gpio.auto_carrier_enable()

    def auto_carrier_disable(self):
        """
        Desactiva la salida Auto Carrier.
        """
        self._gpio.auto_carrier_disable()

    # ==========================
    # Entradas
    # ==========================

    def is_fail_active(self) -> bool:
        """
        Retorna el estado de la entrada FAIL.

        Returns:
            bool:
                True  -> Existe una falla.
                False -> Sistema normal.
        """
        return self._gpio.is_fail_active()