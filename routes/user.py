from fastapi import APIRouter, HTTPException
from models.user import UserModel
from config.db import collection

user = APIRouter()

@user.post("/", response_description="Add new user", response_model=UserModel)
async def create_user(user_data: UserModel):
    try:
        new_user = user_data.dict()
        insert_result = collection.insert_one(new_user)
        created_user = collection.find_one({"_id": insert_result.inserted_id})
        if created_user:
            return created_user
        else:
            raise HTTPException(status_code=500, detail="Error creating user")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating user")
