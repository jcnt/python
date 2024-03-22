import requests
from datetime import datetime
from time import sleep

MY_LAT = -34.576294
MY_LONG = -30.131772

iss_resp = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_resp.raise_for_status()
data = iss_resp.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

sun_resp = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_resp.raise_for_status()
data = sun_resp.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = str(datetime.now())
hour_now = int(time_now.split(" ")[1].split(":")[0])

is_running = True

print(MY_LAT)
print(MY_LONG)
print(iss_latitude)
print(iss_longitude)

while is_running: 
#If the ISS is close to my current position
    if abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5:
#ANG:    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
# and it is currently dark
        if hour_now > sunset or hour_now < sunrise: 
# Then send me an email to tell me to look up.
            print("sending an email to notify")
        else:
            print("it's not dark")
    else: 
        print("not close enough")
# BONUS: run the code every 60 seconds.
    sleep(60)    



