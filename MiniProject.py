#Count the Number of Student

numofStudents = int(input("Enter Total Students:"))


#Data Storage

studentData = []

#inserting data

for i in range(numofStudents):
    print(f"Enter the Data of Student {i+1}")
    name = input("Name: ")
    roll_no = int(input("Roll Number: "))
    marks = int(input("Marks: "))

    if marks > 95:
        grades = "A"
    elif marks > 80:
        grades = "B"
    elif marks > 60:
        grades = "C"
    elif marks >= 33:
        grades = "D"
    else:
        grades = "F"

    students = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grades": grades
    }

    studentData.append(students)

#Data Printing
print("\n All Students Data: ")

for s in studentData:
    print(f"{s['name']} - Roll Number: {s['roll_no']}- Marks: {s['marks']} - Grades: {s['grades']}")


#Passed Students
print("\n Student Who are Passed: ")

for s in studentData:
    if s['marks'] >= 33:
        print(f"{s['name']} - Marks: {s['marks']}") 
