# Student Record Manager using Dictionary

students = {}

while True:
    choice = input("\n1. Add Student\n2. Get Grade\n3. Update Grade\n4. Exit\nChoose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added!")

    elif choice == "2":
        name = input("Enter student name: ")
        print(f"Grade: {students.get(name, 'Not found')}")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            students[name] = input("Enter new grade: ")
            print("Grade updated!")
        else:
            print("Student not found!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")