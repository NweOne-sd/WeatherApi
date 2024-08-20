from fastapi import APIRouter
from models.state import State

state = APIRouter()

@state.get('/')
async def find_all_states():
    return {"states": []}  

@state.get('/{id}')
async def find_state(id: str):
    return {"state": {"id": id}}
