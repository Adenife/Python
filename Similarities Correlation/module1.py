# import the libraries to be used in reading the data and performing operatons on it
import numpy as np
import pandas as pd
from io import StringIO
import csv


data = []

with open('data.csv', encoding='utf-8') as f:
    data_reader = csv.reader(f, delimiter=',')
    for row in data_reader:
        data.append(row)


# read in the csv file
data = pd.read_csv('data.csv')


# Check the top five rows of the data to have a glimpse of how the table looks like
# data.head()


# check for missing values in the data. It io sseen the data has no missing values
# data.isnull().sum()

# check for the dimension of the data
# data.shape

# print the names of all columns in the dataset
# data.columns

# retrieve the required columns and check
specific_columns = data[['acousticness', 'artists', 'danceability', 'energy', 'id', 'liveness', 
                         'loudness', 'name', 'popularity', 'speechiness', 'tempo', 'valence']]

# specific_columns.head()

# create id for the artist. Each artist is is linked to a specific id. An artist having multiple rows (obsrvation) has same id
specific_columns['artist_id'] = specific_columns.groupby(['artists']).ngroup()

# check the new dimension of the data
# specific_columns.head()
# specific_columns.set_index('artist_id').T.to_dict('list')



# functions to get the required columns fo the different dictionaries to be created

def artist_music(data):
    '''
    Takes in a dataset, extracts specific columns and transforms the columns into a dictionary.
    The funtion stores the columns as a dictionary in memory.
    
    Parameter:
    data - A single dataset having rows and columns.
    '''
    
    artist = data[['acousticness', 'artists', 'danceability', 'energy', 'artist_id', 'liveness', 
                   'loudness', 'name', 'popularity', 'speechiness', 'tempo', 'valence']]
    
    return artist.set_index('artist_id').T.to_dict('list')


def music_features(data):
    '''
    Takes in a dataset, extracts specific columns and transforms the columns into a dictionary.
    The funtion stores the columns as a dictionary in memory.
    
    Parameter:
    data - A single dataset having rows and columns.
    '''
    
    artist = data[['acousticness', 'danceability', 'energy', 'id', 'liveness', 
                   'loudness', 'popularity', 'speechiness', 'tempo', 'valence']]
    
    return artist.set_index('id').T.to_dict('list')

# create the containers (variables) holding the dictionaries
music = music_features(specific_columns)
artist = artist_music(specific_columns)

# artist[4880]
# artist[9738]