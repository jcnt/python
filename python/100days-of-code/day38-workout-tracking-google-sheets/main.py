import requests
from datetime import datetime
from os import environ

GENDER = "male"
WEIGHT = 75
HEIGHT = 180
AGE = 47

dt = datetime.now()
date = dt.strftime("%d/%m/%Y")
time = dt.strftime("%X")

APP_ID = environ["APP_ID"]
API_TOKEN = environ["API_TOKEN"]

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("Tell me what exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_TOKEN,
}

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

resp_nutr = requests.post(endpoint, json=parameters, headers=headers, verify=False)
result = resp_nutr.json()

user_exer = result["exercises"][0]['user_input']
user_duration = result["exercises"][0]['duration_min']
calories = result["exercises"][0]['nf_calories']

SHEETID = environ["SHEETID"]

sheet_endpoint = f"https://api.sheety.co/{SHEETID}/myWorkoutPython/workouts"

body = {
    "workout": {
        "date": date,
        "time": time, 
        "exercise": user_exer,
        "duration": user_duration, 
        "calories": calories,
    }
}

SHEETTOKEN = environ["SHEETTOKEN"]

headers = {
    "Authorization": f"Bearer {SHEETTOKEN}"
}


resp_sheet = requests.post(sheet_endpoint, headers=headers, json=body, verify=False)
result_sheet = resp_sheet.json()
print(result_sheet)

