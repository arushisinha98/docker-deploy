import math
import numpy as np
import pandas as pd
import csv

filepath = r"" # fill filepath
filename = r"" # fill filename
df = pd.read_csv(filepath + filename)

# isolate training rows
df_ebooks = df.loc[(df[''] == "Overdrive")]
df_physical = df.loc[(df[''] != "Overdrive")]

import sklearn
import matplotlib.pyplot as plt
import scipy
import flask
import pickle

"""
Create basic recommender
- this is a basic example b/c it only considers books read and rating given (if any)
- this DOES NOT use information about Patron demographics and book attributes aside from Genre
- this is a "wildcard" predictor

n = total number of unique books in df_extract
p = total number of unique readers in df_extract
p x n is a large and sparse matrix

suppose g = total number of unique genre classifications
p x g is a smaller matrix

1. Create a genre recommender
2. Create book recommender for each genre

code can be adapted from: https://towardsdatascience.com/item-based-collaborative-filtering-in-python-91f747200fab
"""
unique_genre = np.unique(df_ebooks['Genre'])
unique_patron = np.unique(df_ebooks['Patron'])

len_g = len(unique_genre)
len_p = len(unique_patron)

pg_mat = np.zeros([p, g])
popular_book_per_genre = np.empty([1, g], dtype = "S64")

for ig, g in enumerate(unique_genre):
  this_genre = df_ebooks.loc[(df['Genre'] == unique_genre(ig))]
  popular_book_per_genre(0, ig) = this_genre['Title'].mode()
  for ip, p in enumerate(unique_patron):
    patron_hist = df_ebooks.loc[(df['Patron'] == unique_patron(ip))]
    pg_mat(ip, ig) = count(patron_hist['Genre'] == unique_genre(ig)) # dot product with rating?

from sklearn.neighbors import NearestNeighbors
knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
pg_df = pd.DataFrame(pg_mat)
knn.fit(pg_df.values)
distances, indices = knn.kneighbors(df.values, n_neighbors = 5)

# recommend most popular book in favorite genre

# use nearest neighbor genre if most popular book in favorite genre has already been read

# use most popular book in most populat genre if no reading history

# randomized wildcards = recommendation of a highly rated book, regardless of genre

"""
Store the model file generated after training as a pickle file
"""
from sklearn.externals import joblib

model_columns = list(cf_recs.columns) # persist list of columns
joblib.dump(columns, 'model_columns.pkl')
joblib.dump(cf_recs, 'trained_model.pkl')
