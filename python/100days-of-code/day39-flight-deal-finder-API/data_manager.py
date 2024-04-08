from os import environ
import requests

SHEET = environ["PRICE_SHEET"]
TOKEN = environ["PRICE_TOKEN"]
HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

class DataManager:

    def __init__(self):
        pass
        
    def get_reqs(self): 

        endpoint = f"https://api.sheety.co/{SHEET}/flightDeals/prices"

        response = requests.get(endpoint, headers=HEADERS, verify=False)
        result = response.json()

        return result

    def update_iata(self, iata, objid): 

        print(objid, iata)

        body = {
            "price": {
                'iataCode': iata,
            }
        }
        
        endpoint = f"https://api.sheety.co/{SHEET}/flightDeals/prices/{objid}"

        response = requests.put(endpoint, headers=HEADERS, json=body, verify=False)
        response_sheet = response.json()
        print("update done")
        
