import json
from psycopg2.extras import RealDictCursor

def fetch_data_as_json(conn, query, filename):
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
