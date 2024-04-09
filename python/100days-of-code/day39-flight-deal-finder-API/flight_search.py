import os
import requests
import datetime

TOKEN = os.environ["KIWI_TOKEN"]
HEADERS = {
    "apikey": TOKEN,
}

dt = datetime.datetime.now()
tomorrow_full = datetime.datetime.now() + datetime.timedelta(days=1)
latest_full = datetime.datetime.now() + datetime.timedelta(days=60)
tomorrow = tomorrow_full.strftime('%d/%m/%Y')
latest = latest_full.strftime('%d/%m/%Y')


class FlightSearch:

    def __init__(self) -> None:
        pass

    def get_iata(self, city): 
#        return "TESTING"

        params = {
            "term": city,
        }

        endpoint = "https://api.tequila.kiwi.com/locations/query"

        data = requests.get(endpoint, headers=HEADERS, params=params, verify=False)
        return data.json()["locations"][0]['code']


    def flight_search(self, destination):

        hit = []

        params = {
            'fly_from': 'BUD',
            'fly_to': destination,
            'date_from': tomorrow,
            'date_to': latest,
            'nights_in_dst_from': 3, 
            "nights_in_dst_to": 5, 
            'curr': "EUR",
#             'price_to': 650,
            'max_stopovers': 2,
            'stopover_to': '6:00',
            'sort': 'price',

        }

        endpoint = 'https://api.tequila.kiwi.com/v2/search'

        data = requests.get(endpoint, headers=HEADERS, params=params, verify=False)
        result = data.json()["data"][0]

        hit.append(result['cityFrom'])
        hit.append(result['cityCodeFrom'])
        hit.append(result['cityTo'])
        hit.append(result['cityCodeTo'])
        hit.append(result['price'])
        if len(result['route']) == 2:
            hit.append(result['route'][0]['local_departure'])
            hit.append(result['route'][1]['local_departure'])
        elif len(result['route']) == 4:
            hit.append(result['route'][0]['local_departure'])
            hit.append(result['route'][2]['local_departure'])
        return hit



