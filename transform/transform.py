import pandas as pd

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)
    columns = ['kenteken', 'voertuigsoort', 'vervaldatum_apk', 'datum_eerste_toelating']

    # Copy selected columns
    df_clean = df[columns].copy()

    # Clean data
    df_clean['kenteken'] = df_clean['kenteken'].str.strip()

    # Format date
    df_clean['vervaldatum_apk'] = pd.to_datetime(
        df_clean['vervaldatum_apk'],
        format='%Y%m%d',
        errors='coerce'
    ).dt.date

    # Format date
    df_clean['datum_eerste_toelating'] = pd.to_datetime(
        df_clean['datum_eerste_toelating'],
        format='%Y%m%d',
        errors='coerce'
    ).dt.date

    return df_clean
    # print(df_clean)