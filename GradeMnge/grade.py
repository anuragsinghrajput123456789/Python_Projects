# Grade management system


student_grades = {}


# Add a new students
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")


# Update a student grades
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name} with a {grade}")
    else:
        print(f"Student {name} not found")


# Remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Removed {name}")
    else:
        print(f"Student {name} not found")


# List all students
def list_students():
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")


# Search for a student
def search_student(name):
    if name in student_grades:
        print(f"{name}: {student_grades[name]}")
    else:
        print(f"Student {name} not found")


def main():
    while True:
        print("\n Student Grades Management System \n")
        print("1. Add a new student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View all students")
        print("5 . Search for a student")
        print("6. Exit")

        choice = int(input("ENter your choice : "))
        if choice == 1:
            name = input("Enter student name : ")
            grade = input("Enter student grade : ")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name : ")
            grade = input("Enter student grade : ")
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name : ")
            remove_student(name)
        elif choice == 4:
            list_students()
        elif choice == 5:
            name = input("Enter student name : ")
            search_student(name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
