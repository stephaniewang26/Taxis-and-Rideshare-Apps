import json

#MICRO

f = open(r"D:\New folder\Taxis-and-Rideshare-Apps-1\data\tripsperday_taxi_rideshare\taxi_rideshare_data.csv", "r")
lines = f.readlines()
taxi_dictionary = {}
general_rideshare_dictionary = {}



for line in lines:
    line = line.split(',')

    line[7] = line[7].replace("\n","")
    current_year = line[0][:4]
    if (line[0][5:7])[0] != "0":
        current_month = line[0][5:7]
    else:
        current_month = line[0][6:7]
    if current_month != "/Y":
        current_month = int(current_month)
    print(type(current_month))

    if line[1] == "Yellow":
        if current_year not in taxi_dictionary:
            taxi_dictionary[current_year] = dict()
            taxi_dictionary[current_year][current_month] = dict()
        elif current_month not in taxi_dictionary[current_year]:
            taxi_dictionary[current_year][current_month] = dict()
        #print(line[2])
        taxi_dictionary[current_year][current_month]["trips per day"] = line[2]
        taxi_dictionary[current_year][current_month]["farebox per day"] = line[3]
        taxi_dictionary[current_year][current_month]["unique vehicles"] = line[4]
        taxi_dictionary[current_year][current_month]["vehicles per day"] = line[5]
        taxi_dictionary[current_year][current_month]["avg hrs per day per vehicle"] = line[6]
        taxi_dictionary[current_year][current_month]["avg mins per trip"] = line[7]

    if line[1] == "FHV - High Volume":
        if current_year not in general_rideshare_dictionary:
            general_rideshare_dictionary[current_year] = dict()
            general_rideshare_dictionary[current_year][current_month] = dict()
        elif current_month not in general_rideshare_dictionary[current_year]:
            general_rideshare_dictionary[current_year][current_month] = dict()
        general_rideshare_dictionary[current_year][current_month]["trips per day"] = line[2]
        general_rideshare_dictionary[current_year][current_month]["farebox per day"] = line[3]
        general_rideshare_dictionary[current_year][current_month]["unique vehicles"] = line[4]
        general_rideshare_dictionary[current_year][current_month]["vehicles per day"] = line[5]
        general_rideshare_dictionary[current_year][current_month]["avg hrs per day per vehicle"] = line[6]
        general_rideshare_dictionary[current_year][current_month]["avg mins per trip"] = line[7]

#Save the json object to a file
f2 = open("taxi_data.json", "w")
json.dump(taxi_dictionary, f2, indent = 4)

f2.close()

f3 = open("general_rideshare_data.json", "w")
json.dump(general_rideshare_dictionary, f3, indent = 4)

f3.close()