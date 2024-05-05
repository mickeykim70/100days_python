import requests
from datetime import datetime

USERNAME = "mickeykim70"
TOKEN = "kd324dqfsdf45er34fgf26lsdfh2df234"


pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}'

today = datetime.now()

exercise_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5",
}

response = requests.post(url=pixel_creation_endpoint, json=exercise_config, headers=headers)

print(response.text)
