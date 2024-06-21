import requests

# API_KEY = '6c392caaec6bbdf7bee6b0415362271e'
# lat = '37.5665'
# lon = '126.9776'
# https://api.openweathermap.org/data/2.5/weather?q=&appid=6c392caaec6bbdf7bee6b0415362271e
#
parameters = {
    q : "London,UK",
    appid :'6c392caaec6bbdf7bee6b0415362271e'
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?", params=parameters)
print(response.json())
