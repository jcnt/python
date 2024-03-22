import requests
from datetime import datetime

MY_LAT = 47.576294
MY_LNG = 19.131772

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
resp_clear = response.json()
sunrise = resp_clear["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = resp_clear["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
# print(f"Sunrise: {sunrise}")
# print(f"Sunset: {sunset}")
