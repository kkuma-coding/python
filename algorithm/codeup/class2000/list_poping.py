my_list = [1,2,3,4,5,6]
my_list = reversed(my_list[1:])
print(*my_list)

print_val = "-123"
print_val = print_val[1:]
print_val = print_val[::-1]
print(print_val)

"""
while my_list:
    print(my_list.pop(), end=", ")
"""