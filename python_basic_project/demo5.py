def student_database():
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            city = input("Enter City: ")

            students[roll] = {"name": name, "age": age, "city": city}

        elif choice == "2":
            roll = input("Enter Roll No: ")
            print(students.get(roll, "Student not found"))

        elif choice == "3":
            for roll, details in students.items():
                print(roll, details)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


student_database()