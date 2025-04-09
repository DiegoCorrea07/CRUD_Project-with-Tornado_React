class Flight:
    def __init__(self, airline, flight_number, origin, destination, departure_time, arrival_time, id=None):
        self.id = id
        self.airline = airline
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time