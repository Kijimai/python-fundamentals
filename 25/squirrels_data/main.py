import pandas as pd

# TODO: Get primary fur color using "Primary Fur Color" column

data = pd.read_csv(
    './2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
primary_fur_colors = data["Primary Fur Color"]

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels, red_squirrels, black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

# for data in primary_fur_colors:
#   if data not in data_dict:
#     data_dict[data] = 1
#   else:
#     data_dict[data] += 1

print(data_dict)
fur_colors = pd.DataFrame(data_dict)
print(fur_colors)

fur_colors.to_csv('2018_central_park_squirrel_colors')
