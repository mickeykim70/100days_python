import requests
import datetime as dt
import json

MY_LAT = 37.263573
MY_LONG = 127.028603


def is_iss_on_my_head():
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss['iss_position']['latitude'])
    iss_longitude = float(data_iss['iss_position']['longitude'])

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True


# ------ CURRENT SUNRISE ------ #
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = dt.datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True

if is_iss_on_my_head() and is_night():
    print('It\'s on my head')
