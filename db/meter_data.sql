CREATE TABLE meter_data
(
    meter_number varchar(250) PRIMARY KEY,
    connection_ean_code varchar(200) UNIQUE,
    business_partner_id varchar(200) UNIQUE,
    brand brand_enum,
    utility_type utility_type_enum
    grid_company_code varchar(200),
    oda_code varchar(200),
    smart_collectable varchar(50),
    sjv1 float,
    sjv2 float,
    installation varchar(200),
    division varchar(50),
    move_out_date timestamp,
    row_create_datetime timestamp,
    move_in_date timestamp
);
