# https://codepractice.tistory.com/73
# 일차방정식 (equation)
from sympy import Symbol, solve
x = Symbol ('x')
equation = 2 * x - 6
print (solve (equation))