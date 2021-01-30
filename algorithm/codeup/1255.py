# https://codeup.kr/problem.php?id=1255
'''
a, b = 2.00, 2.03
step = 0.01
for value in range(a, b+step, step):
    print (value, " ")
'''
a, b = input().split()

a = float(a)*100
b = float(b)*100

a = round(a, 2)
b = round(b, 2)

for value in range(int(a), int(b+1)):
    print("{:0.2f}".format(value/100), end=" ")


# a = int(100 * a)
# b = int(100 * b)
# print(a, b)
'''
for value in range(a, b):
    print(value)
'''