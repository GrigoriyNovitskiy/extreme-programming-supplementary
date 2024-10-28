from fastapi import FastAPI

from backend.user.user import User
from backend.database import users

app = FastAPI()

@app.get("/login")
async def login():
    return {}

@app.get("/healthchecker")
async def check():
    return {"message": "API is alive"}

def register_user(self, fname: str, sname: str, login: str, password: str, role: str):
    global id
    id += 1
    users[id] = login

    pass
def login_user(self, login: str, password: str):
    pass

@app.post("/register")
async def register(user: User):
    register_user(user.f_name, user.s_name, user.login, user.password, user.role)