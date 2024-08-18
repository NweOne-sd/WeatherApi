from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

conn = "mongodb+srv://mostafaworknow:BQm8EYwz4225JqrW@afaqy.me3rg.mongodb.net/?retryWrites=true&w=majority&appName=Afaqy"

# Create a new client and connect to the server
client = MongoClient(conn, server_api=ServerApi('1'))


db = client.user_db
collection = db["user_data"]

