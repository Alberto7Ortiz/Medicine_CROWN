from database.database import get_session

from database.models import (
    Station,
    AntennaSystem,
    Parameter,
    Measurement,
    Alarm
)



class Repository:


    def __init__(self):

        self.session = None



    # ==================================
    # SESSION
    # ==================================

    def _get_session(self):

        if self.session is None:

            self.session = get_session()

        return self.session



    # ==================================
    # STATION
    # ==================================

    def get_station(self):

        session = self._get_session()

        return (
            session.query(Station)
            .first()
        )



    def update_station(
        self,
        station_data
    ):

        station = self.get_station()


        if station is None:

            return False


        for key, value in station_data.items():

            setattr(
                station,
                key,
                value
            )


        self._get_session().commit()


        return True



    # ==================================
    # ANTENNA SYSTEM
    # ==================================

    def get_antenna(self):

        session = self._get_session()

        return (
            session.query(AntennaSystem)
            .first()
        )



    def update_antenna(
        self,
        antenna_data
    ):

        antenna = self.get_antenna()


        if antenna is None:

            return False


        for key, value in antenna_data.items():

            setattr(
                antenna,
                key,
                value
            )


        self._get_session().commit()


        return True



    # ==================================
    # PARAMETERS
    # ==================================

    def get_parameters(self):

        session = self._get_session()

        return (
            session.query(Parameter)
            .all()
        )



    def get_parameter(
        self,
        name
    ):

        session = self._get_session()

        return (
            session.query(Parameter)
            .filter(
                Parameter.name == name
            )
            .first()
        )



    def update_parameter(
        self,
        name,
        data
    ):

        parameter = self.get_parameter(name)


        if parameter is None:

            return False


        for key, value in data.items():

            setattr(
                parameter,
                key,
                value
            )


        self._get_session().commit()


        return True



    # ==================================
    # MEASUREMENTS
    # ==================================

    def save_measurement(
        self,
        measurement
    ):

        session = self._get_session()


        data = Measurement(

            station_id=1,


            measured_at=
                measurement["timestamp"],


            rf_power=
                measurement["analog"]
                ["rf_power"]
                ["value"],


            swr=
                measurement["analog"]
                ["swr"]
                ["value"],


            alc=
                measurement["analog"]
                ["alc"]
                ["value"],


            pa_dc_volts=
                measurement["analog"]
                ["pa_dc_volts"]
                ["value"],


            pa_dc_amps=
                measurement["analog"]
                ["pa_dc_amps"]
                ["value"],


            pa_temperature=
                measurement["analog"]
                ["pa_temperature"]
                ["value"],


            supply_dc_volts=
                measurement["analog"]
                ["supply_dc_volts"]
                ["value"]

        )


        session.add(data)

        session.commit()


        return data



    def get_measurements(
        self,
        limit=100
    ):

        session = self._get_session()


        return (
            session.query(Measurement)
            .order_by(
                Measurement.measured_at.desc()
            )
            .limit(limit)
            .all()
        )



    # ==================================
    # ALARMS
    # ==================================

    def create_alarm(
        self,
        alarm_data
    ):

        session = self._get_session()


        alarm = Alarm(
            **alarm_data
        )


        session.add(alarm)

        session.commit()


        return alarm



    def get_active_alarm(self):

        session = self._get_session()


        return (
            session.query(Alarm)
            .filter(
                Alarm.status == "ACTIVE"
            )
            .first()
        )



    def close_alarm(
        self,
        alarm,
        end_time
    ):

        alarm.end_time = end_time

        alarm.status = "CLEARED"


        self._get_session().commit()



    # ==================================
    # CLOSE
    # ==================================

    def close(self):

        if self.session:

            self.session.close()

            self.session = None