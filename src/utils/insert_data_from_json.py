from .read_json_file import read_json_file
from .database_insertions import database_insertions

def insert_data_from_json(filepath, conn, table_name):
    data_list = read_json_file(filepath)
    database_insertions(conn, table_name, data_list)

    return True
