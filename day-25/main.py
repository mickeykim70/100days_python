# with open("weather_data.csv", mode="r") as file:
#     weather_data = file.readlines()
#     weathers = []
#     for weather in weather_data:
#         weathers.append(weather.split(","))
# print(weathers[0])

# import csv
#
# with open("weather_data.csv") as datafile:
#     data = csv.reader(datafile)
#
#     temperatures = []
#     for datum in data:
#         if datum[1] != "temp":
#             temperatures.append(int(datum[1]))
#
#     print(temperatures)

import pandas as pd

weather = pd.read_csv("weather_data.csv")
print(weather)
print(weather["temp"])





