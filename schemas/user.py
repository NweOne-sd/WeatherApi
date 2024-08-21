from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    email: str
    city: str
    state: str
    temp: Optional[str] = None
    humidity: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

def userEntity(user) -> User:
    return User(**user)

def usersEntity(users) -> List[User]:
    return [userEntity(user) for user in users]
