import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_counts = len(gray_squirrels)
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_counts = len(cinnamon_squirrels)
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_counts = len(black_squirrels)

data_dict = {
    "Fur_color": ["gray", "cinnamon", "black"],
    "count": [gray_squirrels_counts, cinnamon_squirrels_counts, black_squirrels_counts]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirral count.csv")
