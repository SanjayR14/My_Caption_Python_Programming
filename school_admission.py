import csv

def add_student(file_name, name, student_id, courses, grades):
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, student_id, courses, grades])

def get_student(file_name, student_id):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == student_id:
                return row
    return None

def update_student(file_name, student_id, courses, grades):
    students = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == student_id:
                row[2] = courses
                row[3] = grades
            students.append(row)
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)

def delete_student(file_name, student_id):
    students = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] != student_id:
                students.append(row)
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)

add_student("students.csv", "John Doe", "12345", "Math,Science,History", "A,B,C")
student = get_student("students.csv", "12345")
print(student)
update_student("students.csv", "12345", "Math,Science,English", "A,A,B")
student = get_student("students.csv", "12345")
print(student) 
delete_student("students.csv", "12345")
student = get_student("students.csv", "12345")
print(student) 