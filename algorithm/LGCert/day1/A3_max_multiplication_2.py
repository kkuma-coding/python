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

clist = list()

clist += num
start, end, grow = 0, N, N-1
print(start, end, "diff={}".format(end-start))

while(grow > 0):
    for i in range(start, end-1):
        clist.append(clist[i]*clist[i+1])
    start, end, grow = end, end + grow, grow - 1
    print(start, end, "diff={}".format(end - start))

# print(clist)
clist.sort()
clist.pop()

# 여기서부터 작성

# 출력하는 부분
print(f"{clist.pop():.3f}")