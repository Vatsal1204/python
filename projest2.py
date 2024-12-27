# Student Data Organizer
students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists. Try again.")
        return
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    subjects = input("Enter Subjects (comma-separated): ").split(',')
    students[student_id] = {
        "Name": name,
        "Age": age,
        "Grade": grade,
        "DOB": dob,
        "Subjects": [subject.strip() for subject in subjects]
    }
    print("Student added successfully!")

def display_all_students():
    if not students:
        print("No students available.")
        return
    print("--- Display All Students ---")
    for student_id, details in students.items():
        subjects = ", ".join(details["Subjects"])
        print(f"Student ID: {student_id} | Name: {details['Name']} | Age: {details['Age']} | "
              f"Grade: {details['Grade']} | Subjects: {subjects}")

def update_student_info():
    student_id = input("Enter Student ID to update: ")
    if student_id not in students:
        print("Student not found!")
        return
    print("Updating details for:", students[student_id]["Name"])
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    subjects = input("Enter Subjects (comma-separated): ").split(',')
    students[student_id] = {
        "Name": name,
        "Age": age,
        "Grade": grade,
        "DOB": dob,
        "Subjects": [subject.strip() for subject in subjects]
    }
    print("Student updated successfully!")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def display_subjects_offered():
    all_subjects = set()
    for student in students.values():
        all_subjects.update(student["Subjects"])
    print("Subjects offered:", ", ".join(all_subjects))

def main():
    while True:
        print("\nWelcome to the Student Data Organizer!")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            update_student_info()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_subjects_offered()
        elif choice == '6':
            print("Thank you for using the Student Data Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
