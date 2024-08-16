CREATE TABLE mandate_data
(
    mandate_id int PRIMARY KEY,
    business_partner_id varchar(200) UNIQUE,
    brand brand_enum,
    mandate_status varchar(50),
    collection_frequency varchar(50),
    row_update_datetime timestamp,
    row_create_datetime timestamp,
    changed_by varchar(150),
    collection_type varchar(50),
    metering_consent varchar(150)
);
