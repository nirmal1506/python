from task22 import fn4

class StudentInfo:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

class StudentMarks:
    def __init__(self, studentInfo_Object, marks1, marks2, marks3):
        self.studentInfo_Object = studentInfo_Object
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        average = (self.marks1 + self.marks2 + self.marks3) // 3

        return average


class Main:
    def __init__(self):
        n = int(input("Enter total number of students:"))

        ls3 = []
        ls4 = []

        for i in range(n):
            rollno = int(input("Enter rollno.:"))
            name = (input("Enter name:"))
            marks1 = int(input("Enter marks1:"))
            marks2 = int(input("Enter marks2:"))
            marks3 = int(input("Enter marks3:"))

            studentInfo_Object = StudentInfo(rollno, name)

            studentMarks_Object = StudentMarks(studentInfo_Object, marks1, marks2, marks3)

            average = studentMarks_Object.average()

            ls3.append([str(rollno), name])

            ls4.append([str(rollno), str(average)])

        print(ls3)

        print(ls4)

        a=fn4(ls3, ls4)
        print(a)


objectMain = Main()