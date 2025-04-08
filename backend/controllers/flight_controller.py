from backend.repositories.flight_repository import FlightRepository
from backend.models.flight import Flight
from backend.views.responses import success_response, error_response

class FlightController:
    def __init__(self):
        self.repo = FlightRepository()

    def get_all(self):
        """Maneja la petición para obtener todos los vuelos."""
        flights = self.repo.get_all()
        return success_response([flight.__dict__ for flight in flights])

    def get_by_id(self, flight_id):
        """Maneja la petición para obtener un vuelo por ID."""
        flight = self.repo.get_by_id(flight_id)
        if flight:
            return success_response(flight.__dict__)
        else:
            return error_response("Flight not found")

    def create(self, flight_data):
        """Maneja la creación de un nuevo vuelo."""
        try:
            flight = Flight(**flight_data)
            self.repo.create(flight)
            return success_response("Flight created successfully")
        except Exception as e:
            return error_response(str(e))

    def update(self, flight_id, flight_data):
        """Maneja la actualización de un vuelo."""
        try:
            flight = Flight(**flight_data)
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
