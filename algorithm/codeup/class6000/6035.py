# https://codeup.kr/problem.php?id=6035
# 2개의 실수가 공백으로 구분되어 입력된다.

# 첫 번째 실수와 두 번째 실수를 곱한 값을 출력한다.
#
# 입력 예시: 0.5 2.0
# 출력 예시: 1.0

a, b = input().split()
a, b = float(a), float(b)
print(a * b)