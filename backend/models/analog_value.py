from models.status import Status


class AnalogValue:
    """
    Representa el valor procesado de un canal analógico.
    """

    def __init__(self):
        # Lectura directa del ADC
        self.raw_adc = 0

        # Voltaje calculado desde ADC
        self.voltage = 0.0

        # Valor final después de gain y offset
        self.value = 0.0

        # Estado actual del parámetro
        self.status = Status.NORMAL

    def __repr__(self):
        return (
            f"AnalogValue("
            f"raw_adc={self.raw_adc}, "
            f"voltage={self.voltage:.3f}, "
            f"value={self.value:.3f}, "
            f"status={self.status.name})"
        )