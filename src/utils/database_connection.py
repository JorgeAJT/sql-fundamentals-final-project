import os
import psycopg2
from dotenv import load_dotenv

def database_connection():
    load_dotenv()
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    print("Successful connection!")
    return conn