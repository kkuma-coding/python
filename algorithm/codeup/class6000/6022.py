# https://codeup.kr/problem.php?id=6022
# 6자리 숫자로 이루어진 연월일(YYMMDD)이 입력된다.
# 입력예시: 200304
# 출력예시: 20 03 04
value = input()
print(value[0:2], value[2:4], value[4:6])