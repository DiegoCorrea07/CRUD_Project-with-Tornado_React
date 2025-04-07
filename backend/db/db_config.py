import pyodbc

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DIEGOC\\SQLEXPRESS02;"
        "DATABASE=FlightDB;"
        "Trusted_Connection=yes;"
    )
