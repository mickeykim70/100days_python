import requests

# HOST = "https://trackapi.nutritionix.com"
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "16ae977d"
API_KEY = '970ac330489b726350be3db40c595117'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

params = {
    "query": "Tell me which exercise you did: ",
    'gender': "MALE",
    "weight_kg": "70",
    "height_cm": "168",
    "age": "50",
}

response = requests.post(endpoint, json=params, headers=headers)

result = response.json()
print(result)