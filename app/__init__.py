# app/__init__.py
from flask import Flask
from .flight_data_model import Flight

app = Flask(__name__)

# Dummy data
app.flights_data = [
    Flight("Dehradun", "New Delhi", "A123", "AirIndia", "2024-03-03", "1000 Hrs", "1300 Hrs", "2 hours", 1, 200.0),
    Flight("New Delhi", "Dehradun", "SP223", "Spice Jet", "2024-03-21", "1500 Hrs", "1700 Hrs", "2 hours", 1, 200.0)
    # Add more Flight instances as needed
]

from app import routes
