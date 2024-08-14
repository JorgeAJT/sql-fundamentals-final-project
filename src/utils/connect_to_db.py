import os
import psycopg2
from dotenv import load_dotenv
#

def connect_to_db():
    load_dotenv()
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        print("Successful connection")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None