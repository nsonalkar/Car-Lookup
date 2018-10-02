
import csv
import requests,json
import numpy as np
import pandas as pd
#from json import load
from urllib.request import urlopen
import math



file = open("vin.csv", "r")
next(file)
vin = file.read().splitlines()

data = [["Vin Number", "Make", "Model", "Model Year", "Engine Cylinders", "Transmission Style", "Trim"]]
checkedVin = []
for x in vin:
    if x not in checkedVin:
        data2 = []
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/' + x + '?format=json'
        response = urlopen(url).read()
        result2 = json.loads(response)
        data2.append(x)
        if result2['Results'][0]['Make'] == "":
            result2['Results'][0]['Make'] = "N/A"
            data2.append(result2['Results'][0]['Make'])
        else:
            data2.append(result2['Results'][0]['Make'])
        if result2['Results'][0]['Model'] == "":
            result2['Results'][0]['Model'] = "N/A"
            data2.append(result2['Results'][0]['Model'])
        else:
            data2.append(result2['Results'][0]['Model'])
        if result2['Results'][0]['ModelYear'] == "":
            result2['Results'][0]['ModelYear'] = "N/A"
            data2.append(result2['Results'][0]['ModelYear'])
        else:
            data2.append(result2['Results'][0]['ModelYear'])
        if result2['Results'][0]['EngineCylinders'] == "":
            result2['Results'][0]['EngineCylinders'] = "N/A"
            data2.append(result2['Results'][0]['EngineCylinders'])
        else:
            data2.append(result2['Results'][0]['EngineCylinders'])
        if result2['Results'][0]['TransmissionStyle'] == "":
            result2['Results'][0]['TransmissionStyle'] = "N/A"
            data2.append(result2['Results'][0]['TransmissionStyle'])
        else:
            data2.append(result2['Results'][0]['TransmissionStyle'])
        if result2['Results'][0]['Trim'] == "":
            result2['Results'][0]['Trim'] = "N/A"
            data2.append(result2['Results'][0]['Trim'])
        else:
            data2.append(result2['Results'][0]['Trim'])
        data.append(data2)
        checkedVin.append(x)
        #print("\n")
print(data)
data3 = {"hello": data}
print(data3)
print(checkedVin)

file2 = open("carInfo.csv", "w")
with file2:
    writer = csv.writer(file2)
    writer.writerows(data)



# print("a", vin)
# #print(vin[0])
# df = pd.read_csv('vin.csv')
# print(df)
# reader = csv.DictReader(open('vin.csv', 'r'))
# for line in reader:
#     print(line)
# dict = pd.read_csv("vin.csv").to_dict()
# print(dict)
# url = 'https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/'
# r = requests.get(url, params=dict)
# print()
#r = requests.get(url, params=vin)
#print(r)