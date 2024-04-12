import json

f = open("lyft_uber_data.csv", "r")
lines = f.readlines()
dictionary = {}

for line in lines:
    line = line.split(',')

    # line[4] = line[4].replace("\n","")
    if line[0] == "UBER":
        dictionary["UBER"] = [line[1],line[2],line[3],line[4]]

print(lines)

#Save the json object to a file
f2 = open("lyft_uber_data.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()