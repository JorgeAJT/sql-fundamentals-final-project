import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        data_to_insert = []
        for item in data:
            values = []
            for column in column_order:
                value = item.get(column, None)
                if isinstance(value, dict):
                    value = json.dumps(value)
                elif value is None:
                    value = 'NULL'
                values.append(value)
            data_to_insert.append(values)
    return data