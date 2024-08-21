from fastapi import APIRouter, Depends
from config.db import collection
from concurrent.futures import ThreadPoolExecutor
from schemas.user import usersEntity
from auth.jwt_bearer import JWTBearer

batch = APIRouter()

def process_user_batch(user_ids):
    users = collection.local.user.find({"_id": {"$in": user_ids}})
    total_temp = 0
    count = 0

    for user in users:
        if 'temp' in user:
            temp_celsius = float(user['temp'].split(' ')[0])
            total_temp += temp_celsius
            count += 1

    if count > 0:
        avg_temp = total_temp / count
        return avg_temp
    return None

@batch.post('/batch-process', dependencies=[Depends(JWTBearer())])
async def batch_process():
    user_ids = [user['_id'] for user in collection.local.user.find({}, {"_id": 1})]
    chunk_size = len(user_ids) // 4  # Divide users into 4 threads

    with ThreadPoolExecutor() as executor:
        results = executor.map(process_user_batch, [user_ids[i:i + chunk_size] for i in range(0, len(user_ids), chunk_size)])

    avg_temp = sum(filter(None, results)) / len(user_ids)
    return {"average_temperature": avg_temp}
