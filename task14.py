li  = []
li1 = []
li2 = []
n = int(input("Enter the no.of elements: "))
for i in range(1,n+1):
    n1 = int(input("Enter element: "))
    li.append(n1)

li.sort(reverse=True)
print(li)

sum1 = sum(li)
print("The sum of list: ",sum1)


if divmod(sum1,2)[1] != 0:
    print("Not possible")
else:
    for j in range(0,len(li)):
        if sum(li1)<sum(li2):
            li1.append(li[j])

        else:
            li2.append(li[j])


if sum(li1) == sum(li2):
    print("li1  :",li1)
    print("li2  :",li2)
else:
    print("--Not Possible--")






