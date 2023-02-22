import json
import os
def create_file():
    f = open("database/persons.json", "w")
    f.write("[]")
    f.close()

def get_all_humans() -> list:
    try:
        f = open("database/persons.json", "r")
    except FileNotFoundError:
        if os.path.exists("database"):
            create_file()
        else:
            os.mkdir("database")
            create_file()
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
    if is_string_email(human["email"]):
        data.append(human)
        file = open("database/persons.json", "w")
        data = json.dumps(data)
        file.write(data)
        file.close()
    else:
        print("Your email is incorrect!")



def is_string_email(string):
    if "@" in string:
        if "." in string[string.split().index("@"):]:
            return True
        else:
            return False
    else:
        return False
