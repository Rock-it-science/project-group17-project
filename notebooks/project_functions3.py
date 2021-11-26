import pandas as pd
import numpy as np

#Method chaining function (Load and process data; deal with missing data, etc.)
def unprocessed(tracks_csv="../data/raw/tracks.csv"):
    #Loading data
    data = pd.read_csv(tracks_csv, low_memory=False) 
    data = (
        data
        
        #Remove row 1
        .drop(data.index[1])
        
        #Select needed columns that we will be using for the analysis
        .loc[:, ['Unnamed: 0','track.7', 'track.14', 'artist.12', 'artist.9', 'album.2']]
        
        #Rename columns that we will be using for the analysis
        .rename(columns={'Unnamed: 0': 'Track ID', 'track.7': 'Genre', 'track.14': 'Listens', 'artist.12': 'Artist Name', 'artist.9': 'Location', 'album.2': 'Release Date'})
       
        #Drop rows with na values
        .dropna()
    )
    
        return data
    