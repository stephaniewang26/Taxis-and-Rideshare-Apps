
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
    requested_year = request.args.get('year')
    all_years = sorted(list(gen_rideshare_data.keys()))
    tripsbyk = ["800,000","700,000","600,000","500,000","400,000","300,000","200,000","100,000",]
    return render_template('macro.html',year=requested_year, all_years=all_years, trips_increment = tripsbyk)

@app.route('/micro')
def micro():
    f = open("data/tripsperday_taxi_rideshare/general_rideshare_data.json")
    gen_rideshare_data = json.load(f)
    f.close()
    requested_year = request.args.get('year')
    all_years = sorted(list(gen_rideshare_data.keys()))
    return render_template('micro.html',year=requested_year, all_years=all_years)

app.run(debug=True)