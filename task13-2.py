# for dynamic input for student dictionary
student = {}
n = int(input("Enter the no.of students : "))

for i in range(1, n + 1):
    rollno = int(input("Enter rollno  :"))
    name = input("Enter name :")
    marks = int(input("Enter marks :"))

    if 90 < marks <= 100:
        grade = 'A'
    elif 80 < marks <= 90:
        grade = 'B'
    elif 60 < marks <= 80:
        grade = 'C'
    elif 40 < marks <= 60:
        grade = 'D'
    else:
        grade = "FAIL"

    student["s{}".format(i)] = {
        "rollno": rollno,
        "name": name,
        "marks": marks,
        "grade": grade
    }
print(student)