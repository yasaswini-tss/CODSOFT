students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Student Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\n----- STUDENT RECORDS -----")
    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print("-" * 30)

def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            return

    print("Student not found.")

def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["marks"] = float(input("Enter New Marks: "))
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def calculate_grade():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            marks = student["marks"]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            else:
                grade = "Fail"

            print(f"\nStudent Name: {student['name']}")
            print(f"Marks: {marks}")
            print(f"Grade: {grade}")
            return

    print("Student not found.")

while True:

    print("\n" + "=" * 40)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Grade")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_grade()

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")