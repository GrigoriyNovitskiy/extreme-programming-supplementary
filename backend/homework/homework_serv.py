from backend.database import hw
from backend.database import result
from backend.homework_result.homework_result import Homework_Result

class HomeWorkServ:
    def get_homework_res(self):
        resulting = {}
        keys = hw.keys()
        for r in keys:
            homework = result[r]
            resulting[r] = resulting.get(result, []) + [(homework.hw_id, homework.hw_result)]
        return resulting
    def load_homework(self, id: int, filename):
        hw[id].filename = filename
    def check_homework(self, id: int, mark: float, comment: str="", fix: bool = True):
        result[id] = Homework_Result(id = id, mark=mark, comment=comment, fixes=fix)


