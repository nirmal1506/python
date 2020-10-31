def f1(row, col):
    for i in range(0, row):

        for j in range(row, i, -1):
            print(end=" ")

        for k in range(0, i + 1):
            print(col, end=" ")

        print()


f1(int(input("Enter no.of rows: ")), input("Enter symbol: "))