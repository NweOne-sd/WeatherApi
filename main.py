from fastapi import FastAPI
from routes.user import user
from routes.authuser import authuser
from routes.admin import admin
from routes.state import state
from tasks.scheduler import auto_inactivate_users
from fastapi_utils.tasks import repeat_every
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

app = FastAPI()

app.include_router(user)
app.include_router(authuser)
app.include_router(admin)
app.include_router(state)

@app.on_event("startup")
@repeat_every(seconds=60*60)  # Run every hour
def run_auto_inactivate_users():
    auto_inactivate_users()
