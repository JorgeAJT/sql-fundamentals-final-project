

def insert_into_db(conn, table_name, json_data, column_order):
    try:
        cursor = conn.cursor()