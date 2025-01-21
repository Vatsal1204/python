import os
from datetime import datetime

FILE_NAME = "my_journal.txt"

def add_new_entry():
    print("\n--- Add a New Entry ---")
    entry = input("Write your journal entry: ")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    with open(FILE_NAME, "a") as file:
        file.write(f"{timestamp} {entry}\n")
    print("Your entry has been saved!\n")

def view_all_entries():
    print("\n--- View All Entries ---")
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            entries = file.readlines()
            if entries:
                print("Your Journal Entries:")
                print("-" * 30)
                for entry in entries:
                    print(entry.strip())
                print("-" * 30)
            else:
                print("The journal file is empty. Add an entry first!")
    else:
        print("No journal file found. Please add an entry to create one.\n")

def search_entry():
    print("\n--- Search for an Entry ---")
    if os.path.exists(FILE_NAME):
        search_term = input("Enter a keyword or date (YYYY-MM-DD) to search: ").lower()
        with open(FILE_NAME, "r") as file:
            entries = file.readlines()
            matches = [entry for entry in entries if search_term in entry.lower()]
            if matches:
                print("Matching Entries:")
                print("-" * 30)
                for match in matches:
                    print(match.strip())
                print("-" * 30)
            else:
                print(f"No entries found for the keyword/date: {search_term}")
    else:
        print("No journal file found. Add some entries first!\n")

def delete_all_entries():
    print("\n--- Delete All Entries ---")
    if os.path.exists(FILE_NAME):
        confirmation = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirmation.lower() == "yes":
            os.remove(FILE_NAME)
            print("All entries have been deleted successfully.")
        else:
            print("Operation canceled. No entries were deleted.")
    else:
        print("No journal file found. Nothing to delete.\n")

def main():
    while True:
        print("\n=== Personal Journal Manager ===")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        print()  
        if choice == "1":
            add_new_entry()
        elif choice == "2":
            view_all_entries()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            delete_all_entries()
        elif choice == "5":
            print("Exiting the program. Thank you for using the journal manager!")
            break
        else:
            print("Invalid input! Please select a valid option (1-5).\n")

if __name__ == "__main__":
    main()
