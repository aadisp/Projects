import pandas
sqrl={
    "Fur Colour":["Gray","Cinnamon","Black"],
    "Count":[]
}
squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
for color in sqrl["Fur Colour"]:
    fr_clr = squirrel_data[squirrel_data["Primary Fur Color"] == color]
    sqrl["Count"].append(len(fr_clr))
    # count = 0
    # for rows in fr_clr["Primary Fur Color"]:
    #     count += 1
    # sqrl["Count"].append(count)
sqrl_count=pandas.DataFrame(sqrl)
sqrl_count.to_csv("squirrel_count.csv")
