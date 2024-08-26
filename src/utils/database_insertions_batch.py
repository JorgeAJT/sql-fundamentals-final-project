import json
from psycopg2.extras import execute_batch

def database_insertions_batch(conn, table_name, json_data):
    cursor = conn.cursor()

    columns = list(json_data[0].keys())
    columns_sql = ",".join(columns)
    insert_statement = f'INSERT INTO {table_name} ({columns_sql}) VALUES ({",".join(["%s"] * len(columns))})'

    data_to_insert = []
    for item in json_data:
        row = []
        for column in columns:
            value = item.get(column, None)
            if isinstance(value, dict):
                value = json.dumps(value)
            row.append(value)
        data_to_insert.append(row)

    execute_batch(cursor, insert_statement, data_to_insert)
    print("Insertion done correctly!")
    conn.commit()
    cursor.close()