a = int(input("Enter The No of Rows:-"))
for i in range(1,a):
    for j in range(a,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
            print(" *",end="")
    print()
for i in range(a,0,-1):
    for j in range(i,a):
        print(" ",end="")
    for k in range(1,i+1):
            print(" *",end="")
    print()