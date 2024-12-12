import json
import logging
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
from typing import List
from .database_functions import database_insertions


def read_json_file(file_path: str) -> List:
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data


def insert_data_from_json(filepath: str, conn: connection, table_name: str) -> bool:
    data_list = read_json_file(filepath)
    database_insertions(conn, table_name, data_list)

    return True


def fetch_data_as_json(conn: connection, query: str, filename: str) -> bool:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query)

    rows = cursor.fetchall()
    if not rows:
        logging.warning("No data found for the given query.")
        return False

    file_path = f'./data/{filename}'
    with open(file_path, 'x') as json_file:
        json_file.write(json.dumps(rows, default=str, indent=4))

    logging.info("File created and data written correctly")

    return True