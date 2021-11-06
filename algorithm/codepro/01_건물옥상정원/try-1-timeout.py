"""
1) 메모리에 input 값을 모두 넣어둔다는 것
2) 메모리에 적재한 input list 제일 뒤에서부터 알고리즘 돌려보겠다는 것
"""
from collections import deque

count = int(input())
h_list = []
for _ in range(count):
    h_list.append(int(input()))

Q = deque()
ans = 0
for h in h_list[::-1]:
    if Q:
        for comp_h in Q:
            if h > comp_h:
                ans += 1
            else:
                break
        Q.appendleft(h) ## this code was so important. but timeout after 6th testcases

    if not Q:
        Q.appendleft(h)


print(ans)