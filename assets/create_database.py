# create database for Ch3

import pandas as pd
import sqlite3
from urllib.request import urlretrieve
import os

# asset urls 
url = 'https://assets.datacamp.com/production/repositories/4180/datasets/82c41048fc89f03f3b0a4122642bc4fd39306071/Spotify_Popularity.csv'

# download assets locally 
urlretrieve(url, 'Spotify_Popularity.csv')

# import into python
df = pd.read_csv('Spotify_Popularity.csv')

# load into sqlite3
with sqlite3.connect('SpotifyDatabase.db') as conn:
  cursor = conn.cursor()
  df.to_sql("Spotify_Popularity", conn, if_exists = 'replace', index = False)
  conn.commit()
conn.close()

# remove original to keep a clear local directory   
os.remove("Spotify_Popularity.csv")