class Homework_Result:
    def __init__(self, id: int, mark: float, comment: str = "", fixes: bool = False):
        self.id = id
        self.mark = mark
        self.comment = comment
        self.fixes   = fixes