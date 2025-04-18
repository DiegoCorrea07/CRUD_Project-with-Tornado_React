from backend.db.db_config import get_connection
from backend.models.flight import Flight

class FlightRepository:
    @staticmethod
    def get_all():
        """Obtiene todos los vuelos de la base de datos."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights")
            rows = cursor.fetchall()
            flights = []
            for row in rows:
                id, airline, flight_number, origin, destination, departure_time, arrival_time = row
                flight = Flight(airline, flight_number, origin, destination, departure_time, arrival_time, id)
                flights.append(flight)
            return flights

    @staticmethod
    def get_by_id(flight_id):
        """Obtiene un vuelo por ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights WHERE id = ?", flight_id)
            row = cursor.fetchone()
            if row:
                flight = Flight(*row)
                return flight
            return None

    @staticmethod
    def get_by_flight_number(flight_number):
        """Obtiene un vuelo por número de vuelo."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights WHERE flight_number = ?", flight_number)
            row = cursor.fetchone()
            if row:
                flight = Flight(*row)
                return flight
            return None

    @staticmethod
    def create(flight):
        """Crea un nuevo vuelo."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO flights (airline, flight_number, origin, destination, departure_time, arrival_time)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (flight.airline, flight.flight_number, flight.origin, flight.destination, flight.departure_time, flight.arrival_time))
            conn.commit()

    @staticmethod
    def update(flight_id, flight):
        """Actualiza un vuelo existente."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE flights SET airline=?, flight_number=?, origin=?, destination=?,
                departure_time=?, arrival_time=? WHERE id=?
            """, (flight.airline, flight.flight_number, flight.origin, flight.destination,
                  flight.departure_time, flight.arrival_time, flight_id))
            conn.commit()

    @staticmethod
    def delete(flight_id):
        """Elimina un vuelo de la base de datos."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM flights WHERE id = ?", flight_id)
            conn.commit()