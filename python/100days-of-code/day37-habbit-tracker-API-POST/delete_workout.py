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

delete_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}/{date}"

delete_config = {

}

response = requests.delete(url=delete_endpoint, headers=headers, verify=False)
print(response.text)

