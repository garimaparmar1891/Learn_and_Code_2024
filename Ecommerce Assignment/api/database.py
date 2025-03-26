import pyodbc

def get_database_connection():
    try:
        return pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=ITT-GARIMA-P\\SQLEXPRESS;"
            "DATABASE=EcomDB;"
            "Trusted_Connection=yes;"
        )
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return None
