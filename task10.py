ls=[1,2,3,['a','b'],4,5,6,['d','e','f'],'g',7,8,[9,10,'i','j'],'aansh']
print(ls)
for i in range(0,len(ls)):
    if type(ls[i]) == int:
        print(ls[i])
    elif type(ls[i])== str:
        print("   "+ls[i])
    else:
        for j in range(0,len(ls[i])):
            if type(ls[i][j])==int:
                print(ls[i][j])
            else:
                print("   "+ls[i][j])
