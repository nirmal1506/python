# Author=>Nirmal Mehta
# Created Date=>24-09-2020
# Updated Date=>28-09-2020
# Program=>file task write data in a file then
#          reverse write the data in another file & replace it
# pep 8=>python coding standard

# demo.txt and dummy.txt open in w+ mode
demo_file = open("demo.txt", "w+")
dummy_file = open("dummy.txt", "w+")
# user will input no of lines to write
n_lines = int(input("Enter No. Of Lines="))


# writelines=>list data write
# readlines=>data read it will return in list format
# readline=>single line read in string format
# writeline=>deprecated in python3 only supported in python2

# write_data function definition to write data in demo.txt
def write_data(n_lines):
    data_list = []
    for i in range(n_lines):
        data = input("Enter Data=")
        data_list.append(data + "\n")

    print("data_list>>>>>>>>>>>>>>>>>>", data_list)

    demo_file.writelines(data_list)


# reverse_data function definition to read data from demo.txt and
#  reverse write in dummy.txt
def reverse_data():
    # demo_file cursor reposition
    demo_file.seek(0, 0)
    data_list = demo_file.readlines()
    data_list.reverse()
    print(data_list)
    dummy_file.writelines(data_list)


# replace_data function definition to replace the data in dummy.txt
def replace_data():
    dummy_file.seek(0, 0)
    dummy_data = dummy_file.read()
    print('dummy_data>>>>\n', dummy_data)
    old_string = input('Enter string which you want to replace=')
    new_string = input('Enter replace String=')
    dummy_file.seek(0, 0)
    replace_data = dummy_data.replace(old_string, new_string)
    dummy_file.write(replace_data)


# write_data function call
write_data(n_lines)
# reverse_data function call
reverse_data()
# replace_data function call
replace_data()
# demo.txt and dummy.txt file close
demo_file.close()
dummy_file.close()