import pandas as pd

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)
    columns = ['kenteken', 'voertuigsoort', 'vervaldatum_apk', 'datum_eerste_toelating']

    # Copy selected columns
    df_clean = df[columns].copy()

    # Clean data
    df_clean['kenteken'] = df_clean['kenteken'].str.strip()

    return df_clean