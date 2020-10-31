def fun(*args):
    print(args)

    temp=[]

    ls=[]

    for j in args:
        temp.append(j)

    print(temp)

    if len(temp)==1:

        for k in range(len(temp)):
            ls.extend(temp[k])

        print('Final List:',ls)

    if len(temp) == 2:

        for k in range(len(temp)):
            ls.extend(temp[k])

        ls.sort()
        print("Final Sorted List", ls)

    if len(temp)==3:

        for k in range(len(temp)):
            ls.extend(temp[k])

        ls.sort()
        print("Final Sorted List", ls)

        print('minimum:',min(ls))
        print('maximum:', max(ls))
        print('final sorted list:',ls)


n = int(input("Enter how many list:"))
if n == 1:
    ele=int(input('how many elements for list1:'))

    l1=[]
    print('Enter Elements for List 1:')

    for i in range(ele):
        l1.append(int(input()))

    fun(l1)

elif n == 2:

    print('How many elements you want in List 1 ?')

    el1 = int(input())

    print('How many elements you want in List 2 ?')

    el2 = int(input())

    li1 = []

    li2 = []

    print('Enter Elements for List 1:')

    for i in range(el1):
        li1.append(int(input()))

    print('Enter Elements for List 2: ')

    for j in range(el2):
        li2.append(int(input()))

    fun(li1, li2)

elif n == 3:

    print('How many elements you want in List 1 ?')

    el1 = int(input())

    print('How many elements you want in list 2 ?')

    el2 = int(input())

    print('How many elements you want in list 3 ?')

    el3 = int(input())

    li1 = []

    li2 = []

    li3 = []

    print('Enter Elements for List 1:')

    for i in range(el1):
        li1.append(int(input()))

    print('Enter Elements for List 2:')

    for j in range(el2):
        li2.append(int(input()))

    print('Enter Elements for List 3:')

    for k in range(el3):
        li3.append(int(input()))

    fun(li1, li2, li3)

else:
    print("ERROR!PRESS ANY FROM 1,2 & 3")
    exit()