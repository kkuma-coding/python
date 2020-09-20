# https://codepractice.tistory.com/73
# 실근을 갖지 않는 이차방정식 (equation)
from sympy import Symbol, solve
x = Symbol ('x')
equation = x ** 2 + x + 1
print (solve (equation, dict=True))