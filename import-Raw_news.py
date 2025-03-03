import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('/data/raw_news.csv')

client = MongoClient('mongodb://mongodb:27017/')
db = client['sentiment_analysis']
collection = db['raw_news']

records = df.to_dict('records')
collection.insert_many(records)

print(f"Imported {len(records)} records into raw_news collection")

print(f"Count of documents in raw_news collection: {collection.count_documents({})}")