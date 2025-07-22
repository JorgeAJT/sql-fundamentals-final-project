import logging
from src.utils import database_connection, insert_data_from_json, fetch_data_as_json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run_database_insertions(args, data_path, environment):
    try:
        conn = database_connection()

        if args.all:
            insert_data_from_json(f"{data_path}/meter_data.json", conn, "meter_data")
            insert_data_from_json(f"{data_path}/meter_readings.json", conn, "meter_readings")
            insert_data_from_json(f"{data_path}/mandate_data.json", conn, "mandate_data")

        elif args.insert and args.table:
            insert_data_from_json(f"{data_path}/{args.insert}", conn, args.table)

        if environment == "development" and args.fetch and args.outfile:
            fetch_data_as_json(conn, args.fetch, args.outfile)

        conn.close()
    except Exception as e:
        logging.error(f"Error: {e}")
        raise e
