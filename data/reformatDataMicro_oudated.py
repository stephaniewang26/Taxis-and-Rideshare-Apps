import json

#MICRO

f = open("lyft_uber_data.csv", "r")
lines = f.readlines()
uber_dictionary = {}
lyft_dictionary = {}

for line in lines:
    line = line.split(',')

    line[4] = line[4].replace("\n","")
    if line[0] == "UBER":
        if line[1] not in uber_dictionary:
            uber_dictionary[line[1]] = dict()
        uber_dictionary[line[1]][line[2]] = [("total dispatched trips:",line[3]),("unique dispatched vehicles:",line[4])] 

    if line[0] == "LYFT":
        if line[1] not in lyft_dictionary:
            lyft_dictionary[line[1]] = dict()
        lyft_dictionary[line[1]][line[2]] = [("total dispatched trips:",line[3]),("unique dispatched vehicles:",line[4])] 

#Save the json object to a file
f2 = open("uber_data.json", "w")
json.dump(uber_dictionary, f2, indent = 4)

f2.close()

f3 = open("lyft_data.json", "w")
json.dump(lyft_dictionary, f3, indent = 4)

f3.close()