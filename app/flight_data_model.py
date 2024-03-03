# app/flight_data_model.py
class Flight:
    def __init__(self, source_city, destination_city, flight_number, airline_name, departure_date, departure_time, arrival_time, duration, num_of_stops, price):
        self.source_city = source_city
        self.destination_city = destination_city
        self.flight_number = flight_number
        self.airline_name = airline_name
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.duration = duration
        self.num_of_stops = num_of_stops
        self.price = price
