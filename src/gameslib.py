import math
import requests


#libreria aux

def geocode(address):
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }


def gMapsLink(point):
    return f'https://www.google.com/maps/@{point["coordinates"][1]},{point["coordinates"][0]},14z'


def toCartoPoint(lon,lat):
    return f'POINT ({str(lon)} {str(lat)})'


def toGeoJSON(lon,lat):
    return {
        "type":"Point",
        "coordinates":[lon,lat]
    }