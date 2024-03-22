import requests

with open("token.txt") as file: 
    TOKEN = file.readline().rstrip()
USER = "jac1nt"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

date = 20240303

update_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}/{date}"

update_config = {
    "quantity": "27",

}

response = requests.put(url=update_endpoint, json=update_config, headers=headers, verify=False)
print(response.text)

