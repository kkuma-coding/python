# https://codepractice.tistory.com/73
# 이차방정식 (equation)
from sympy import Symbol, solve
x = Symbol ('x')
equation = x ** 2 + 3 * x + 2
print (solve (equation))
# print (solve (equation, dict=True))