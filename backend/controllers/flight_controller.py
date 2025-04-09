from backend.repositories.flight_repository import FlightRepository
from backend.models.flight import Flight
from backend.utils.serializers import flight_to_dict
from backend.views.responses import success_response, error_response
from backend.utils.datetime_utils import parse_datetime_local

class FlightController:
    def __init__(self):
        self.repo = FlightRepository()

    def get_all(self):
        """Maneja la petición para obtener todos los vuelos."""
        flights = FlightRepository.get_all()
        return success_response([flight_to_dict(flight) for flight in flights])

    def get_by_id(self, flight_id):
        """Maneja la petición para obtener un vuelo por ID."""
        flight = self.repo.get_by_id(flight_id)
        if flight:
            return success_response(flight_to_dict(flight))
        else:
            return error_response("Flight not found")

    def create(self, flight_data):
        """Maneja la creación de un nuevo vuelo."""
        try:
            # Verificar si ya existe un vuelo con el mismo número de vuelo
            existing_flight = self.repo.get_by_flight_number(
                flight_data.get('flight_number')
            )
            if existing_flight:
                return error_response("A flight with this flight number already exists.")

            # Parsear las fechas y crea el vuelo
            departure_time = parse_datetime_local(flight_data.get('departure_time'))
            arrival_time = parse_datetime_local(flight_data.get('arrival_time'))
            flight = Flight(
                flight_data.get('airline'),
                flight_data.get('flight_number'),
                flight_data.get('origin'),
                flight_data.get('destination'),
                departure_time,
                arrival_time
            )
            self.repo.create(flight)
            return success_response("Flight created successfully")
        except Exception as e:
            return error_response(str(e))

    def update(self, flight_id, flight_data):
        """Maneja la actualización de un vuelo."""
        try:
            departure_time = parse_datetime_local(flight_data.get('departure_time'))
            arrival_time = parse_datetime_local(flight_data.get('arrival_time'))
            flight = Flight(
                flight_data.get('airline'),
                flight_data.get('flight_number'),
                flight_data.get('origin'),
                flight_data.get('destination'),
                departure_time,
                arrival_time
            )
            self.repo.update(flight_id, flight)
            return success_response("Flight updated successfully")
        except Exception as e:
            return error_response(str(e))

    def delete(self, flight_id):
        """Maneja la eliminación de un vuelo."""
        try:
            self.repo.delete(flight_id)
            return success_response("Flight deleted successfully")
        except Exception as e:
            return error_response(str(e))