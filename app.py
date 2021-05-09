import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import pandas as pd

file = pd.read_csv("C:\\Users\\shane\\Downloads\\incidents_cleanforproject.csv")


incident_df = pd.DataFrame(file)



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
        f"/api/v1.0/incidents<br/>"
    )


@app.route("/api/v1.0/incidents")
def incidents():
    # Create our session (link) from Python to the DB

    engine = create_engine('sqlite://', echo = False)

    incident_df.to_sql('incident_data', con = engine)

    incidents = engine.execute("SELECT * FROM incident_data").fetchall()

    return jsonify({'Incidents': [dict(row) for row in incidents]})

if __name__ == '__main__':
    app.run(debug=True)
