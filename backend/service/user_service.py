from backend.database.repository import UserRepository
from backend.model.user import User


class UserService:
    def register(self, user: User):
        UserRepository().add_user(user=user)

    def get_user(self, user_id: int):
        UserRepository().get_user(user_id)
