"""
https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/17

<input>
7
2 4 3 2 2 5 1

<output>
8
"""
from collections import deque

count = int(input())
h_list = list(map(int, input().split()))

ans = 0

stack = []
for x in h_list:
    stack.append(x)

for i in range(count):
    if stack:
        able_to_commute = True
        min_ant_h = min(stack[i], stack[-(1+i)])
        for x in stack[i+1:-(1+i)]:
            if x >= min_ant_h:
                able_to_commute = False
                stack.pop()
                break
        if able_to_commute:
            ans += 1
            stack.pop()


print(ans)