import pandas as pd
import re

def chain(tracks_csv="../data/raw/tracks.csv", features_csv="../data/raw/features.csv"):
    """
        Method chain function to load and process tracks and features data for analysis 1 (Will)
    """
    
    tracks = pd.read_csv(tracks_csv, low_memory=False) # must load before method chain as first rename statement references another row, which requires having this loaded prior to the method chain
    # tracks
    tracks = (
        tracks
        # Append specific name (row 0) to column name 
        .rename(columns=lambda x: x + ' ' + str(tracks.loc[0, x]))
        # Remove dot and number at end of original name
        .rename(columns=lambda x: re.sub("[\\.][0-9]*", "", x)) # Use a regex to remove dot followed by any number of numeric digits
        # Now remove first 2 rows after column titles
        .drop([0, 1])
        # Rename first unnamed column to id
        .rename(columns={'Unnamed: 0 nan': 'track id', 'track genre_top': 'genre'})
        # Select just the columns we will be using for the analysis
        .loc[:, ['track id', 'track title', 'artist name', 'album title', 'genre']]
        # Drop rows with na values
        .dropna()
    )
    # Cast track id to int (cannot apply astype to only a single column in method chain)
    tracks['track id'] = tracks['track id'].astype(int)

    # Features
    # Load data; skip first 3 rows as they are just metadata headers. Use only track id and RMSE columns
    cols = [0] + list(range(293,314)) + [395] # list of coumns we want to use
    features = pd.read_csv("../data/raw/features.csv", skiprows=[0,1,2], usecols=cols)

    features = (
        features
        # Rename track id and rmse mean
        .rename(columns={"track_id":"track id", "Unnamed: 395":"rmse_mean"})
        # Rename 20 mfcc columns via lambda function
        .rename(columns=lambda x: 'mfcc' + str(int(x[x.index(':')+1:]) - 292) if ':' in x else x)
    )

    # Merge features and tracks data
    data = (
        pd.merge(tracks, features, on="track id")
    )
    
    return data