import datetime

def flight_to_dict(flight):
    """Convierte un objeto Flight a un diccionario serializable en JSON."""
    return {
        "id": flight.id,
        "airline": flight.airline,
        "flight_number": flight.flight_number,
        "origin": flight.origin,
        "destination": flight.destination,
        "departure_time": flight.departure_time.isoformat() if isinstance(flight.departure_time, datetime.datetime) else str(flight.departure_time) if flight.departure_time else None,
        "arrival_time": flight.arrival_time.isoformat() if isinstance(flight.arrival_time, datetime.datetime) else str(flight.arrival_time) if flight.arrival_time else None
    }