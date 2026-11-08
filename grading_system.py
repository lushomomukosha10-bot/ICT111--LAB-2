students = []

while True:
    print("\n--- Student Grading System ---")
    print("1. Add student")
    print("2. Display all")
    print("3. Class summary")
    print("4. Exit")
    option = input("Choose 1-4: ")

    if option == "1":
        # --- Get student number, reject blank ---
        student_number = input("Enter student number: ")
        if student_number == "":
            print("Student number cannot be blank.")
            continue

        name = input("Enter student name: ")
        if name == "":
            print("Name cannot be blank.")
            continue

        # --- Get mark, keep asking until valid ---
        
        while True:
            mark_input = input("Enter mark (0-100): ")
            try:
                mark = float(mark_input)
            except ValueError:
                print("Invalid mark. Enter a number.")
                continue

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.")
                continue
            break

        
    
        if mark >= 80:
            grade = "A"
            decision = "Excellent"
        elif mark >= 70:
            grade = "B"
            decision = "Very good"
        elif mark >= 60:
            grade = "C"
            decision = "Good"
        elif mark >= 50:
            grade = "D"
            decision = "Pass"
        else:
            grade = "F"
            decision = "Fail"

        
        student = {
            "student_number": student_number,
            "name": name,
            "mark": mark,
            "grade": grade,
            "decision": decision
        }
        students.append(student)
        print(f"Added: {name} - Mark: {mark} - Grade: {grade} - {decision}")

    elif option == "2":
        if len(students) == 0:
            print("No students yet. Add a student first.")
        else:
            print("\n--- All Students ---")
            
            for student in students:
                print(f"{student['student_number']} | {student['name']} | Mark: {student['mark']} | Grade: {student['grade']} | {student['decision']}")

    elif option == "3":
        if len(students) == 0:
            print("No students yet. Cannot calculate summary.")
        else:
            total = 0
            highest = students[0]["mark"]
            lowest = students[0]["mark"]
            passes = 0
            fails = 0

            for student in students:
                mark = student["mark"]
                total = total + mark
                if mark > highest:
                    highest = mark
                if mark < lowest:
                    lowest = mark
                if mark >= 50:
                    passes = passes + 1
                else:
                    fails = fails + 1

            average = total / len(students)
            print("\n--- Class Summary ---")
            print(f"Total students: {len(students)}")
            print(f"Class average: {average:.2f}")
            print(f"Highest mark: {highest}")
            print(f"Lowest mark: {lowest}")
            print(f"Passes: {passes}")
            print(f"Fails: {fails}")

    elif option == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose 1-4.")