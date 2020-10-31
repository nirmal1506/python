student = {}
stu = int(input("Enter no of students: "))
for i in range(1, stu+1):
    RollNo = int(input("Enter The RollNo: "))
    Name = input("Enter The Name:")
    Marks = int(input("Enter The Marks: "))

    student["RollNo{}".format(i)] = RollNo
    student["Name{}".format(i)] = Name
    student["Marks{}".format(i)] = Marks
print(student)
print()

print(" Enter 1 For RollNo \n Enter 2 For Name \n Enter 3 For Marks \n Enter 4 for exit")
choice = int(input("Enter Your Choice:- "))
if choice == 1:
        print("RollNo is:")
        for i in range(0, stu):
            print(student["RollNo{}".format(i)])

elif choice == 2:
        print("Name is:")
        for i in range(0, stu):
            print(student["Name{}".format(i)])

elif choice == 3:
        print("Marks is:")
        for i in range(0, stu):
            print(student["Marks{}".format(i)])
else:
        exit()



