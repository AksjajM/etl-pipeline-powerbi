import pandas as pd
import requests


df = pd.DataFrame(r.json())

# Transform the original data and paste into df_clean
columns = ['kenteken', 'voertuigsoort', 'vervaldatum_apk', 'datum_eerste_toelating']
df_clean = df[columns].copy()

# Strip spaces
df_clean['kenteken'] = df_clean['kenteken'].str.strip()

# Request data
def extract(limit=1):
    url = f'https://opendata.rdw.nl/resource/m9d7-ebf2.json?$limit={limit}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()