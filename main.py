import os
import argparse
from src import run_database_insertions

DATA_PATH = os.getenv("DATA_PATH", "./data")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

parser = argparse.ArgumentParser()
parser.add_argument('--insert', type=str, help='Relative path from DATA_PATH to JSON file '
                                               '(e.g., meter_data.json)')
parser.add_argument('--fetch', type=str, help='Query SQl to fetch data')
parser.add_argument('--table', type=str, help='Name of the table')
parser.add_argument('--outfile', type=str, help='Name of the JSON file where to save it')
parser.add_argument('--insert_all', action='store_true', help='Insert all known files into '
                                                              'their corresponding tables')

args = parser.parse_args()

if __name__ == "__main__":
    run_database_insertions(args, DATA_PATH, ENVIRONMENT)
