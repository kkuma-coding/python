# https://codepractice.tistory.com/73
# 근의 공식
from sympy import Symbol, symbols, solve
x=Symbol('x')
a, b, c = symbols ('a, b, c')
equation = a * x ** 2 + b * x + c
print (solve (equation, x, dict=True))

# [{x: (-b + sqrt(-4*a*c + b**2))/(2*a)}, {x: -(b + sqrt(-4*a*c + b**2))/(2*a)}]