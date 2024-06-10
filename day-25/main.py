import pandas as pd

#Making Pandas DataFrame
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Squirrel Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pd.DataFrame(data_dict)

print(df)
