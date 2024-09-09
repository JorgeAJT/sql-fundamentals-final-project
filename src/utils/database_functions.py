import os
import psycopg2
import json
import logging
from dotenv import load_dotenv
from typing import List, Dict, Any


def database_connection() -> psycopg2.extensions.connection:
    logging.info("Connecting with the db ...")

    load_dotenv()
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    logging.info("Successful connection!")
    return conn


def database_insertions(conn: psycopg2.extensions.connection,
                        table_name: str,
                        json_data: List[Dict[str, Any]]) -> bool:
    logging.info(f"Inserting data into '{table_name}' table...")

    cursor = conn.cursor()

    columns = list(json_data[0].keys())
    columns_sql = ",".join(columns)
    insert_statement = f'INSERT INTO {table_name} ({columns_sql}) VALUES %s'

    data_to_insert = []
    for item in json_data:
        row = []
        for column in columns:
            value = item.get(column, None)
            if isinstance(value, dict):
                value = json.dumps(value)
            row.append(value)
        data_to_insert.append(row)

    psycopg2.extras.execute_values(cursor, insert_statement, data_to_insert, page_size=1000)
    conn.commit()

    logging.info(f"All insertions in {table_name} done correctly!")
    cursor.close()

    return True