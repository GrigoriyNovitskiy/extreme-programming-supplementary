from fastapi import FastAPI

from backend.homework.homework import Homework
from backend.homework.homework_serv import HomeWorkServ
from backend.homework_result.homework_result import Homework_Result
from backend.database import users
from backend.model.user import User
from backend.service.user_service import UserService

app = FastAPI()


@app.get("/healthchecker/")
async def check():
    return {"message": "API is live"}

@app.post("/upload")
async def homework(hw: Homework):
    hw_name = ""
    with open(hw_name, "w") as fi:
        fi.write("Some hw task")
    HomeWorkServ.load_homework(hw.hw_id, hw_name)

@app.post("/eval/homework")
async def eval_hw(eval: Homework_Result):
    return HomeWorkServ.check_homework(id=eval.id, mark=eval.mark, comment=eval.comment)


@app.get("/login/")
async def login():
    return {}


@app.post("/register/")
async def register(user: User):
    UserService().register(user)


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return UserService().get_user(user_id)

