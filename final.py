class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks
        self.total_marks = sum(marks)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        percentage = (self.total_marks / 300) * 100
        if percentage >= 90:
            return 'A'
        elif 90>percentage >= 75:
            return 'B'
        elif 75>percentage >= 50:
            return 'C'
        else:
            return 'F'

    def update_marks(self, new_marks):
        self.marks = new_marks
        self.total_marks = sum(new_marks)
        self.grade = self.calculate_grade()

    def display(self):
        return f"Roll Number: {self.roll_number}, Name: {self.name}, Marks: {self.marks}, Total: {self.total_marks}, Grade: {self.grade}"


class ReportCardSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll_number = int(input("Enter Roll Number: "))
        if roll_number in self.students:
            print("Roll number already exists!")
            return
        name = input("Enter Name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return
        marks = []
        for i in range(3):
            mark = int(input(f"Enter Marks for Subject {i+1}: "))
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100!")
                return
            marks.append(mark)
        self.students[roll_number] = Student(roll_number, name, marks)
        print("Student record added successfully!")

    def view_students(self):
        if not self.students:
            print("No records to display!")
            return
        for student in self.students.values():
            print(student.display())

    def update_student(self):
        roll_number = int(input("Enter Roll Number to Update: "))
        if roll_number not in self.students:
            print("Student not found!")
            return
        marks = []
        for i in range(3):
            mark = int(input(f"Enter New Marks for Subject {i+1}: "))
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100!")
                return
            marks.append(mark)
        self.students[roll_number].update_marks(marks)
        print("Student record updated successfully!")

    def delete_student(self):
        roll_number = int(input("Enter Roll Number to Delete: "))
        if roll_number in self.students:
            del self.students[roll_number]
            print("Student record deleted successfully!")
        else:
            print("Student not found!")

    def calculate_grades(self):
        for student in self.students.values():
            print(f"{student.name} (Roll: {student.roll_number}) - Grade: {student.grade}")

    def sort_students(self):
        if not self.students:
            print("No records to sort!")
            return
        criteria = input("Sort by roll_number, name, or total_marks? ").strip().lower()
        if criteria == "roll_number":
            sorted_students = sorted(self.students.values(), key=lambda x: x.roll_number)
        elif criteria == "name":
            sorted_students = sorted(self.students.values(), key=lambda x: x.name)
        elif criteria == "total_marks":
            sorted_students = sorted(self.students.values(), key=lambda x: x.total_marks, reverse=True)
        else:
            print("Invalid sorting criteria!")
            return
        for student in sorted_students:
            print(student.display())

    def generate_summary(self):
        if not self.students:
            print("No records to summarize!")
            return
        total_students = len(self.students)
        highest_marks = max(self.students.values(), key=lambda x: x.total_marks).total_marks
        average_marks = sum(student.total_marks for student in self.students.values()) / total_students
        pass_percentage = (len([s for s in self.students.values() if s.grade != 'F']) / total_students) * 100

        print(f"Total Students: {total_students}")
        print(f"Highest Marks: {highest_marks}")
        print(f"Average Marks: {average_marks:.2f}")
        print(f"Pass Percentage: {pass_percentage:.2f}%")

    def run(self):
        while True:
            print("\nWelcome to the Student Report Card System")
            print("1. Add a new student record")
            print("2. View all student records")
            print("3. Update a record")
            print("4. Delete a student record")
            print("5. Calculate and display grades")
            print("6. Sort student records")
            print("7. Generate summary report")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.calculate_grades()
            elif choice == "6":
                self.sort_students()
            elif choice == "7":
                self.generate_summary()
            elif choice == "8":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
if __name__ == "__main__":
    system = ReportCardSystem()
    system.run()
