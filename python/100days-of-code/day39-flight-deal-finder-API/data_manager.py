from os import environ
import requests

class DataManager:

    def __init__(self) -> None:
        
        SHEET = environ["PRICE_SHEET"]
        TOKEN = environ["PRICE_TOKEN"]
        
        endpoint = f"https://api.sheety.co/{SHEET}/flightDeals/prices"

        headers = {
            "Authorization": f"Bearer {TOKEN}"
        }

        response = requests.get(endpoint, headers=headers, verify=False)
        result = response.json()

