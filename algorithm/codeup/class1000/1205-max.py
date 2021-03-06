# https://codeup.kr/problem.php?id=1205
'''
1+2 = 3   , 2+1 = 3
1 - 2 = -1,   2 - 1 = 1
1 * 2 = 2,    2 * 1 = 2

1 / 2 = 0.5,   2 / 1 = 2

12=1 ,   21 = 2
print(pow(3,2))
print(pow(2,1))
'''
calc_list = []
a, b = input().split()
a, b = int(a), int(b)
calc_list.append(a+b)
calc_list.append(a-b)
calc_list.append(b-a)
calc_list.append(a*b)
calc_list.append(a/b)
calc_list.append(b/a)
calc_list.append(pow(a, b))
calc_list.append(pow(b, a))
# print (calc_list)
print ("{:.06f}".format(max(calc_list)))