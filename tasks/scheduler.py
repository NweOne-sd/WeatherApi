from datetime import datetime, timedelta
from config.db import collection
from bson import ObjectId

def auto_inactivate_users():
    threshold_date = datetime.utcnow() - timedelta(days=30)
    users = collection.local.user.find({"last_login": {"$lt": threshold_date}, "state": "Active"})
    
    for user in users:
        collection.local.user.update_one({"_id": ObjectId(user["_id"])}, {"$set": {"state": "Inactive"}})
