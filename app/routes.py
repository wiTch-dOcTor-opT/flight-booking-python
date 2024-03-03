from flask import request, jsonify
from . import app


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response


@app.route('/search_flights', methods=['POST'])
def search_flights():
    search_query = request.get_json()

    required_fields = ['source', 'destination', 'travel_date']
    for field in required_fields:
        if field not in search_query:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    departure_results = []
    arrival_results = []

    for flight in app.flights_data:
        if (
            flight.source_city == search_query['source']
            and flight.destination_city == search_query['destination']
            and flight.departure_date == search_query['travel_date']
        ):
            departure_results.append(flight.__dict__)

        if 'return_date' in search_query and (
            (flight.source_city == search_query['destination']
             and flight.destination_city == search_query['source']
             and flight.departure_date == search_query['return_date'])
        ):
            arrival_results.append(flight.__dict__)

    return jsonify({
        "departure": {"results": departure_results, "total_results": len(departure_results)},
        "arrival": {"results": arrival_results, "total_results": len(arrival_results)}
    })