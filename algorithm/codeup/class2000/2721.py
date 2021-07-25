"""
https://codeup.kr/problem.php?id=2721

turtle
error
robot
"""
input_list = []
input_list.append(input())
input_list.append(input())
input_list.append(input())

is_circular = False

a = input_list[0][len(input_list[0])-1]
b = input_list[1][len(input_list[1])-1]
c = input_list[2][len(input_list[2])-1]

if a == input_list[1][0]:
    if b == input_list[2][0]:
        if c == input_list[0][0]:
            is_circular = True

if (is_circular):
    print("good")
else:
    print("bad")