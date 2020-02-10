import math
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()



def numSchoolsFromCoords(tupla):
    tipositio='primary_school'
    radio='1000'
    API_KEY = os.getenv("PLACES_API_TOKEN")
    URL = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={tupla[0]},{tupla[1]}&type={tipositio}&radius={radio}&key={API_KEY}'
    response_data = requests.get(URL)
    json_data = json.loads(response_data.text)
    return len(json_data['results'])

def numStarbucksFromCoords(tupla):
    tipositio='cafe'
    clave='Starbucks'
    radio='1000'
    API_KEY = os.getenv("PLACES_API_TOKEN")
    URL = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={tupla[0]},{tupla[1]}&type={tipositio}&keyword={clave}&radius={radio}&key={API_KEY}'
    response_data = requests.get(URL)
    json_data = json.loads(response_data.text)
    return len(json_data['results'])

def numAirportsFromCoords(tupla):
    tipositio='airport'
    radio='15000'
    API_KEY = os.getenv("PLACES_API_TOKEN")
    URL = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={tupla[0]},{tupla[1]}&type={tipositio}&radius={radio}&key={API_KEY}'
    print(URL)
    response_data = requests.get(URL)
    json_data = json.loads(response_data.text)
    return len(json_data['results'])


# From Response/JSON to dict:
# data_dict = json.loads(response_data.text)
# From dict to json:
# y = json.dumps(data_dict)