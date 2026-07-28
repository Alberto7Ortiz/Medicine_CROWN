from datetime import datetime


class AcquisitionSample:
    """
    Representa una lectura completa del sistema CROWN.
    Contiene los 7 canales analógicos y los estados digitales.
    """

    def __init__(self):
        # Tiempo de la adquisición
        self.timestamp = datetime.now()

        # Canales analógicos
        self.rf_power = None
        self.swr = None
        self.alc = None
        self.pa_dc_volts = None
        self.pa_dc_amps = None
        self.pa_temperature = None
        self.supply_dc_volts = None

        # Estados digitales
        self.carrier = False
        self.auto_carrier = False
        self.fail = False

    def __repr__(self):
        return (
            f"AcquisitionSample("
            f"timestamp={self.timestamp}, "
            f"rf_power={self.rf_power}, "
            f"swr={self.swr}, "
            f"carrier={self.carrier}, "
            f"fail={self.fail})"
        )