from pydantic import BaseModel

class AuthUser(BaseModel):
    name: str
    email: str
    city: str
    state: str

print("AuthUser model defined")
