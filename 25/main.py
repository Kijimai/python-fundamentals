import csv
import pandas as pd

# with open('./weather_data.csv', mode="r") as file:
#     data = file.readlines()
#     print(data)

# with open('./weather_data.csv') as data_file:
#     data = list(csv.reader(data_file))
#     temperatures = []
#     for row in data[1:]:
#       temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv('./weather_data.csv')
# print(data["day"])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)


# builtin python method
average = sum(temp_list) / len(temp_list)
# print(average)

# Referring to a series, rather than the list
# print(data["temp"].max())

# Getting data in the rows of the DataFrame
monday_row = data[data["day"] == "Monday"]
# print(monday_row)

# Getting the row of data that contains the maximum temp data for the week
# max_temp_weather_row = data[data["temp"] == data["temp"].max()]
# print(max_temp_weather_row)

# monday_temp_fahrenheit


def convert_to_fahrenheit(c):
    return ((9/5)*c) + 32


mon_temp_fahrenheit = convert_to_fahrenheit(int(monday_row.temp))
print(mon_temp_fahrenheit)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "Jamie", "Lamie"],
    "scores": [75, 55, 50]
}

new_df = pd.DataFrame(data_dict)
print(new_df)

#convert the newly created DataFrame to a csv file
new_csv = new_df.to_csv('new_data_csv')