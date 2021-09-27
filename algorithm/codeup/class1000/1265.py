# 구구단 체험하기 codeup.kr/problem.php?id=1265
# 2021.5.15
num = int(input())

for mul in range(1, 10):
    print("{}*{}={}".format(num, mul, num*mul))