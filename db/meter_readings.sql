CREATE TABLE meter_readings
(
    meter_readings_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    meter_number varchar(200) UNIQUE,
    connection_ean_code varchar(200) UNIQUE,
    account_id varchar(200),
    brand brand_enum,
    energy_type utility_type_enum,
    reading_date date,
    reading_electricity text,
    reading_gas text,
    rejection text,
    validation_status varchar(50)
);
