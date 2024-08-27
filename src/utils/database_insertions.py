import json
from psycopg2.extras import execute_values

def database_insertions(conn, table_name, json_data):
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

    execute_values(cursor, insert_statement, data_to_insert, page_size=1000)
    conn.commit()

    print(f"All insertion in {table_name} done correctly!")
    cursor.close()