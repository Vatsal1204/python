class Student:
    def __init__(self, name, grade, percentage):
        self.name = name        
        self.grade = grade      
        self.percentage = percentage  

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with percentage {self.percentage}%")


student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

student1.student_details()
student2.student_details()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")


def menu():
    person = None
    employee = None
    manager = None

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Compare Salaries")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            person = Person(name, age)
            print(f"Person created with name: {person.name} and age: {person.age}.")
        
        elif choice == 2:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employee = Employee(name, age, emp_id, salary)
            print(f"Employee created with name: {employee.name}, age: {employee.age}, ID: {employee.emp_id}, and salary: {employee.salary}.")
        
        elif choice == 3:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            manager = Manager(name, age, emp_id, salary, department)
            print(f"Manager created with name: {manager.name}, age: {manager.age}, ID: {manager.emp_id}, salary: {manager.salary}, and department: {manager.department}.")
        
        elif choice == 4:
            if person:
                person.show_details()
            elif employee:
                employee.show_details()
            elif manager:
                manager.show_details()
            else:
                print("No details available. Create an entity first.")
            
        elif choice == 5:
            print("Feature not implemented yet.")
        
        elif choice == 6:
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")
menu()
