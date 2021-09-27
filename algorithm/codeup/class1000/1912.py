"""
https://codeup.kr/problem.php?id=1912

n! 의 값을 출력한다.

"""

val = int(input())

def mul(n):
    if (n <= 1):
        return 1
    return n * mul(n-1)

print(mul(val))