from fastapi import FastAPI

from backend.model.user import User
from backend.service.user_service import UserService

app = FastAPI()


@app.get("/healthchecker/")
async def check():
    return {"message": "API is live"}


@app.get("/login/")
async def login():
    return {}


@app.post("/register/")
async def register(user: User):
    UserService().register(user)


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return UserService().get_user(user_id)

