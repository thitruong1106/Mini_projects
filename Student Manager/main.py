from students import add_student, list_student, search_students
STUDENT_FILE = 'students.json'

def display_menu(): 
    print("=========== Student manager ============")
    print("\n")
    print("1. Add student")
    print("2. List Student")
    print("3. Search student")
    print("4. Quit'")

while True: 
    try: 
        display_menu()
        choice = input("Choose 1-4")
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            added = add_student(STUDENT_FILE, name, age, grade)
            if added: 
                print("Student Added successfully")
            else: 
                print("Could not add students, please check inputs")
        elif choice == "2":
            list_student(STUDENT_FILE) 
        elif choice == "3":
            query = input("Who do you want to search for: ")
            search_students(STUDENT_FILE, query)
        elif choice == "4":
            print("Thank you for user the program, Goodbye")
            break
        else:
            print("Invalid input, type 1-4")
            continue
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break