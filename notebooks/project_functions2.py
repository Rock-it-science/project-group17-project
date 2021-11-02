import pandas as pd

#load 
tracks_raw = pd.read_csv("../data/raw/tracks.csv", low_memory=False)

def jinData(jintracks = "../data/raw/tracks.csv"):
    
    #Method Chain (Loading data and dealing with missing data)
    tracks_cleanup = (
        
    #Only taking the columns needed for my research question
    tracks_raw[['Unnamed: 0', 'track.3', 'track.6', 'track.7', 'track.14', 'artist.12', 'track.19']]
        
    #Giving Columns sensible names
    .rename(columns = {'Unnamed: 0': "Track ID", 'track.3': "year of release", 'track.6': "favorites", 'track.7': "genre", 'track.14': "number of listens", 'artist.12': "artist name", 'track.19': "track title"})
        
    #Dropping any rows with missing values (NaN values) from the dataset
    .dropna()
)
    
    #The rest of the steps had to be done outside tracks_cleanup because I can't work on single columns within it.
    
    #cut off string values beyond the first four digits, telling us the year because the rest is not needed
    tracks_cleanup['year of release'] = tracks_cleanup['year of release'].str[:4]
    
    #Change the strings into integers
    tracks_cleanup[['year of release', 'favorites', 'number of listens']] = tracks_cleanup[['year of release', 'favorites', 'number of listens']].astype(int)
    
    #only taking columns needed
    tracks_cleanup = tracks_cleanup[['artist name', 'track title', 'Track ID', 'year of release', 'genre', 'favorites', 'number of listens']]
    tracks_cleanup

    return tracks_cleanup


