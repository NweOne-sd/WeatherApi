from fastapi import APIRouter, Depends, HTTPException
from models.admin import Admin
from config.db import collection
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from weatherApi import weatherApi
from auth.jwt_bearer import JWTBearer
from logger import logger
from threading import Thread

admin = APIRouter()

def background_task(user_id):
    logger.info(f"Background task running for user_id: {user_id}")
    collection.local.user.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": {"status": "Task Completed"}})

@admin.get('/')
async def find_all_users(skip: int = 0, limit: int = 10):
    logger.info(f"Fetching users with skip={skip} and limit={limit}")
    return usersEntity(collection.local.user.find().skip(skip).limit(limit))

@admin.get('/{id}')
async def find_one_user(id: str):
    logger.info(f"Fetching user with id: {id}")
    return userEntity(collection.local.user.find_one({"_id": ObjectId(id)}))

@admin.post('/')
async def create_user(user: Admin):
    try:
        user_dict = dict(user)
        city = user_dict.get('city')
        temp, humidity, description = weatherApi(city)
        user_dict['temp'] = str(round(temp - 273.15)) + ' °C'
        user_dict['humidity'] = str(humidity) + ' %'
        user_dict['description'] = str(description)
        user_dict['status'] = "Task Pending"
        inserted_user = collection.local.user.insert_one(user_dict)
        thread = Thread(target=background_task, args=(str(inserted_user.inserted_id),))
        thread.start()
        logger.info(f"User created: {user.email}")
        return userEntity(collection.local.user.find_one({"_id": ObjectId(inserted_user.inserted_id)}))
    except Exception as e: 
        logger.error(f"Error creating user: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating user")

@admin.put('/{id}')
async def update_user(id: str, user: Admin):
    collection.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(collection.local.user.find_one({"_id": ObjectId(id)}))
