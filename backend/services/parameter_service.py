from database.database import fetch_all


class ParameterService:
    """
    Servicio encargado de cargar y administrar
    la configuración de los parámetros analógicos.
    """


    def __init__(self):

        self._parameters = {}

        self.load_parameters()



    # ==================================
    # CARGAR PARAMETROS
    # ==================================

    def load_parameters(self):
        """
        Carga todos los parámetros desde la base de datos.
        """

        query = """
            SELECT
                id,
                display_name,
                channel,
                unit,
                gain,
                offset,
                ideal_value,
                warning_low,
                warning_high,
                alarm_low,
                alarm_high,
                description
            FROM parameters;
        """


        rows = fetch_all(query)


        self._parameters.clear()


        for row in rows:

            channel = row["channel"]


            self._parameters[channel] = {

                "id": row["id"],

                "display_name": row["display_name"],

                "channel": channel,

                "unit": row["unit"],

                "gain": row["gain"],

                "offset": row["offset"],

                "ideal_value": row["ideal_value"],

                "warning_low": row["warning_low"],

                "warning_high": row["warning_high"],

                "alarm_low": row["alarm_low"],

                "alarm_high": row["alarm_high"],

                "description": row["description"]

            }



    # ==================================
    # OBTENER POR CANAL
    # ==================================

    def get_by_channel(self, channel):
        """
        Retorna la configuración de un canal hexadecimal.

        Ejemplo:
            "0x10"
        """

        return self._parameters.get(channel)



    # ==================================
    # OBTENER TODOS
    # ==================================

    def get_all(self):
        """
        Retorna todos los parámetros configurados.
        """

        return self._parameters



    # ==================================
    # RECARGAR CONFIGURACION
    # ==================================

    def reload(self):
        """
        Recarga los parámetros desde SQLite.
        """

        self.load_parameters()