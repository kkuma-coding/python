'''
N개의 0또는 양의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아,
그 곱을 출력하는 프로그램을 작성하시오. 예를 들어 아래와 같이 8개의 양의 실수가 주어진다면,

8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4

--> 1.638
'''

import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [float(readl()) for _ in range(N)]
    return N, num

sol = 0.0

# 입력받는 부분
N, num = input_data()
calc = list()

def oper(list_num, len):
    for i in range(len - 1):
        calc.append(list_num[i] * list_num[i + 1])

# calc 에 처음 추가됨
oper(num, N)

#
prev_len = len(calc)
print(1, prev_len)
oper(calc[0:], prev_len)

#
prev_len = len(calc) - prev_len
print(2, prev_len)
oper(calc[prev_len-1:], prev_len)

#
prev_len = len(calc) - prev_len
print(3, prev_len)
oper(calc[prev_len-1:], prev_len)


print(calc)
# 여기서부터 작성

# 출력하는 부분
print(f"{sol:.3f}")