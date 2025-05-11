import csv
import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temperature"])
