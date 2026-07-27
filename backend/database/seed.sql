-- =====================================================
-- CROWN MONITOR DATABASE
-- seed.sql
-- Initial Factory Data
-- =====================================================


-- =====================================================
-- CONFIGURACION INICIAL DEL SISTEMA
-- =====================================================

INSERT INTO system_config
(
    configured,
    alarm_enabled,
    max_measurements,
    measurement_interval,
    device_name,
    description
)
VALUES
(
    0,
    0,
    5475,
    1,
    'CROWN_MONITOR',
    'Equipo pendiente de configuracion inicial'
);



-- =====================================================
-- PARAMETROS INICIALES DE MEDICION
-- =====================================================


INSERT INTO parameters
(
    name,
    display_name,
    channel,
    unit,
    gain,
    offset,
    description
)
VALUES

(
    'rf_power',
    'RF Power',
    '0x10',
    'W',
    1,
    0,
    'Potencia de salida RF'
),


(
    'swr',
    'SWR',
    '0x20',
    'ratio',
    1,
    0,
    'Relacion de onda estacionaria'
),


(
    'alc',
    'ALC',
    '0x30',
    '%',
    1,
    0,
    'Control automatico de nivel'
),


(
    'pa_dc_volts',
    'PA DC Volts',
    '0x40',
    'V',
    1,
    0,
    'Voltaje DC del amplificador'
),


(
    'pa_dc_amps',
    'PA DC Amps',
    '0x50',
    'A',
    1,
    0,
    'Corriente DC del amplificador'
),


(
    'pa_temperature',
    'PA Temperature',
    '0x60',
    'C',
    1,
    0,
    'Temperatura del amplificador'
),


(
    'supply_dc_volts',
    'Supply DC Volts',
    '0x70',
    'V',
    1,
    0,
    'Voltaje principal de alimentacion'
);



-- =====================================================
-- ESTACION INICIAL
-- SE COMPLETA EN LA CONFIGURACION
-- =====================================================

INSERT INTO station
(
    description
)
VALUES
(
    'Estacion pendiente de configuracion'
);



-- =====================================================
-- TORRE Y ANTENA INICIAL
-- SE COMPLETA EN LA CONFIGURACION
-- =====================================================

INSERT INTO tower_antenna_info
(
    description
)
VALUES
(
    'Informacion de torre y antena pendiente de configuracion'
);



-- =====================================================
-- CONFIGURACION INICIAL DE CORREO
-- DESACTIVADA
-- =====================================================

INSERT INTO email_config
(
    enabled,
    use_ssl,
    use_tls
)
VALUES
(
    0,
    0,
    1
);