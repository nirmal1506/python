row = int(input("ENTER NUMBER OF ROWS="))
space = 2 * row
col = 1

for i in range(0, row):

    for j in range(0, space):
        print(end=" ")

    for k in range(0, i + 1):
        print(col, end=" ")
        col = col + 1

    space = space - 1

    print()