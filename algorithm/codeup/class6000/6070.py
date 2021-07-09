"""
https://codeup.kr/problem.php?id=6070
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
"""
m = int(input())

if (m in [12, 1, 2]):
    print("winter")
elif (m in [3, 4, 5]):
    print("spring")
elif (m in [6, 7, 8]):
    print("summer")
elif (m in [9, 10, 11]):
    print("fall")