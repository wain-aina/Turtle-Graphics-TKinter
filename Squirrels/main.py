import csv
import pandas
import pandas as pd

# # with open("weather_data.csv") as data_list:
# #     data = csv.reader(data_list)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
#
# # print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# # print(avg)
#
# # print(data["temp"].max())
#
# # print(data[data["day"] == "Monday"])
#
# print(data[data["temp"] == data["temp"].max()])

data = pandas.read_csv("squirrel.csv")
gray_count = len(data[data['Primary Fur Color'] == "Gray"])
black_count = len(data[data['Primary Fur Color'] == "Black"])
cinnamon_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
print(gray_count)

d = {
    'Fur Color': ["Gray", "Black", "Cinnamon"],
    'Count': [gray_count, black_count, cinnamon_count]
}

df = pd.DataFrame(data = d)
df.to_csv("colors.csv")
