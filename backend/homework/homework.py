class Homework:
    def __init__(self, user_id: int, hw_id: int):
        self.user_id = user_id
        self.hw_id = hw_id
        self.is_done = False
        self.filename = None

    def change_status(self):
        self.is_done ^= True

    def upload_solution(self, filename: str):
        self.filename = filename