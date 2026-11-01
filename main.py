from extract.extract import extract
from transform.transform import transform_data
from load.load import load_to_sqlite

def run_pipeline():
    print('Extracting data...')
    raw_data = extract(limit=500)

    print('Data is transforming...')
    data = transform_data(raw_data)

    print('Loading data into database...')
    load_to_sqlite(data)

if __name__ == '__main__':
    run_pipeline()