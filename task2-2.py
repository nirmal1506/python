#

x = float(input("enter your number : "))

print(x)
if x > 0:
    if x % 2 == 0:
        print(x*2.5)
    else:
        print(2+x)
else:
    if x % 2 == 0:
        print(x/2.5)
    else:
        print(x - 5)
