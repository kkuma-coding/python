'''
https://codeup.kr/problem.php?id=2102

자연수 N이 입력될 때, 0과 1로 이루어진 N의 배수 중 가장 작은 자연수를 출력하시오.

<<<입력>>>
자연수 N이 입력된다(N<2의 64승)

<<<출력>>>
0과 1로 이루어진 N의 배수 중 가장 작은 자연수를 출력한다.
이때 출력되는 자연수의 맨 앞자리는 1이어야 한다.
조건을 만족하는 자연수가 unsigned long long형의 범위에 없을 경우 0을 출력한다.

<<<입력 예시>>>
3

<<<출력 예시>>>
111
'''

val = int(input())


mul = 1
mul_bin_str = ""
mul_int = 0

while 1:
    mul_bin_str = "{:b}".format(mul)
    if (len(mul_bin_str) > 20):
        print(0)
        break

    mul_int = int(mul_bin_str)
    if (mul_int % val == 0 and mul_bin_str[0] == '1'):
        print(mul_bin_str)
        break

    mul += 1
