-- =====================================================
-- CROWN MONITOR DATABASE
-- seed.sql
-- Initial Factory Data
-- =====================================================


-- =====================================================
-- INITIAL SYSTEM CONFIGURATION
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
    'Device pending initial configuration'
);



-- =====================================================
-- INITIAL MEASUREMENT PARAMETERS
-- Factory default limits are used until configuration
-- is completed.
-- =====================================================

INSERT INTO parameters
(
    name,
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
)
VALUES

(
    'rf_power',
    'RF Power',
    '0x10',
    'W',
    1,
    0,
    0,
    -999999,
    999999,
    -999999,
    999999,
    'RF output power'
),


(
    'swr',
    'SWR',
    '0x20',
    '',
    1,
    0,
    0,
    -999999,
    999999,
    -999999,
    999999,
    'Standing wave ratio'
),


(
    'alc',
    'ALC',
    '0x30',
    'V',
    1,
    0,
    0,
    -999999,
    999999,
    -999999,
    999999,
    'Automatic level control voltage'
),


(
    'pa_dc_volts',
    'PA DC Volts',
    '0x40',
    'V',
    1,
    0,
    0,
    -999999,
    999999,
    -999999,
    999999,
    'Power amplifier DC voltage'
),


(
    'pa_dc_amps',
    'PA DC Amps',
    '0x50',
    'A',
    1,
    0,
    0,
    -999999,
    999999,
    -999999,
    999999,
    'Power amplifier DC current'
),


(
    'pa_temperature',
    'PA Temperature',
    '0x60',
    'C',
    1,
    0,
    0,
    -999999,
    999999,
    -999999,
    999999,
    'Power amplifier temperature'
),


(
    'supply_dc_volts',
    'Supply DC Volts',
    '0x70',
    'V',
    1,
    0,
    0,
    -999999,
    999999,
    -999999,
    999999,
    'Main supply voltage'
);



-- =====================================================
-- INITIAL STATION INFORMATION
-- Completed during system configuration
-- =====================================================

INSERT INTO station
(
    description
)
VALUES
(
    'Station information pending configuration'
);



-- =====================================================
-- INITIAL TOWER AND ANTENNA INFORMATION
-- Completed during system configuration
-- =====================================================

INSERT INTO tower_antenna_info
(
    description
)
VALUES
(
    'Tower and antenna information pending configuration'
);



-- =====================================================
-- INITIAL EMAIL CONFIGURATION
-- Disabled by default
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