import json

class Database:
    def __init__(self):
        with open('db.json', "r") as f:
            self.db = json.load(f)
        
    def add(self, usr: str, pars: list) -> None:
        db = dict(self.db)
        if usr in db.keys():
            db[usr][pars[0]] = pars[1]
        else:
            db[usr] = {pars[0]: pars[1]}

        with open('db.json', "w") as f:
            json.dump(db, f)
        self.db = db
            
    def get(self, usr: str, attr: str) -> str:
        return self.db[usr][attr]

    def find(self, usr:str, par:str) -> bool:
        if usr in self.db.keys():
            if par in self.db[usr].keys():
                return True
        return False
