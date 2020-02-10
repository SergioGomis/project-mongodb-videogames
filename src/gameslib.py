import math
import requests
import os
from dotenv import load_dotenv
load_dotenv()

#libreria aux

def geocode(address):
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }

def coordsFromAddress(address):
    API_KEY = os.getenv("PLACES_API_TOKEN")
    data = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}")
    location = data.json()['results'][0]['geometry']['location']
    return {
        "type":"Point",
        "coordinates":[float(location["lng"]),float(location["lat"])]
    }

def tuplaFromPoint(punto):
    return (punto['coordinates'][1],punto['coordinates'][0])

def gMapsLink(point):
    return f'https://www.google.com/maps/@{point["coordinates"][1]},{point["coordinates"][0]},14z'


def toCartoPoint(lon,lat):
    return f'POINT ({str(lon)} {str(lat)})'


def toGeoJSON(lon,lat):
    return {
        "type":"Point",
        "coordinates":[lon,lat]
    }