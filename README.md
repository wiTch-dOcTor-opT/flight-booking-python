# Flight Booking System

This project was created using python 3.9 and Flask for Altimetrik.

## Project Info

This is a flight booking system. Here we have a search bar with items like source, destination, travel date and return date.

In here we have an single api endpoint "/search_flights" that is running on localhost. 
You need to provide it with data like source, destination, travel date and return date and it returns you a json output as shown below.

```json
    {
    "arrival": {
        "results": [
            {
                "airline_name": "Spice Jet",
                "arrival_time": "1700 Hrs",
                "departure_date": "2024-03-21",
                "departure_time": "1500 Hrs",
                "destination_city": "New Delhi",
                "duration": "2 hours",
                "flight_number": "SP223",
                "num_of_stops": 1,
                "price": 200.0,
                "source_city": "Dehradun"
            }
        ],
        "total_results": 1
    },
    "departure": {
        "results": [
            {
                "airline_name": "AirIndia",
                "arrival_time": "1300 Hrs",
                "departure_date": "2024-03-03",
                "departure_time": "1000 Hrs",
                "destination_city": "New Delhi",
                "duration": "2 hours",
                "flight_number": "A123",
                "num_of_stops": 1,
                "price": 200.0,
                "source_city": "Dehradun"
            }
        ],
        "total_results": 1
    }
}
```

## How to run the project

You will need to have python 3.9 and pip installed in your system for it to work.

In the project directory, you can do:

### `pip install requirements.txt`

It will install all the dependencies for the project.

Now to run the project do:

### `python run.py`
