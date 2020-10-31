a=[1, 'a', 2, 'b', 3, 4, 55, 'nirmal', 'aakash']
print(a)
str_list=[]
int_list=[]

for i in range(0,len(a)):
    if type(a[i]) == str:
        str_list.append(a[i])

    elif type(a[i]) == int:
        int_list.append(a[i])

    else:
        exit()

print("Integer List: ",int_list)
print(max(int_list))
print(min(int_list))

print("String List: ",str_list)
str_list.reverse()
print("Reversed String list: ",str_list)