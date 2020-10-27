from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
from config import pg_password
import pandas as pd

app = Flask(__name__)

#### Database Set up######

pg_user = 'postgres'
db_name = 'etl_movie_project_db'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')
# Base = automap_base()
# Base.prepare(engine, reflect = True)
# financials = Base.classes.movie_financials
# streaming = Base.classes.movie_streaming
# data = Base.classes.movie_data

@app.route('/')
def home():

    return(f"Welcome<br/>"
    f"Available Routes:<br/>"
    f"Route 1: /movie_data")

@app.route("/movie_data")
def movie_data():
    # Query
    results_pd = pd.read_sql_query('select * from movie_data', con=engine)
    
    # session = Session(engine)
    # results = session.query(data.film, data.year, data.netflix, data.hulu, data.prime_video, data.disney, data.revenue, data.budget, data.est_profit).all()
    
    movie_list = []
    
    for index, row in results_pd.iterrows():
        movie_dict = {}
        movie_dict["Film"] = row['film']
        movie_dict["Year"] = row['year']
        movie_dict["Netflix"] = row['netflix']
        movie_dict["Hulu"] = row['hulu']
        movie_dict["Amazon Prime"] = row['prime_video']
        movie_dict["Disney"] = row['disney']
        movie_dict["Revenue"] = row['revenue']
        movie_dict["Budget"] = row['budget']
        movie_dict["Profit"] = row['est_profit']
        movie_list.append(movie_dict)
    # session.close()

    return jsonify(movie_list)


@app.route("/financials")
def movie_financials():

    financials_pd = pd.read_sql_query('select * from movie_financials', con=engine)
    financials_json = financials_pd.to_json(split)
    return financials_json

# @app.route("/streaming")



if __name__ == '__main__':
    app.run(debug=True)




