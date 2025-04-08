import pyodbc

def get_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DIEGOC\\SQLEXPRESS02;"
        "DATABASE=FlightDB;"
        "Trusted_Connection=yes;"
    )
    create_table_if_not_exists(connection)
    return connection

def create_table_if_not_exists(connection):
    """Crea la tabla 'flights' si no existe."""
    create_table_query = """
    IF NOT EXISTS (
        SELECT * FROM sysobjects WHERE name='flights' AND xtype='U'
    )
    CREATE TABLE flights (
        id INT PRIMARY KEY IDENTITY(1,1),
        airline NVARCHAR(100) NOT NULL,
        flight_number NVARCHAR(50) NOT NULL,
        origin NVARCHAR(100) NOT NULL,
        destination NVARCHAR(100) NOT NULL,
        departure_time DATETIME NOT NULL,
        arrival_time DATETIME NOT NULL
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
        connection.commit()
