l = []
n = int(input("Enter the no.of elements: "))
for i in range(1, n + 1):
    l.append(int(input("Enter the Value of List: ")))
print(l)
a = []
b = []
b.append(l[0])

for j in range(1, len(l)):
    if l[j] > b[-1]:
        b.append(l[j])
    else:
        a.append(b)
        b = [l[j]]
a.append(b)
print("Sublist:-", a)

max = 0
for i in (a):
    if len(i) > max:
        max = len(i)
print("Max length: ", max)

temp = []
for i in (a):
    if len(i) == max:
        if i not in temp:
            print("Maximum increasing Sublist: ", i)
            temp.append(i)
