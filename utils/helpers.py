import json


def get_all_humans() -> list:
    f = open("database/persons.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def write_new_human(human: dict):
    data = get_all_humans()
    if len(data) < 1:
        human["id"] = 1
    else:
        human["id"] = len(data) + 1
    data.append(human)
    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()

