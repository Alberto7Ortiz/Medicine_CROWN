from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from datetime import datetime

from .database import Base



# ==================================
# Station
# ==================================

class Station(Base):

    __tablename__ = "station"


    id = Column(
        Integer,
        primary_key=True
    )


    callsign = Column(
        String
    )


    name = Column(
        String
    )


    location = Column(
        String
    )


    frequency = Column(
        Float
    )


    tpo = Column(
        Float
    )


    timezone = Column(
        String
    )


    description = Column(
        String
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    # Relaciones

    antenna = relationship(
        "AntennaSystem",
        back_populates="station",
        uselist=False
    )


    parameters = relationship(
        "Parameter",
        back_populates="station"
    )


    measurements = relationship(
        "Measurement",
        back_populates="station"
    )


    alarms = relationship(
        "Alarm",
        back_populates="station"
    )



# ==================================
# Antenna System
# ==================================

class AntennaSystem(Base):

    __tablename__ = "antenna_system"


    id = Column(
        Integer,
        primary_key=True
    )


    station_id = Column(
        Integer,
        ForeignKey("station.id")
    )


    tower_height = Column(
        Float
    )


    antenna_type = Column(
        String
    )


    antenna_height = Column(
        Float
    )


    antenna_azimuth = Column(
        Float
    )


    antenna_quantity = Column(
        Integer
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    station = relationship(
        "Station",
        back_populates="antenna"
    )



# ==================================
# Parameter Configuration
# ==================================

class Parameter(Base):

    __tablename__ = "parameter"


    id = Column(
        Integer,
        primary_key=True
    )


    station_id = Column(
        Integer,
        ForeignKey("station.id")
    )


    name = Column(
        String,
        unique=True
    )


    display_name = Column(
        String
    )


    # ADS1256 channel

    channel = Column(
        Integer
    )


    unit = Column(
        String
    )


    # ADC conversion

    gain = Column(
        Float,
        default=1.0
    )


    offset = Column(
        Float,
        default=0.0
    )


    ideal_value = Column(
        Float
    )


    # Warning limits

    warning_low = Column(
        Float,
        nullable=True
    )


    warning_high = Column(
        Float,
        nullable=True
    )


    # Alarm limits

    alarm_low = Column(
        Float,
        nullable=True
    )


    alarm_high = Column(
        Float,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    station = relationship(
        "Station",
        back_populates="parameters"
    )



# ==================================
# Measurement History
# ==================================

class Measurement(Base):

    __tablename__ = "measurement"


    id = Column(
        Integer,
        primary_key=True
    )


    station_id = Column(
        Integer,
        ForeignKey("station.id")
    )


    measured_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    rf_power = Column(
        Float
    )


    swr = Column(
        Float
    )


    alc = Column(
        Float
    )


    pa_dc_volts = Column(
        Float
    )


    pa_dc_amps = Column(
        Float
    )


    pa_temperature = Column(
        Float
    )


    supply_dc_volts = Column(
        Float
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    station = relationship(
        "Station",
        back_populates="measurements"
    )



# ==================================
# Alarm History
# ==================================

class Alarm(Base):

    __tablename__ = "alarm"


    id = Column(
        Integer,
        primary_key=True
    )


    station_id = Column(
        Integer,
        ForeignKey("station.id")
    )


    start_time = Column(
        DateTime
    )


    end_time = Column(
        DateTime,
        nullable=True
    )


    rf_power = Column(
        Float
    )


    swr = Column(
        Float
    )


    alc = Column(
        Float
    )


    pa_dc_volts = Column(
        Float
    )


    pa_dc_amps = Column(
        Float
    )


    pa_temperature = Column(
        Float
    )


    supply_dc_volts = Column(
        Float
    )


    alarm_source = Column(
        String
    )


    alarm_level = Column(
        String
    )


    alarm_description = Column(
        String
    )


    status = Column(
        String
    )
    # ACTIVE / CLEARED


    notification_sent = Column(
        Integer,
        default=0
    )


    recovery_sent = Column(
        Integer,
        default=0
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    station = relationship(
        "Station",
        back_populates="alarms"
    )