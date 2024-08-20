from pydantic import BaseModel

class Admin(BaseModel):
    name: str
    email: str
    city: str
    state: str