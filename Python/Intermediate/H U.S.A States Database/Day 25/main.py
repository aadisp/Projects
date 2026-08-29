# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         temperature.append(row[1])
#     temperature.pop(0)
#     for temp in temperature:
#         temperature[temperature.index(temp)]=int(temp)
# print(temperature)

import pandas

data=pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# data_dict=data.to_dict()
# print(data_dict)
# temp_list=data["temp"].to_list()
# avg_temp=sum(temp_list)/len(temp_list)
# print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"])
# print(data.temp)
# print(data[data.temp==data.temp.max()])
monday=data[data.day=="Monday"]
print(monday.temp[0]*9/5+32)
data_dict={
    "A":[1,2,3,4,5,6],
    "B":[7,8,9,10,11,12]
}
new_data=pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")