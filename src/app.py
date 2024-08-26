from src.utils import database_connection, read_json_file, database_insertions, database_insertions_batch

def run_database_insertions():
    try:
        print("Connecting with the db ...")
        conn = database_connection()
        testing_data_list = read_json_file('./data/testing.json')
        database_insertions(conn, 'testing_table', testing_data_list)

    except Exception as e:
        print(f"Error: {e}")
        raise e