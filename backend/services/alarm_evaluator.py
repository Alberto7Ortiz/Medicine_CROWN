from models.status import Status


class AlarmEvaluator:
    """
    Evaluates the status of a parameter
    according to its configured limits.
    """


    def evaluate(self, value, parameter_config):
        """
        Evaluate parameter status.

        Returns:
            Status.NORMAL
            Status.WARNING
            Status.ALARM
        """


        alarm_low = parameter_config.get("alarm_low")
        alarm_high = parameter_config.get("alarm_high")

        warning_low = parameter_config.get("warning_low")
        warning_high = parameter_config.get("warning_high")


        # ==============================
        # ALARMS
        # ==============================

        if alarm_low is not None:

            if value <= alarm_low:
                return Status.ALARM


        if alarm_high is not None:

            if value >= alarm_high:
                return Status.ALARM



        # ==============================
        # WARNINGS
        # ==============================

        if warning_low is not None:

            if value <= warning_low:
                return Status.WARNING


        if warning_high is not None:

            if value >= warning_high:
                return Status.WARNING



        # ==============================
        # NORMAL
        # ==============================

        return Status.NORMAL