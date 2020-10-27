from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
from config import pg_password

app = Flask(__name__)

#### Database Set up######

pg_user = 'postgres'
db_name = 'etl_movie_project_db'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')
Base = automap_base()
Base.prepare(engine, reflect = True)
financials = Base.classes.movie_financials
streaming = Base.classes.movie_streaming
data = Base.classes.movie_data

@app.route('/')
def home():

    return(f"Welcome")

@app.route("/movie_data")
def movie_data():
    session = Session(engine)
    results = session.query(data.film, data.year, data.netflix, data.hulu, data.prime_video, data.disney, data.revenue, data.budget, data.est_profit).all()

    movie_list = []
    for film, year, netflix, hulu, prime_video, disney, revenue, budget, est_profit in results:
        movie_dict = {}
        movie_dict["Film"] = film
        movie_dict["Year"] = year
        movie_dict["Netflix"] = netlix
        movie_dict["Hulu"] = hulu
        movie_dict["Amazon Prime"] = prime_video
        movie_dict["Disney"] = disney
        movie_dict["Revenue"] = revenue
        movie_dict["budget"] = budget
        movie_dict["Profit"] = est_profit
        movie_list.append(movie_disct)

    session.close()

    return jsonifu(return_list)


# @app.route("/financial/rawdata")
# session = Session

# @app.route("/streaming")






if __name__ == '__main__':
    app.run(debug=True)




