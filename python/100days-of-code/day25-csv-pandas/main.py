#list = []
#
#with open("weather_data.csv") as file: 
#    for i in range(8): 
#        i = file.readline()
#        list.append(i)
#
#
#print(list)


#import csv
#with open("weather_data.csv") as file: 
#    data = csv.reader(file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp": 
#            temperatures.append(int(row[1]))
#    
#    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
temp = data["day"]
print(temp)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

from statistics import mean
print(mean(temp_list))

sm = 0
for i in temp_list: 
    sm += i

print(sm)
print(sm/len(temp_list))

print(sum(temp_list)/len(temp_list))
print(max(temp_list))
print(data["temp"].max())

mxt = 0
for i in temp_list:
    if i > mxt:
        mxt = i
print(mxt)

print(data[data.day == "Monday"])

print(data[data.temp == max(temp_list)])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
ctemp = monday.temp[0]
print(ctemp)
ftemp = ctemp * 1.8 + 32
print(f"Monday's temperature in F is {ftemp}")


data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

table = pandas.DataFrame(data_dict)
print(table)