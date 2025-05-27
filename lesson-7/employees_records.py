import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = str(employee_id)
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def employee_exists(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(str(employee_id) + ","):
                    return True
        return False

    @staticmethod
    def add_employee(employee):
        if EmployeeManager.employee_exists(employee.employee_id):
            print("Error: Employee ID already exists.")
            return
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee}\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees(sort_by=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            employees = [line.strip() for line in file]

        if sort_by == "name":
            employees.sort(key=lambda x: x.split(",")[1].strip().lower())
        elif sort_by == "salary":
            employees.sort(key=lambda x: float(x.split(",")[3]), reverse=True)

        print("Employee Records:")
        for emp in employees:
            print(emp)

    @staticmethod
    def search_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(str(employee_id) + ","):
                    print("Employee Found:\n" + line.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return

        employees = []
        updated = False

        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == str(employee_id):
                    if name:
                        data[1] = name
                    if position:
                        data[2] = position
                    if salary:
                        data[3] = str(salary)
                    updated = True
                employees.append(",".join(data))

        if updated:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                for emp in employees:
                    file.write(emp + "\n")
            print("Employee record updated successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return

        employees = []
        deleted = False

        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(str(employee_id) + ","):
                    employees.append(line.strip())
                else:
                    deleted = True

        if deleted:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                for emp in employees:
                    file.write(emp + "\n")
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

# --------- Main Program Loop ---------

def main():
    print("Welcome to the Employee Records Manager!")
    while True:
        print("\nMenu:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = float(input("Enter Salary: "))
                emp = Employee(emp_id, name, position, salary)
                EmployeeManager.add_employee(emp)
            except ValueError:
                print("Invalid salary input.")
        elif choice == '2':
            sort = input("Sort by (name/salary/none): ").lower()
            if sort not in ("name", "salary"):
                sort = None
            EmployeeManager.view_all_employees(sort_by=sort)
        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            EmployeeManager.search_employee(emp_id)
        elif choice == '4':
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (or press Enter to skip): ") or None
            position = input("Enter new Position (or press Enter to skip): ") or None
            salary_input = input("Enter new Salary (or press Enter to skip): ")
            salary = float(salary_input) if salary_input else None
            EmployeeManager.update_employee(emp_id, name, position, salary)
        elif choice == '5':
            emp_id = input("Enter Employee ID to delete: ")
            EmployeeManager.delete_employee(emp_id)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
