from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://mostafaworknow:BQm8EYwz4225JqrW@afaqy.me3rg.mongodb.net/?retryWrites=true&w=majority"  # Ensure this matches your setup
client = MongoClient(MONGODB_URI)

db = client['user_management']
collection = db['users']  
print(f"Connecting to MongoDB at {MONGODB_URI}")
try:
  
    client.admin.command('ping')
    print("Database connection successful")
except Exception as e:
    print(f"Failed to connect to the database: {str(e)}")



from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://mostafaworknow:BQm8EYwz4225JqrW@afaqy.me3rg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)
