import requests

with open("token.txt") as file: 
    TOKEN = file.readline().rstrip()

USER = "jac1nt"

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes", 
    "notMinor": "yes",
}


response = requests.post(url=pixela_endpoint, json=params, verify=False)
print(response.text)


