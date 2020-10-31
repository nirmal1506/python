def word_reverse(input_string):
    string_list = input_string.split(" ")
    print("string_list>>>>>>>>", string_list)
    for i in string_list:
        print(i[::-1], end=" ")


def char_interchange(input_string):
    string_list = input_string.split(" ")
    print("string_list>>>>>>>>>>", string_list)

    for i in string_list:
        str_len = len(i)

        for j in range(0, str_len, 2):
            print(i[j:j + 2][::-1], end="")
        print(end=" ")


input_string = input("Enter the string: ")

word_reverse(input_string)

print()

char_interchange(input_string)