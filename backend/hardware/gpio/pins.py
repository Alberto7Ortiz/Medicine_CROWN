# backend/hardware/gpio/pins.py


class Pins:
    """
    Definición de pines GPIO en modo BCM.
    """

    # Salidas
    CARRIER = 25
    AUTO_CARRIER = 24

    # Entrada
    FAIL = 23


    # Raspberry PI ADS1256
    DRDY = 22           
    CS = 8 