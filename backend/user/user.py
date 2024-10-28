class User:
    def __init__(self, id: int, fname: str, sname: str, login: str, password: str, role: str) -> None:
        self.id       = id
        self.f_name    = fname
        self.s_name    = sname
        self.login    = login
        self.password = password
        self.role     = role