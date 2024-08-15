from src.utils import connect_to_db, read_json_file

def database_insertions():
    print("Connecting with the db ...")
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return None
    testing_data_list = read_json_file('./data/testing.json')
    print(testing_data_list)
    return testing_data_list