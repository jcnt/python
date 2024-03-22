import requests
from datetime import datetime

with open("token.txt") as file: 
    TOKEN = file.readline().rstrip()
USER = "jac1nt"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

rec_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}"

date = datetime.now().strftime("%Y%m%d")

rec_config = {
    "date": date,
    "quantity": input("How many kilometers did you cycle today? ")

}

response = requests.post(url=rec_endpoint, json=rec_config, headers=headers, verify=False)
print(response.text)


