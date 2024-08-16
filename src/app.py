from src.utils import connect_to_db, read_json_file, insert_into_db

def database_insertions():
    print("Connecting with the db ...")
    conn = connect_to_db()
    if conn is None:
        return None
    testing_data_list = read_json_file('./data/testing.json')
    insert_into_db(conn, 'testing_table', testing_data_list,
                    ['meter_number',
                    'connection_ean_code',
                    'account_id',
                    'brand',
                    'energy_type',
                    'reading_date',
                    'reading_electricity',
                    'reading_gas',
                    'rejection',
                    'validation_status'])