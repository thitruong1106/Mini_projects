from helpers import save_student, load_students

def add_student(path, name, age, grade):
    #Validate name is not empty 
    if not name or not name.strip(): 
        return False 
    #validate age 
    try: 
        age = int(age)
        if age <= 0: 
            return False 
    except (ValueError, TypeError):
        return False
    #Validate Grade 
    valid_grade = ['A','B','C','D','E','F']
    if grade.upper() not in valid_grade: 
        return False
    
    #Load current students, update and save
    students = load_students(path)
    new_student = {
        "name": name.strip(),
        "age": age, 
        "grade": grade.upper()
    }
    #append new students to loaded students 
    students.append(new_student)
    save_student(path, students)
    return True

def list_student(path):
    students = load_students(path)
    if not students: 
        print("No students in list yet")
        return []
    print("\n ----- Students ----- ")
    for index, s in enumerate(students, start=1):
        print(f"{index}. {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

    return students

def search_students(path, query): 
    students = load_students(path) #load current students 
    search_result = []
    for student in students: #for each student in student 
        if query.lower() in student['name'].lower(): #"al" matches “Alice”
            search_result.append(student) #append the specific student to searched results 
    if not search_result: 
        print("No matches found")
    else:
        print("Search results")
        for s in search_result: 
            print(f"{s['name']} | Age: {s['age']} | Grade: {s['grade']}")
    return search_result
        
