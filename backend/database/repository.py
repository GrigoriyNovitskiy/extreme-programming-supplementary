from backend.database.database import users
from backend.model.user import User


class UserRepository:
    def add_user(self, user: User):
        id = len(users)
        users[id] = user

    def get_user(self, id: int):
        return users[id]

