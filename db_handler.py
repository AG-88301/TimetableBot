import json

def add(usr: str, pars: list) -> None:
    with open('db.json', "r") as f:
        db = json.load(f)

    db = dict(db)
    if usr in db.keys():
        db[usr][pars[0]] = pars[1]
    else:
        db[usr] = {pars[0]: pars[1]}

    with open('db.json', "w") as f:
        json.dump(db, f)
        
def get(usr: str, attr: str) -> str:
    with open('db.json', 'r') as f:
        data = json.load(f)
    return data[usr][attr]
