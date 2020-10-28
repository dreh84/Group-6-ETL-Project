from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
from config import pg_password
import pandas as pd

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#### Database Set up######

pg_user = 'postgres'
db_name = 'etl_movie_project_db'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

@app.route('/')
def home():

    return(f"Welcome<br/>"
    f"Available Routes:<br/>"
    f'Route 1: <a href="/movie_data">/movie_data</a><br/>'
    f'Route 2: <a href="/financials">/financials</a><br/>'
    f'Route 3: <a href="/streaming">/streaming</a> For streaming platforms if 1 = Available 0 = Not available on the mentioned platform')

@app.route("/movie_data")
def movie_data():
    # Query
    results_pd = pd.read_sql_query('select * from movie_data', con=engine)
    
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


    return jsonify(movie_list)


@app.route("/financials")
def movie_financials():

    financials_pd = pd.read_sql_query('select * from movie_financials', con=engine)
    
    movie_financials = []

    for index, row in financials_pd.iterrows():
        financials_dict = {}
        financials_dict['Film'] = row['film']
        financials_dict['Revenue'] = row['revenue']
        financials_dict['Budget'] = row['budget']
        financials_dict['Profit'] = row['est_profit']
        movie_financials.append(financials_dict)

    return jsonify(movie_financials)

@app.route("/streaming")
def streaming():
    streaming_pd = pd.read_sql_query('select * from movie_streaming', con=engine)

    streaming_list = []

    for index, row in streaming_pd.iterrows():
        streaming_dict = {}

        streaming_dict['Film'] = row['title']
        streaming_dict['Year'] = row['year']
        streaming_dict['Age Group'] = row['age']
        streaming_dict['IMDB Rating'] = row['imdb']
        streaming_dict['Rotten Tomatoes Rating'] = row['rotten_tomatoes']
        streaming_dict['Netflix?'] = row['netflix']
        streaming_dict['Hulu?'] = row['hulu']
        streaming_dict['Amazon Prime Video'] = row['prime_video']
        streaming_dict['Disney+?'] = row['disney']
        streaming_dict['Director(s)'] = row['directors']
        streaming_dict['Genres'] = row['genres']
        streaming_dict['Country'] = row['country']
        streaming_dict['Language'] = row['language']
        streaming_dict['Runtime'] = row['runtime']
        streaming_list.append(streaming_dict)

    return jsonify(streaming_list)




if __name__ == '__main__':
    app.run(debug=True)




