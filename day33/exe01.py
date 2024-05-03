import smtplib

import requests
from datetime import datetime

MY_LAT = 37.29111
MY_LONG = 127.00889

def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])


    #Check (iss_position and your_position) within +/-5 degrees
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5<= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }

    response_sunset = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters,)
    response_sunset.raise_for_status()

    data_sunset = response_sunset.json()
    sunrise = int(data_sunset['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data_sunset['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#Send me an email
if issubclass() and is_iss_overhead():
    pass

