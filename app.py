import numpy as np
import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import numpy as np
import pandas as pd

import datetime as dt
from matplotlib import style, figure
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
import matplotlib.dates as DateFormatter
# #################################################
# # Database Setup
# #################################################
# engine = create_engine("sqlite:///hawaii.sqlite")

# # reflect an existing database into a new model
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# # Save reference to the table
# # print(Base.classes.keys())

# measurement = Base.classes.measurement
# station= Base.classes.station
# session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start]<br/>"
        f"/api/v1.0/[start]/[end]<br/>")

@app.route("/api/v1.0/precipitation")

def index():
    return render_template('index.html', title="page", jsonfile=jsonify(data))

def precipitation(): 
    #     ##DO STH
    with open('Resources/pcpt_12mth.json', 'r') as pcpt_file:
        data = pcpt_file.read()

#     pcpt_12mth_q = session.query(measurement.prcp, measurement.date).filter(measurement.date>'2016-08-23').all()
    
#     #  pcpt_12mth=pd.dataFrame(pcpt_12mth_q, columns =['Precipitation', 'Date']) 
#     #  pcpt_12mth=pcpt_12mth.set_index('Date')
#     #  pcpt_12mth=pcpt_12mth.sort_values('Date',ascending=True)
#     #  pcpt_12mth=pcpt_12mth.dropna()
#     #  return (pcpt_12mth)
#     pcpt_12mth=dict()
#     for prcp, date in pcpt_12mth_q: 
#         pcpt_12mth[date] = prcp
#     return jsonify(pcpt_12mth)

# @app.route("/api/v1.0/stations")
# def stations():     
#     name_station=session.query(measurement.station).group_by(measurement.station).all()
#     return jsonify(name_station)
# # @app.route("/api/v1.0/tobs")
# def tobs():     
#     ##DO STH


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def startend(start, end = None): #none in function definition is optional     
    max_temp=session.query(measurement.station, func.max(measurement.tobs)).filter(measurement.date> start).all()
    return jsonify(max_temp)
    # min_temp=session.query( measurement.station, func.min(measurement.tobs)).filter(measurement.date>start).filter(measurement.date<end).all()
    # ave_temp=session.query( measurement.station, func.avg(measurement.tobs)).filter(measurement.date>start).filter(measurement.date<end).all()





if __name__ == '__main__':
    app.run(debug=True)
