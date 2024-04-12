import json

#MICRO

f = open("taxi_rideshare_data.csv", "r")
lines = f.readlines()
taxi_dictionary = {}
general_rideshare_dictionary = {}



for line in lines:
    line = line.split(',')

    line[7] = line[7].replace("\n","")
    current_year = line[0][:4]
    current_month = line[0][5:7]

    if line[1] == "Yellow":
        if current_year not in taxi_dictionary:
            taxi_dictionary[current_year] = dict()
        #print(line[2])
        taxi_dictionary[current_year][current_month] = [("trips per day:",line[2]),
                                                        ("farebox per day:",line[3]),
                                                        ("unique vehicles:",line[4]),
                                                        ("vehicles per day:",line[5]),
                                                        ("avg hrs/day per vehicle:",line[6]),
                                                        ("avg mins/trip:",line[7]),
                                                        ] 

    if line[1] == "FHV - High Volume":
        if current_year not in general_rideshare_dictionary:
            general_rideshare_dictionary[current_year] = dict()
        general_rideshare_dictionary[current_year][current_month] = [("trips per day:",line[2]),
                                                        ("farebox per day:",line[3]),
                                                        ("unique vehicles:",line[4]),
                                                        ("vehicles per day:",line[5]),
                                                        ("avg hrs/day per vehicle:",line[6]),
                                                        ("avg mins/trip:",line[7]),
                                                        ] 

#Save the json object to a file
f2 = open("taxi_data.json", "w")
json.dump(taxi_dictionary, f2, indent = 4)

f2.close()

f3 = open("general_rideshare_data.json", "w")
json.dump(general_rideshare_dictionary, f3, indent = 4)

f3.close()