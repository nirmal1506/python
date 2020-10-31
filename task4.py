#1
#2 3
#4 5 6
#7 8 9 10

row = int(input("ENTER NUMBER OF ROWS="))
col = 1

for i in range(0, row):

    for j in range(0, i + 1):

        print(col, end=" ")

        col = col + 1

    print()