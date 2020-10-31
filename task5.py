row = int(input("ENTER NUMBER OF ROWS="))
col = '*'

for i in range(row, 0, -1):

    for j in range(0, i):
        print(col, end=" ")

    print()

