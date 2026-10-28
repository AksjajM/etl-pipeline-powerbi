import requests

# Request data
def extract(limit=1):
    url = f'https://opendata.rdw.nl/resource/m9d7-ebf2.json?$limit={limit}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()