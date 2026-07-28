from models.status import Status


class AlarmEvaluator:
    """
    Evalúa el estado de un parámetro
    según sus límites configurados.
    """


    def evaluate(self, value, parameter_config):
        """
        Recibe:

        value:
            Valor real calculado del parámetro.

        parameter_config:
            Configuración obtenida desde ParameterService.

        Retorna:

            Status.NORMAL
            Status.WARNING
            Status.ALARM
        """


        alarm_low = parameter_config["alarm_low"]
        alarm_high = parameter_config["alarm_high"]

        warning_low = parameter_config["warning_low"]
        warning_high = parameter_config["warning_high"]



        # ==============================
        # ALARMAS
        # ==============================

        if value <= alarm_low:

            return Status.ALARM


        if value >= alarm_high:

            return Status.ALARM



        # ==============================
        # WARNINGS
        # ==============================

        if value <= warning_low:

            return Status.WARNING


        if value >= warning_high:

            return Status.WARNING



        # ==============================
        # NORMAL
        # ==============================

        return Status.NORMAL