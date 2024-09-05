import json
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
    data = [dict(row) for row in rows]

    file_path = f'./data/{filename}'

    json_file = open(file_path, 'x')
    json_file.write(json.dumps(data, default=str, indent=4))
    json_file.close()

    print("File created and data written correctly")

    return True