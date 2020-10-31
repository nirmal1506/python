str = "this is string example"

print(str[::-1])

ls = str.split(' ')

print(ls)

print(ls[0][::-1], ls[1][::-1], ls[2][::-1], ls[3][::-1])

print(ls[0][0:2][::-1] + ls[0][2:4][::-1], ls[1][0:2][::-1],
      ls[2][0:2][::-1] + ls[2][2:4][::-1] + ls[2][4:6][::-1],
      ls[3][0:2][::-1] + ls[3][2:4][::-1] + ls[3][4:6][::-1] + ls[3][6])

print("*".join(ls))

print(str.replace(' is', ' was'))
