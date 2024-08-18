from fastapi import FastAPI
from routes.user import user
#from routes.authUser import authUser
#from routes.admin import admin
app = FastAPI()

app.include_router(user)
#app.include_router(authUser)
#app.include_router(admin)
