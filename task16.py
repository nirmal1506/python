# ->create two lists

# ->user will input no. of elements for both lists

# ->user will input elements for both lists

# list convert number

# number convert list

# ls1=[1,2,3,4]=>1234


# ls2=[1,2,3,4]=>1234


# addition=>2468[2,4,6,8]

# multiplication=>1522756=>[1,5,2,2,7,5,6]
ls1 = []
n1 = int(input("Enter no.of elements: "))

for i in range(0, n1):
    ls1.append(int(input("Enter element: ")))

ls2 = []
n = int(input("Enter no.of elements: "))

for j in range(0, n):
    ls2.append(int(input("Enter element: ")))

print(ls1)
print(ls2)

s1 = int("".join(map(str, ls1)))
print(s1)
s2 = int("".join(map(str, ls2)))
print(s2)

a = s1 + s2
print("Addition is : ", a)

b = s1 * s2
print("Multiplication is : ", b)
li = list(map(int, list(str(b))))
print("Multiplication in  List:-", li)

temp = []
while (s1 != 0 or s2 != 0):
    t1 = s1 % 10
    t2 = s2 % 10
    if s1 == 0:
        t1 = 0
    if s2 == 0:
        t2 = 0
    temp.append(t1 + t2)
    s1 = s1 // 10
    s2 = s2 // 10
temp.reverse()
print(temp)
