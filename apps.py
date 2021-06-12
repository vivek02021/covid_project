from flask import Flask,render_template, url_for, request
from refresh import refresh_data
import pickle

app = Flask(__name__)


@app.route("/")
def index():
    file = open("state_data.ser","rb")
    state_data = pickle.load(file)
    file.close()
    return render_template("index.html",state_data=state_data)


# For refreshing data every 24 hours, takes long time
@app.route("/refresh")
def refresh():
    refresh_data()
    return "Data refreshed successfully"


# Single state district wise data
@app.route("/state")
def state():
    state_name = request.args["name"]

    file = open("state_data.ser","rb")
    state_data = pickle.load(file)
    file.close()

    district_data = state_data[state_name]['districtData']
    
    return render_template("state.html",district_data=district_data,state_name=state_name)



app.run()