"""
https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/17

<input>
7
2 4 3 2 2 5 1

<output>
8
"""
import sys
readl = sys.stdin.readline
count = int(input())
h_list = list(map(int, readl().split()))

ans = 0
stack = [x for x in h_list]

low_antena = 987654321
for i in range(count):
    found = False

    if stack:
        if h_list[i] < stack[-1]:
            low_antena = h_list[i]
        elif h_list[i] >= stack[-1]:
            low_antena = stack[-1]

        # print(h_list[i], stack[-1], stack[i + 1:-1])

        for x in stack[i + 1:-1]:
            # print("--looping")
            if low_antena <= x:
                found = True
                stack.pop()
                break


    if found:
        ans += 1

print(ans + (count-1))