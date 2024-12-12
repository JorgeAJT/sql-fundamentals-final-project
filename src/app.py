import logging
from src.utils import database_connection, insert_data_from_json, fetch_data_as_json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_database_insertions():
    try:
        conn = database_connection()

        insert_data_from_json('./data/meter_data.json', conn, 'meter_data')
        insert_data_from_json('./data/meter_readings.json', conn, 'meter_readings')
        insert_data_from_json('./data/mandate_data.json', conn, 'mandate_data')

        fetch_data_as_json(conn, "SELECT * FROM mandate_data WHERE mandate_status = 'N'", 'selected_data.json')

    except Exception as e:
        logging.error(f"Error: {e}")
        raise e