import requests

with open("token.txt") as file: 
    APIKEY=file.readline().rstrip()

params = {
    "lat": 59.913868,
    "lon": 10.752245,
    "appid": APIKEY,
    "cnt": 4,
}


result = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params, verify=False)
weather = result.json()

rainy = False

for i in weather["list"]:
    if i["weather"][0]["id"] < 700:
#    if weather["list"][i]["weather"][0]["id"] < 700:
        rainy = True

if rainy: 
    print("bring your umbrella, going to be raining!")
else: 
    print("no worries, gonna be sunny!")

