# with open("weather_data.csv", mode="r") as file:
#     print(file.readlines())

# import csv
#
# with open("weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
#
# # print(data)
# #
# # print(data["temp"].mean())
# # print(data[data["temp"] == data["temp"].max()])
#
# # data["temp"] = (data["temp"] * 9 / 5) + 32
# data["temp"] = data["temp"].apply(lambda x: (x * 9 / 5) + 32)
# print(data)

import pandas as pd

data = pd.read_csv("squirrel.csv")

squirrel_color = {}

for i in range(len(data)):
    color = data.iloc[i]["Primary Fur Color"]
    if not squirrel_color.get(color):
        squirrel_color[color] = 1
    else:
        squirrel_color[color] += 1


new_data = pd.DataFrame({
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [squirrel_color["Gray"], squirrel_color["Cinnamon"], squirrel_color["Black"]]
})

print(new_data.to_csv("new_data.csv"))
