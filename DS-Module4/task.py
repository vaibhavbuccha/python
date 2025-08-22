# EMS

employees = {
    101: {
        'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000
    }
}


def main_menu():
    print("** :: EMS :: **")
    while True: 
        try:
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Search for Employee")
            print("4. Exit")
            option = int(input("Please select option from the menu (1-4)"))
            if option == 1:
                add_employee()
            elif option == 2:
                view_employees()
            elif option == 3:
                search_employee()
            elif option == 4:
                print("Thankyou for choose our EMS")
                break
            else:
                print("Please select a valid option")
        except ValueError: 
            print("Invalid Input")


def add_employee(): 
    print("Please Enter employee details: ")
    while True:
        try: 
            emp_id = int(input("Please enter Employee ID: "))
            if emp_id in employees :
                print("Employee ID is already registered")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer ID.")

    name = input("Please enter employee name: ").strip()
    while True:
        try:
            age = int(input("Please enter employee age: "))
            break
        except ValueError: 
            print("Invalid input. Please enter a valid integer age.")
    
    department = input("Enter Employee Department: ").strip()
    while True:
        try:
            salary = float(input("Please enter employee salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid salary")
        
    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    print(f"Employee '{name}' added successfully!")


def view_employees():
    # print(employees)
    print("-"*92)
    print(f"{'ID':<6}{'Name':<20}{'Age':<10}{"Department":<20}{"salary":<20}")
    print("-"*92)
    for emp in employees:
        print(f"{emp:<6}{employees[emp]['name']:<20}{employees[emp]['age']:<10}{employees[emp]['department']:<20}{employees[emp]['salary']:<20}")
    print("-"*92)



def search_employee():
    try:
        empId = int(input("Please enter Employee ID: "))
        if empId in employees:
            print(employees[empId])
            print("-"*92)
            print(f"{'ID':<6}{'Name':<20}{'Age':<10}{"Department":<20}{"salary":<20}")
            print("-"*92)
            print(f"{empId:<6}{employees[empId]['name']:<20}{employees[empId]['age']:<10}{employees[empId]['department']:<20}{employees[empId]['salary']:<20}")
            print("-"*92)
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter valid Employee ID")



main_menu()