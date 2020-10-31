f1 = open("abc.txt","w+")

def a(f1):
    n = int(input("Enter Number of Line:-"))
    for i in range(0,n):
        f1.write(input("Enter Data:-"))
        f1.write("\n")

def b(f1):
    line=0
    word=0
    without_space_char=0
    f1.seek(0)
    str=f1.read()
    print(str)
    with_space_char=len(str)
    print("with_space_char>>>",with_space_char)

    for i in str:

        if i == " ":
            word=word+1

        elif i=="\n":
            line=line+1
            word=word+1

        else:
            without_space_char=without_space_char+1

    print("Line>>>",line)
    print("Word>>>",word)
    print("without_space_char>>>",without_space_char)



a(f1)
b(f1)

f1.close()