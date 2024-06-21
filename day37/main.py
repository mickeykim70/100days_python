import requests
from datetime import datetime

USER_NAME = 'pixla-test101'
TOKEN = 'lsker1343sdk'
GRAPH_ID = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


# /v1/users/<username>/graphs/<graphID>
record_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'
today = datetime.now()

record_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '2',
}

record = requests.post(url=record_endpoint, json=record_config, headers=headers)
print(record.text)


# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

new_pixla_data = {
    'quantity': '12',
}

requests.put(url=update_endpoint, json=new_pixla_data, headers=headers)

delete_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

delete = requests.delete(url=update_endpoint, headers=headers)

print(delete.text)
