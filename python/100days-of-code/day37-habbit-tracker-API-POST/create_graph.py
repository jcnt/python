import requests

with open("token.txt") as file: 
    TOKEN = file.readline().rstrip()
USER = "jac1nt"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling graph", 
    "unit": "Km", 
    "type": "float", 
    "color": "sora",
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, verify=False)
print(response.text)


