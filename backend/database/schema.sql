-- =====================================================
-- CROWN MONITOR DATABASE
-- schema.sql
-- SQLite Database Structure
-- =====================================================


PRAGMA foreign_keys = ON;


-- =====================================================
-- CONFIGURACION GENERAL DEL SISTEMA
-- =====================================================

CREATE TABLE IF NOT EXISTS system_config (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    configured INTEGER DEFAULT 0,

    alarm_enabled INTEGER DEFAULT 0,

    max_measurements INTEGER DEFAULT 5475,

    measurement_interval INTEGER DEFAULT 1,

    device_name TEXT,

    installation_date DATETIME,

    description TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);



-- =====================================================
-- INFORMACION DE LA ESTACION
-- =====================================================

CREATE TABLE IF NOT EXISTS station (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    callsign TEXT,

    name TEXT,

    location TEXT,

    frequency REAL,

    timezone TEXT,

    description TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);



-- =====================================================
-- INFORMACION DE TORRE Y ANTENAS
-- UNA SOLA TORRE
-- =====================================================

CREATE TABLE IF NOT EXISTS tower_antenna_info (

    id INTEGER PRIMARY KEY AUTOINCREMENT,


    tower_height REAL,

    tower_height_unit TEXT DEFAULT 'm',


    tower_type TEXT,


    antenna_quantity INTEGER,


    antenna_height REAL,

    antenna_height_unit TEXT DEFAULT 'm',


    antenna_direction REAL,


    antenna_type TEXT,


    polarization TEXT,


    antenna_gain REAL,


    frequency_min REAL,

    frequency_max REAL,


    latitude REAL,

    longitude REAL,


    description TEXT,


    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);



-- =====================================================
-- PARAMETROS DE MEDICION
-- =====================================================

CREATE TABLE IF NOT EXISTS parameters (

    id INTEGER PRIMARY KEY AUTOINCREMENT,


    name TEXT NOT NULL UNIQUE,


    display_name TEXT,


    channel TEXT NOT NULL,


    unit TEXT,


    gain REAL DEFAULT 1,


    offset REAL DEFAULT 0,


    ideal_value REAL,


    warning_low REAL,

    warning_high REAL,


    alarm_low REAL,

    alarm_high REAL,


    description TEXT,


    last_status TEXT,


    last_status_time DATETIME
);



-- =====================================================
-- HISTORICO DE MEDICIONES
-- MAXIMO 5475 REGISTROS
-- =====================================================

CREATE TABLE IF NOT EXISTS measurements (

    id INTEGER PRIMARY KEY AUTOINCREMENT,


    parameter_id INTEGER NOT NULL,


    value REAL NOT NULL,


    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(parameter_id)
        REFERENCES parameters(id)
);



-- =====================================================
-- REGISTRO DE ALARMAS
-- GUARDA SNAPSHOT DE LOS 7 PARAMETROS
-- =====================================================

CREATE TABLE IF NOT EXISTS alarms (

    id INTEGER PRIMARY KEY AUTOINCREMENT,


    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,


    level TEXT,


    trigger_parameter TEXT,


    description TEXT,


    rf_power REAL,

    swr REAL,

    alc REAL,

    pa_dc_volts REAL,

    pa_dc_amps REAL,

    pa_temperature REAL,

    supply_dc_volts REAL,


    acknowledged INTEGER DEFAULT 0,


    recovered_at DATETIME
);



-- =====================================================
-- PERSONAS QUE RECIBEN ALERTAS
-- =====================================================

CREATE TABLE IF NOT EXISTS alarm_recipients (

    id INTEGER PRIMARY KEY AUTOINCREMENT,


    name TEXT,


    email TEXT,


    active INTEGER DEFAULT 1,


    description TEXT,


    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,


    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);



-- =====================================================
-- CONFIGURACION DEL SERVICIO DE CORREO
-- =====================================================

CREATE TABLE IF NOT EXISTS email_config (

    id INTEGER PRIMARY KEY AUTOINCREMENT,


    smtp_server TEXT,


    smtp_port INTEGER,


    username TEXT,


    password TEXT,


    sender_email TEXT,


    use_ssl INTEGER DEFAULT 0,


    use_tls INTEGER DEFAULT 1,


    enabled INTEGER DEFAULT 0,


    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,


    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);



-- =====================================================
-- INDICES
-- MEJORAN LAS CONSULTAS
-- =====================================================

CREATE INDEX IF NOT EXISTS idx_measurements_timestamp

ON measurements(timestamp);



CREATE INDEX IF NOT EXISTS idx_measurements_parameter

ON measurements(parameter_id);



CREATE INDEX IF NOT EXISTS idx_alarms_timestamp

ON alarms(timestamp);