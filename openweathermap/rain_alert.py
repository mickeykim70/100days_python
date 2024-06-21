import requests

#https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=6c392caaec6bbdf7bee6b0415362271e

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
OWM_Endpoint1 = 'http://api.openweathermap.org/data/2.5/forecast'
api_key = "6c392caaec6bbdf7bee6b0415362271e"
weather_params = {
    "lat": 37.263573,
    "lon": 127.028603,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['list'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Rain")

# print(weather_data["list"][0]["weather"])
