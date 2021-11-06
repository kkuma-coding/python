"""
<input>
5
2 52 23 55 100
4
5 2 55 99

<output>
0 1 1 0
"""
import sys
readl = sys.stdin.readline


exist_count = int(input())
exist_values = readl().split()

q_count = int(input())
q_values = readl().split()

for q in q_values:
    if q in exist_values:
        print(1, end=" ")
        continue
    print(0, end=" ")