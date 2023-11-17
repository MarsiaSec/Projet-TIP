import pandas as pd
import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

def search_spotify(api, artist, track):
    query = f"artist:{artist} track:{track}"
    results = api.search(q=query, type='track', limit=1)

    # Check if there are any results
    if results['tracks']['items']:
        print(results.headers)
        track_info = results['tracks']['items'][0]
        return {
            'track': track_info['name'],
            'artist': track_info['artists'][0]['name'],
            'id': track_info['id']
        }
    else:
        return None

def get_audio_features(api, track_id):
    # Get audio features for the track
    audio_features = api.audio_features(track_id)

    if audio_features:
        return audio_features[0]
    else:
        return None

def main():
    # Load the CSV file
    input_file = 'spotify_urls.csv'  # Replace with your CSV file containing Spotify URLs
    df = pd.read_csv(input_file)

    # Spotify API credentials
    client_id = '3f09b325ef104402927597303f57f53b'
    client_secret = 'f23bbeaf882843d291c2abdb9697801e'

    # Set up Spotify API authentication
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # List to store Spotify and audio features results
    results = []

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        artist = row['artist']
        track = row['track']
        track_id = row['spotify_url']

        # Get general track information
        spotify_result = search_spotify(sp, artist, track)

        if spotify_result:
            # Get audio features for the track
            audio_features_result = get_audio_features(sp, track_id)

            if audio_features_result:
                # Combine results into a single dictionary
                result = {
                    'track': spotify_result['track'],
                    'artist': spotify_result['artist'],
                    'uri': f"spotify:track:{track_id}",
                    'danceability': audio_features_result['danceability'],
                    'energy': audio_features_result['energy'],
                    'key': audio_features_result['key'],
                    'loudness': audio_features_result['loudness'],
                    'mode': audio_features_result['mode'],
                    'speechiness': audio_features_result['speechiness'],
                    'acousticness': audio_features_result['acousticness'],
                    'instrumentalness': audio_features_result['instrumentalness'],
                    'liveness': audio_features_result['liveness'],
                    'valence': audio_features_result['valence'],
                    'tempo': audio_features_result['tempo'],
                    'duration_ms': audio_features_result['duration_ms'],
                    'time_signature': audio_features_result['time_signature'],
                }

                results.append(result)
                print(result)
    
    # Add three columns with zeros
    df['chorus_hit'] = 0
    df['sections'] = 0
    df['target'] = 0


    # Create a DataFrame from the results
    final_df = pd.DataFrame(results)

    # Save the final results to a new CSV file
    final_df.to_csv('dataset2018_2023.csv', index=False, sep=';', encoding='utf-8')

if __name__ == '__main__':
    main()
