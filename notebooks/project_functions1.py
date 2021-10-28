import pandas as pd
import re

def load_and_process(tracks_csv, features_csv):
    # Load the data (load outside of method chain so tracks is reset every time this code snippet is run
    tracks = pd.read_csv(tracks_csv, low_memory=False)

    tracks = (
        tracks
        # Append specific name (row 0) to column name 
        .rename(columns=lambda x: x + ' ' + str(tracks.loc[0, x]))
        # Remove dot and number at end of original name
        .rename(columns=lambda x: re.sub("[\\.][0-9]*", "", x)) # Use a regex to remove dot followed by any number of numeric digits
        # Now remove first 2 rows after column titles
        .drop([0, 1])
        # Rename first unnamed column to id
        .rename(columns={'Unnamed: 0 nan': 'track id'})
        # Select just the columns we will be using for the analysis
        .loc[:, ['track id', 'track title', 'artist name', 'album title', 'track genre_top']]
        # Drop rows with na values
        .dropna()
    )
    # Cast track id to int (cannot apply astype to only a single column in method chain)
    tracks['track id'] = tracks['track id'].astype(int)

    # Load data; skip first 3 rows as they are just metadata headers. Use only track id and RMSE columns
    rmse = pd.read_csv(features_csv, skiprows=[0,1,2], usecols=[0, 395])

    rmse = (
        rmse
        .rename(columns={"track_id":"track id", "Unnamed: 395":"rmse_mean"})
    )
    
    # Create the main dataframe
    data = (
        pd.merge(tracks, rmse, on="track id", how="inner") # Combine metadata with RMSE
    )
    
    return data