import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def search_spotify(api, artist, track):
    query = f"artist:{artist} track:{track}"
    results = api.search(q=query, type='track', limit=1)

    # Check if there are any results
    if results['tracks']['items']:
        track_info = results['tracks']['items'][0]
        spotify_url = track_info['external_urls']['spotify']

        # Extract the desired portion of the Spotify URL (fixed length of 22 characters)
        start_index = spotify_url.rfind('/') + 1
        end_index = start_index + 22

        return {
            'artist': track_info['artists'][0]['name'],
            'track': track_info['name'],
            'spotify_url': spotify_url[start_index:end_index]
        }
    else:
        return None

def main():
    # Load the CSV file
    input_file = 'tracks.csv'  # Replace with your CSV file
    df = pd.read_csv(input_file)

    # Spotify API credentials
    client_id = 'fa3880dd01dc4674b432d6dbaf889914'
    client_secret = '2c28c6a64d264628878b4acb149889b0'


    # Set up Spotify API authentication
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # List to store Spotify results
    spotify_results = []

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        artist = row.iloc[0]  # Assuming the artist is in the third column
        track = row.iloc[1]   # Assuming the track name is in the fourth column

        # Search for the track on Spotify
        result = search_spotify(sp, artist, track)

        if result:
            spotify_results.append(result)

    # Create a DataFrame from the Spotify results
    spotify_df = pd.DataFrame(spotify_results)

    # Save the Spotify results to a new CSV file
    spotify_df.to_csv('spotify_urls.csv', index=False)

if __name__ == '__main__':
    main()
