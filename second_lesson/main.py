from utils.helpers import write_new_human, get_all_humans

while True:
    print("1. Add new person! \n2. Get all persons!)")
    try:
        flag = int(input("Choose what you want to do: "))
    except ValueError:
        print("E")
        continue
    if flag == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        human_dict = {'first_name': first_name, "last_name": last_name, "email": email}
        write_new_human(human_dict)
    elif flag == 2:
        humans = get_all_humans()
        for human in humans:
            print(human["first_name"])
            print(human["last_name"])
            print(human["email"])
            print("==================================================================")
    else:
        print("Don't have this menu item")
        break