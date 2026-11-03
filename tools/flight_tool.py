
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def search_flights(query):
    if not API_KEY:
        return "Error: AviationStack API key is missing."

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()

        data = response.json()

        # Check API errors
        if "error" in data:
            return f"AviationStack API Error: {data['error']}"

        flights = []

        for flight in data.get("data", [])[:5]:
            airline = flight.get("airline", {}).get("name", "Unknown")
            departure = flight.get("departure", {}).get("airport", "Unknown")
            arrival = flight.get("arrival", {}).get("airport", "Unknown")
            status = flight.get("flight_status", "Unknown")

            flights.append(
                f"""
Airline: {airline}
Departure: {departure}
Arrival: {arrival}
Status: {status}
"""
            )

        if not flights:
            return "API connected, but no flight records were returned."

        return "\n".join(flights)

    except requests.exceptions.RequestException as e:
        return f"Flight API connection error: {str(e)}"
