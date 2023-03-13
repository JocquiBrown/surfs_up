# Import Python Dependencies
import datetime as dt
import numpy as np
import pandas as pd
print(pd.__version__)

# Import SQLAlchemy Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask Dependencies
from flask import Flask, jsonify

# Access the SQLite Database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the Database into Classes
Base = automap_base()

# Reflect the Tables
Base.prepare(engine, reflect = True)

# Save References to each Table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a Session Link from Python to our Database
session = Session(engine)

# Define our Flask App
app2 = Flask(__name__)

# Define the Welcome Route as the Root
@app2.route("/")

# Add the Routing Information for each of the other Routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create the Precipitation Route
@app2.route("/api/v1.0/precipitation")
def precipitation():
    # Add the line of code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify (precip)

# Define the Stations Route and Name
@app2.route("/api/v1.0/stations")
def stations():
    # Create a query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()
    
    # Unravel results and convert results to a list
    stations = list(np.ravel(results))
    
    # Return list as a JSON
    return jsonify(stations=stations)

# Define the Temperature Observations Route and Name
@app2.route("/api/v1.0/tobs")
def temp_monthly():
    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    # Unravel the results into a one-dimensional array, convert the array into a list, then jsonify the list and return the results
    temps = list(np.ravel(results))
    return jsonify (temps=temps)

# Define the statistics route and name. Provide a starting and ending date
@app2.route("/api/v1.0/temp/<start>")
@app2.route("/api/v1.0/temp/<start>/<end>")

# Create a function called stats() to put our code in and add a start and stop parameter
def stats(start=None, end=None):
     # Create a query to select the min, aveg, and max temps, start by creating a list
     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

# Create an if-not statement to query the database for multiple results (start and end)
     if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        
        # Unravel the results into a one-dimensional array, convert the array into a list, then jsonify the list and return the results
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    # Query the data to calculate the temperature minimum, average, and maximum with the start and end dates
     results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
     
     # Unravel the results into a one-dimensional array, convert the array into a list, then jsonify the list and return the results
     temps = list(np.ravel(results))
     return jsonify(temps)

# Run the Flask app
if __name__ == '__main__':
    app2.run()

