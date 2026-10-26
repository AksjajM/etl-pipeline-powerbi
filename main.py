import pandas as pd
import requests

# Request the data and add it to a pandas datafram
r = requests.get('https://opendata.rdw.nl/resource/m9d7-ebf2.json?$limit=1')
df = pd.DataFrame(r.json())

# Transform the original data and paste into df_clean
columns = ['kenteken', 'voertuigsoort', 'vervaldatum_apk', 'datum_eerste_toelating']
df_clean = df[columns].copy()

# Strip spaces
df_clean['kenteken'] = df_clean['kenteken'].str.strip()