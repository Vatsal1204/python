import os
import subprocess

def start_menu():
    while True:
        print("\n=== Executer - Command Line Utility and File System Manager ===")
        print("1. File System Operations")
        print("2. Execute Terminal Commands")
        print("3. File Analysis with Higher-Order Functions")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_system_operations()
        elif choice == "2":
            execute_terminal_commands()
        elif choice == "3":
            file_analysis()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def file_system_operations():
    while True:
        print("\n=== File System Operations ===")
        print("1. Display current directory")
        print("2. List files and directories")
        print("3. Change directory")
        print("4. Create a directory")
        print("5. Remove a directory")
        print("6. Create a file")
        print("7. Delete a file")
        print("8. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current directory:", os.getcwd())
        elif choice == "2":
            print("Files and directories:", os.listdir())
        elif choice == "3":
            path = input("Enter the directory path to change to: ")
            try:
                os.chdir(path)
                print("Directory changed to", os.getcwd())
            except FileNotFoundError:
                print("Invalid directory path.")
        elif choice == "4":
            dir_name = input("Enter the name of the new directory: ")
            os.makedirs(dir_name, exist_ok=True)
            print(f"Directory '{dir_name}' created successfully.")
        elif choice == "5":
            dir_name = input("Enter the name of the directory to remove: ")
            try:
                os.rmdir(dir_name)
                print(f"Directory '{dir_name}' removed successfully.")
            except FileNotFoundError:
                print("Directory not found.")
            except OSError:
                print("Directory is not empty or cannot be removed.")
        elif choice == "6":
            file_name = input("Enter the name of the new file: ")
            with open(file_name, 'w') as f:
                f.write("")
            print(f"File '{file_name}' created successfully.")
        elif choice == "7":
            file_name = input("Enter the name of the file to delete: ")
            try:
                os.remove(file_name)
                print(f"File '{file_name}' deleted successfully.")
            except FileNotFoundError:
                print("File not found.")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

def execute_terminal_commands():
    while True:
        print("\n=== Execute Terminal Commands ===")
        print("1. Run a predefined command (e.g., pwd, ls)")
        print("2. Run a custom command")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("1. pwd")
            print("2. ls")
            print("3. df -h")
            cmd_choice = input("Choose a command: ")

            if cmd_choice == "1":
                subprocess.run(["pwd"])
            elif cmd_choice == "2":
                subprocess.run(["ls"])
            elif cmd_choice == "3":
                subprocess.run(["df", "-h"])
            else:
                print("Invalid command choice.")
        elif choice == "2":
            custom_command = input("Enter the custom command to execute: ")
            try:
                subprocess.run(custom_command.split())
            except FileNotFoundError:
                print("Command not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def file_analysis():
    while True:
        print("\n=== File Analysis with Higher-Order Functions ===")
        print("1. Sort files by name")
        print("2. Filter files by extension")
        print("3. Calculate total size of files in a directory")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            files = sorted(os.listdir())
            print("Files sorted by name:")
            for f in files:
                print(f)
        elif choice == "2":
            ext = input("Enter file extension to filter by (e.g., .txt): ")
            filtered_files = list(filter(lambda f: f.endswith(ext), os.listdir()))
            print("Filtered files:")
            for f in filtered_files:
                print(f)
        elif choice == "3":
            total_size = sum(os.path.getsize(f) for f in os.listdir() if os.path.isfile(f))
            print(f"Total size of files: {total_size} bytes")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start_menu()