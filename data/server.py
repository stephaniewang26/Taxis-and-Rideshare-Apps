
from flask import Flask
from flask import request
from flask import render_template
import json

#test

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/macro')
def macro():
    return render_template('macro.html')

@app.route('/micro')
def micro():
    f = open("data/tripsperday_taxi_rideshare/general_rideshare_data.json")
    gen_rideshare_data = json.load(f)
    f.close()

    #Check to see if year is passed via the query string portion of the URL
    requested_year = request.args.get('year')
    return render_template('micro.html',year=requested_year)

app.run(debug=True)