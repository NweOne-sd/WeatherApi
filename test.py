from pymongo import MongoClient
from decouple import config

def test_db_connection():
    mongo_uri = config('MONGODB_URI')
    client = MongoClient(mongo_uri)
    db = client.get_default_database()

    try:
        test_collection = db['test_collection']
        sample_data = test_collection.find_one()
        if sample_data:
            print("Database connection is working and data found.")
            print(sample_data)
        else:
            print("Database connection is working, but no data found.")
    except Exception as e:
        print("Database connection failed:", e)

if __name__ == "__main__":
    test_db_connection()
