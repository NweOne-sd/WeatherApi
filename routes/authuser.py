from fastapi import APIRouter, HTTPException
from models.authuser import AuthUser
from config.db import collection
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from weatherApi import weatherApi
from auth.jwt_bearer import JWTBearer

authuser = APIRouter()

@authuser.get('/')
async def find_all_users(skip: int = 0, limit: int = 10):
    return usersEntity(collection.local.user.find().skip(skip).limit(limit))

@authuser.get('/{id}')
async def find_one_user(id: str):
    user = collection.local.user.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return userEntity(user)

@authuser.post('/')
async def create_user(user: AuthUser):
    user_dict = dict(user)
    city = user_dict.get('city')
    temp, humidity, description = weatherApi(city)
    user_dict['temp'] = str(round(temp - 273.15)) + ' °C'
    user_dict['humidity'] = str(humidity) + ' %'
    user_dict['description'] = str(description)
    user_dict['status'] = "Task Pending"
    inserted_user = collection.local.user.insert_one(user_dict)
    return userEntity(collection.local.user.find_one({"_id": ObjectId(inserted_user.inserted_id)}))

@authuser.put('/{id}')
async def update_user(id: str, user: AuthUser):
    result = collection.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return userEntity(collection.local.user.find_one({"_id": ObjectId(id)}))
