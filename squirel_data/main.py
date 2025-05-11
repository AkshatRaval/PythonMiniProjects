import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnsmon", "Black"],
    "Count": [gray_squirels_count, cinnamon_squirels_count, Black_squirels_count]
}


new_dataframe = pandas.DataFrame(data_dict)
new_dataframe.to_csv("./newData.csv")