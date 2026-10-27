from sqlalchemy import create_engine

def load_to_sqlite(df, db_name='rdw_voertuigen.db', table_name='voertuigen'):
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Succesvol {len(df)} rijen weggeschreven naar tabel '{table_name}' in {db_name}")