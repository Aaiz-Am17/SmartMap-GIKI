# utils/map_utils.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

BUILDING_MAP = {
    "FES": "3J9R+RW7 Faculty of Engineering Sciences, GIKI, Topi, Pakistan",
    "FCSE": "Faculty of Computer Science and Electrical Engineering, GIKI",
    "Mosque": "Student Mosque, GIKI",
    "Faculty of Mechanical Engineering": "Faculty of Mechanical Engineering, GIKI",
    "Faculty of Materials and Chemical Engineering": "Faculty of Materials and Chemical Engineering, GIKI",
    "Academic Block": "Academic Block, GIKI",
    "Agha Hassan Abedi Auditorium": "Agha Hassan Abedi Auditorium, GIKI",
    "Habib Bank Ltd": "Habib Bank Ltd, GIKI",
    "LOGIK": "LOGIK - Landmark of GIK",
    "GIKI Guest House": "GIKI Guest House",
    "Tuc": "34.069686, 72.647110",
    "Library": "Central Library, GIKI",
}

def get_directions_and_steps(origin, destination_raw):
    if API_KEY is None:
        raise ValueError("❌ Google Maps API Key not found in environment.")

    destination = BUILDING_MAP.get(destination_raw.strip().title(), destination_raw + ", GIKI")

    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": "walking",
        "key": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data["status"] != "OK":
            return None, None

        steps = []
        for step in data["routes"][0]["legs"][0]["steps"]:
            instructions = step["html_instructions"]
            clean = instructions.replace("<b>", "").replace("</b>", "").replace('<div style="font-size:0.9em">', " ").replace("</div>", "")
            steps.append(clean)

        maps_url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode=walking"
        return steps, maps_url

    except Exception:
        return None, None
