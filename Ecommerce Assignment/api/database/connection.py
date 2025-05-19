import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_database_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={os.getenv('DB_DRIVER')};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"Trusted_Connection={os.getenv('DB_TRUSTED_CONNECTION')};"
        )
        return conn
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return None
