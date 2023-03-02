from models import Plant, Employee

while True:
    print("1. Add Plant\n2. Gel all plants\n3. Add Employee\n4. Get all employees\n5. Update employee\n6. Update Plant")
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        name = input("Employee name: ")
        email = input("Employee email: ")
        plant_id = int(input("Plant id: "))
        employee = Employee(name, email, plant_id)
        employee.save()
    elif flag == 4:
        Employee.get_all()
    elif flag == 5:
        id = int(input("Id which employee you want to update: "))
        employee = Employee.get_el_by_id(id)
        employee.update()
    elif flag == 6:
        id = int(input("Id which plant you want to update: "))
        Plant.update(id)