import json

f = open(r"D:\New folder\Taxis-and-Rideshare-Apps-1\taxi_zone_lookup.csv", "r")
lines = f.readlines()
taxi_zone_dict = {}

for line in lines:
    line = line.split(',')
    if line[1] not in taxi_zone_dict.keys():
        taxi_zone_dict[line[1]] = []
    taxi_zone_dict[line[1]].append(line[0])

print(taxi_zone_dict)
f2 = open("taxi_zone.json", "w")
json.dump(taxi_zone_dict, f2, indent = 4)

f2.close()