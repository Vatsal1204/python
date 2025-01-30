import datetime
import math
import random
import uuid

# Main Menu Function
def main_menu():
    while True:
        print("\n=== Multi-Utility Toolkit ===")
        print("1. Date and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generator")
        print("4. UUID Generator")
        print("5. File Management")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = input("Select an option (1-7): ")
        if choice == '1':
            date_time_operations()
        elif choice == '2':
            math_operations()
        elif choice == '3':
            random_data_operations()
        elif choice == '4':
            generate_uuid()
        elif choice == '5':
            file_operations()
        elif choice == '6':
            explore_module_attributes()
        elif choice == '7':
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid selection. Please try again.")

# Date and Time Operations
def date_time_operations():
    while True:
        print("\n== Date and Time Operations ==")
        print("1. Display Current Date and Time")
        print("2. Calculate Date Difference")
        print("3. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("Current Date and Time:", datetime.datetime.now())
        elif choice == '2':
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date (YYYY-MM-DD): ")
            try:
                d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
                print("Difference:", abs((d2 - d1).days), "days")
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# Mathematical Operations
def math_operations():
    while True:
        print("\n== Mathematical Operations ==")
        print("1. Calculate Factorial")
        print("2. Compound Interest Calculator")
        print("3. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            num = int(input("Enter a number: "))
            print(f"Factorial of {num}: {math.factorial(num)}")
        elif choice == '2':
            principal = float(input("Principal Amount: "))
            rate = float(input("Interest Rate (in %): "))
            time = float(input("Time Period (in years): "))
            compound_interest = principal * (pow((1 + rate / 100), time))
            print(f"Compound Interest: {compound_interest:.2f}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# Random Data Generator
def random_data_operations():
    while True:
        print("\n== Random Data Generator ==")
        print("1. Generate Random Number")
        print("2. Generate Random Password")
        print("3. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("Random Number:", random.randint(1, 100))
        elif choice == '2':
            length = int(input("Password Length: "))
            password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%", k=length))
            print("Generated Password:", password)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# UUID Generator
def generate_uuid():
    while True:
        print("\n== UUID Generator ==")
        print("1. Generate UUID1")
        print("2. Generate UUID4")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")
        
        if choice == '1':
            print("UUID1:", uuid.uuid1())
        elif choice == '2':
            print("UUID4:", uuid.uuid4())
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# File Management
def file_operations():
    while True:
        print("\n== File Management ==")
        print("1. Create a File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")
        
        if choice == '1':
            filename = input("Enter file name: ")
            with open(filename, 'w') as file:
                print("File created successfully!")
        elif choice == '2':
            filename = input("Enter file name: ")
            data = input("Enter text to write: ")
            with open(filename, 'a') as file:  # Changed 'w' to 'a' to append data
                file.write(data + "\n")
                print("Data written successfully!")
        elif choice == '3':
            filename = input("Enter file name: ")
            try:
                with open(filename, 'r') as file:
                    print("File Content:\n", file.read())
            except FileNotFoundError:
                print("File not found. Please create it first.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

# Module Attribute Exploration
def explore_module_attributes():
    module_name = input("Enter module name to explore: ")
    try:
        module = __import__(module_name)
        print("Available Attributes in", module_name, "module:")
        print(dir(module))
    except ModuleNotFoundError:
        print("Invalid module name.")

if __name__ == "__main__":
    main_menu()
