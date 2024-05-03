
from flask import Flask
from flask import request
from flask import render_template
import json

#test

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/tripsperday_taxi_rideshare/general_rideshare_data.json")
    gen_rideshare_data = json.load(f)
    f.close()
    requested_year = request.args.get('year')
    all_years = sorted(list(gen_rideshare_data.keys()))
    return render_template('about.html',year=requested_year, all_years=all_years)

@app.route('/macro')
def macro():
    f = open("data/tripsperday_taxi_rideshare/general_rideshare_data.json")
    gen_rideshare_data = json.load(f)
    f.close()

    f = open("data/tripsperday_taxi_rideshare/taxi_data.json")
    taxi_data = json.load(f)
    f.close()

    gen_rideshare_data = dict(reversed(gen_rideshare_data.items()))
    taxi_data = dict(reversed(taxi_data.items()))

    requested_year = request.args.get('year')
    all_years = sorted(list(gen_rideshare_data.keys()))
    tripsbyk = ["800,000","700,000","600,000","500,000","400,000","300,000","200,000","100,000","0"]

    taxi_line_endpoints =[]
    connect_x = None
    for year in taxi_data:
        taxi_data[year] = dict(reversed(taxi_data[year].items()))
        for month in taxi_data[year]:
            if month == "1" and connect_x != None:
                stop_x = taxi_data[year][month]["trips per day"]
                taxi_line_endpoints.append([float(connect_x),float(stop_x)])

                start_x = taxi_data[year][month]["trips per day"]
                stop_x = taxi_data[year][str(int(month)+1)]["trips per day"]
                taxi_line_endpoints.append([float(start_x),float(stop_x)])
            elif month == "12":
                connect_x = taxi_data[year][month]["trips per day"]
            else:
                start_x = taxi_data[year][month]["trips per day"]
                stop_x = taxi_data[year][str(int(month)+1)]["trips per day"]
                taxi_line_endpoints.append([float(start_x),float(stop_x)])
    
    print(taxi_line_endpoints)
    
    rideshare_endpoints =[]
    connect_x = None
    for year in gen_rideshare_data:
        gen_rideshare_data[year] = dict(reversed(gen_rideshare_data[year].items()))
        for month in gen_rideshare_data[year]:
            if month == "1" and connect_x != None:
                stop_x = gen_rideshare_data[year][month]["trips per day"]
                rideshare_endpoints.append([float(connect_x),float(stop_x)])

                start_x = gen_rideshare_data[year][month]["trips per day"]
                stop_x = gen_rideshare_data[year][str(int(month)+1)]["trips per day"]
                rideshare_endpoints.append([float(start_x),float(stop_x)])
            elif month == "12":
                connect_x = gen_rideshare_data[year][month]["trips per day"]
            else:
                start_x = gen_rideshare_data[year][month]["trips per day"]
                stop_x = gen_rideshare_data[year][str(int(month)+1)]["trips per day"]
                rideshare_endpoints.append([float(start_x),float(stop_x)])

    # for i in range(len(all_years)-1): # make it easy to dynamically generate a line graph
    #     start_y = all_years[i] #generate endpoints for each line segment
    #     stop_y = all_years[i+1]

    #     taxi_line_endpoints.append([taxi_trip_values[start_y],taxi_trip_values[stop_y]])
    return render_template('macro.html',year=requested_year, all_years=all_years, trips_increment = tripsbyk, taxiendpoints = taxi_line_endpoints, rideshareendpoints = rideshare_endpoints)

@app.route('/micro')
def micro():
    f = open("data/tripsperday_taxi_rideshare/general_rideshare_data.json")
    gen_rideshare_data = json.load(f)
    f.close()
    requested_year = request.args.get('year')
    all_years = sorted(list(gen_rideshare_data.keys()))

    # set the style in the svg
    # https://austinpoor.com/blog/plots-with-jinja/
    taxi_zones = []
    for i in range(1,266):
        taxi_zones.append(i)
    #print(taxi_zones)

    #f = open("data/yearly_yellowtaxi_full_json/combined_yellowtaxi.json")
    f = open("combined.json")
    combined_data = json.load(f)
    f.close()

    #pickup
    year_data = combined_data[requested_year]
    pu_zones_data = {}
    # makes a dictionary
    # zone id:# of trips
    for zone in taxi_zones:
        pu_zones_data[zone] = 0

    print(pu_zones_data)

    for entry in year_data:
        current_zone = entry["pulocationid"]
        pu_zones_data[int(current_zone)] += 1

    #get total entries
    total_entries = 0
    for entry in pu_zones_data:
        total_entries += pu_zones_data[entry]

    print(max(pu_zones_data,key=pu_zones_data.get),requested_year)
    print(max(pu_zones_data.values()))
    print(total_entries)

    #get percentages for each zone
    for entry in pu_zones_data:
        pu_zones_data[entry] = ((pu_zones_data[entry])/total_entries)*1000
    
    print(max(pu_zones_data.values()))
    print(pu_zones_data)

    #drop off
        
    color_key = {
        #0 #F8E7EE
        #2 #E9C0D1
        #4 #D791AE
        #6 #C86890
        #8 #B83D70
        #10 #A20245
    }
    
    return render_template('micro.html',year=requested_year, all_years=all_years, all_zones = taxi_zones, pu_data = pu_zones_data)

app.run(debug=True)