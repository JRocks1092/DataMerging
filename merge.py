import pandas as pd
import csv

data1= []

with open("bright_stars.csv") as f:
    reader = csv.reader(f)
    for i in reader:
        data1.append(i)

data2= []

with open("dwarf_converted.csv") as f:
    reader = csv.reader(f)
    for i in reader:
        data2.append(i)

header1 = data1[0]
#header2 = data2[0]

stars1 = data1[1:]
stars2 = data2[1:]

starsData = []

for i in stars1:
    starsData.append(i)    
for i in stars2:
    starsData.append(i)

with open("mergedData.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header1)
    writer.writerows(starsData)