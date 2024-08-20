from pydantic import BaseModel

class State(BaseModel):
    name: str
    email: str
    city: str
    state: str
