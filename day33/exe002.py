import requests
from datetime import datetime

MY_LAT = 37.29111
MY_LONG = 127.00889

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters,)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise)
print(sunset)

