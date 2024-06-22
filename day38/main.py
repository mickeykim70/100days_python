import requests
import json

GENDER = 'MALE'
WEIGHT_KG = '63'
HEIGHT_CM = '168'
AGE = '54'
APP_ID = 'd63cfc61'
# APP_ID = '9fa3007f'
API_KEY = '677a4762bf79196ed9cc234d7b6cf412'
# API_KEY = 'c00ce89c396f38d2c0ce44add9849537'
# USERNAME = 'guessagain@naver.com'
production_endpoint = 'https://api.syndigo.com'
UAT_endpoint = 'https://api.uat.syndigo.com'
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input('Enter your exercise: ')

headers = {
    'x-api-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)




