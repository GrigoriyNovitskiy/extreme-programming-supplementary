from fastapi import FastAPI

from backend.homework.homework import Homework
from backend.homework.homework_serv import HomeWorkServ
from backend.homework_result.homework_result import Homework_Result
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
    users[id] = User(id, fname, sname, login, password, role)

def login_user(self, login: str, password: str):
    pass

@app.post("/upload")
async def homework(hw: Homework):
    hw_name = ""
    with open(hw_name, "w") as fi:
        fi.write("Some hw task")
    HomeWorkServ.load_homework(hw.hw_id, hw_name)

@app.post("/eval/homework")
async def eval_hw(eval: Homework_Result):
    return HomeWorkServ.check_homework(id=eval.id, mark=eval.mark, comment=eval.comment)

@app.post("/register")
async def register(user: User):
    register_user(user.f_name, user.s_name, user.login, user.password, user.role)