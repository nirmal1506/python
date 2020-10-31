student={
    's1':{'rollno':int(input("Enter rollno:")),
          'name':input("Enter name:"),
          'marks':int(input("Enter marks:")),
          'grade':None},
    's2':{'rollno':int(input("Enter rollno:")),
          'name':input("Enter name:"),
          'marks':int(input("Enter marks:")),
          'grade':None},
    's3':{'rollno':int(input("Enter rollno:")),
          'name':input("Enter name:"),
          'marks':int(input("Enter marks:")),
          'grade':None},
    's4':{'rollno':int(input("Enter rollno:")),
          'name':input("Enter name:"),
          'marks':int(input("Enter marks:")),
          'grade':None},
    's5':{'rollno':int(input("Enter rollno:")),
          'name':input("Enter name:"),
          'marks':int(input("Enter marks:")),
          'grade':None}
}

stu = list(student.keys())

for i in stu:
    if 90 < student[i]["marks"] <= 100:
        student[i]["grade"] = 'A'
    elif 80 < student[i]["marks"] <= 90:
        student[i]["grade"] = 'B'
    elif 60 < student[i]["marks"] <= 80:
        student[i]["grade"] = 'C'
    elif 40 < student[i]["marks"] <= 60:
        student[i]["grade"] = 'D'
    else:
        student[i]["grade"] = 'Fail'

print(student)