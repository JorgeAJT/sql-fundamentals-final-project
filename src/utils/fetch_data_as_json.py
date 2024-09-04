import json
from psycopg2.extras import RealDictCursor

def fetch_data_as_json(conn, query, filename):
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(query)

    rows = cursor.fetchmany(2)

    data = [dict(row) for row in rows]

    print(data)

    file_path = f'./data/{filename}'

    with open(file_path, 'x') as json_file:
        json.dump(data, json_file, indent=4)

    print("File created and data written correctly")
