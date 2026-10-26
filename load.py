from sqlalchemy import create_engine

# Create local SQLite DB in local folder
engine = create_engine('sqlite:///rdw_voertuigen.db')

# Load to localDB
df_clean.to_sql('voertuigen', con=engine, if_exists='replace', index=False)
print('Data successfully loaded in DB')