import os
import pandas as pd

movie_path = os.path.join("Resources", 'MoviesOnStreamingPlatforms_updated.csv')
movies_db = pd.read_csv(movie_path, index_col= False)

columns = ['film', 'year']

titles = []
years = []
for index, rows in movies_db[:20].iterrows():
    movies_list = rows.Title
    movies_year = rows.Year
    
    titles.append(movies_list)
    years.append(movies_year)

titles = []
years = []
for index, rows in movies_db[:20].iterrows():
    movies_list = rows.Title
    movies_year = rows.Year
    
    titles.append(movies_list)
    years.append(movies_year)
