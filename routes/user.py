from fastapi import APIRouter
import json
from models.user import User 
from config.db import conn,client,collection
from schemas.user import userEntity,usersEntity
from bson import ObjectId
user = APIRouter()
import requests

#weather API
API_KEY = "79dca03661d9eccf9772ce6935f90829"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


#get all users with pagination option
@user.get('/')
async def find_all_users(page: int = 1, limit: int = 2 ):
    return usersEntity(collection.local.user.find().skip((page - 1) * limit).limit(limit))

@user.get('/{id}')
async def find_one_user(id):
          #print(type(collection.local.user.find_one({"_id":ObjectId(id)})))
          #print(collection.local.user.find_one({"_id":ObjectId(id)}))
          #city = (collection.local.user.find_one({"_id":ObjectId(id)}).get("city"))
          #url = BASE_URL + "appid=" + API_KEY + "&q=" + city
          #print (city)
          #response = requests.get(url).json()

          #temp = response['main']['temp']
          #humidity = response['main']['humidity']
          #description = response['weather'][0]['description']
          
          #print('temperature = ' + str(round(temp - 273.15))+ '°C')
          #print('humidity = ' + str(humidity) + ' %')
          #print('description = ' + str(description)) 
          
          return userEntity (collection.local.user.find_one({"_id":ObjectId(id)}))

#post user info with some info about his city weather
@user.post('/')
async def create_user(user: User):
    x = (dict(user))

    city = x.get('city')
    print(city)
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city

    response = requests.get(url).json()

    temp = response['main']['temp']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
          
    print('temperature = ' + str(round(temp - 273.15))+ '°C')
    print('humidity = ' + str(humidity) + ' %')
    print('description = ' + str(description))

    x['temp'] = str(round(temp - 273.15))+ ' °C'
    x['humidity'] = str(humidity) + ' %'
    x['description'] = str(description)

    print(x)
    collection.local.user.insert_one(x)

    return usersEntity(collection.local.user.find())






















@user.put('/{id}')
async def update_user(id,user: User):
     collection.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
     return userEntity (collection.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user: User):
     return userEntity (collection.local.user.find_one_and_delete({"_id":ObjectId(id)}))

     