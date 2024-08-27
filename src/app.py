from src.utils import database_connection, insert_data_from_json

def run_database_insertions():
    try:
        print("Connecting with the db ...")
        conn = database_connection()

        insert_data_from_json('./data/meter_data.json', conn, 'meter_data')

        insert_data_from_json('./data/meter_readings.json', conn, 'meter_readings')

        insert_data_from_json('./data/mandate_data.json', conn, 'mandate_data')

    except Exception as e:
        print(f"Error: {e}")
        raise e