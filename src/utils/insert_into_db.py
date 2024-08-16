import json
from psycopg2.extras import execute_values

def insert_into_db(conn, table_name, json_data, column_order):
    try:
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = '{table_name}' 
            AND column_default IS NULL
            AND is_identity = 'NO'
        """)
        table_columns = [row[0] for row in cursor.fetchall()]

        missing_columns = []
        for col in table_columns:
            if col not in column_order:
                missing_columns.append(col)

        if missing_columns:
            print(f"Error: Missing mandatory column(s) in column_order: {missing_columns}")
            return None

        columns = ",".join(column_order)
        insert_statement = f'INSERT INTO {table_name} ({columns}) VALUES %s'

        data_to_insert = []
        for item in json_data:
            values = []
            for column in column_order:
                value = item.get(column, None)
                if isinstance(value, dict):
                    value = json.dumps(value)
                elif value is None:
                    value = 'NULL'
                values.append(value)
            data_to_insert.append(values)

        print(f"Insert statement: {insert_statement}")
        print(f"Data to insert: {data_to_insert}")

        execute_values(cursor, insert_statement, data_to_insert)
        print("Insertion done correctly!")

    except Exception as e:
        print(f"Error inserting datas into the database: {e}")
        return None

    finally:
        conn.commit()
        cursor.close()