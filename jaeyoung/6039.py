# [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)
# https://codeup.kr/problem.php?id=6039

# 4.0 2.0
a, b = input().split()
a, b = float(a), float(b)
# float: 둥둥 떠다니다. 4.0 0.0000004 40000000.0
# print (a ** b)
print(pow(a, b))