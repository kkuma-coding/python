# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
3
041
253
620
"""
from heapq import *
import sys
from collections import deque
readl = sys.stdin.readline

origin_map = []
calc_map = []
INF = 987654321

count = int(readl())

for _ in range(count):
	line = readl().strip()
	origin_map.append([int(x) for x in line])

calc_map = origin_map.copy()
for i in range(count):
	for j in range(count):
		calc_map[i][j] = INF

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
q.append((0, 0))
while q:
	r, c = q.pop()
	if calc_map[r][c] == INF:
		print(f"[00] calc_map[{r}][{c}] = {calc_map[r][c]}, origin_map[{r}][{c}]={origin_map[r][c]}")
		calc_map[r][c] = origin_map[r][c]
		print(f"[00] calc_map[{r}][{c}] = {calc_map[r][c]}, origin_map[{r}][{c}]={origin_map[r][c]}")
	else:
		print(f"[01] calc_map[{r}][{c}] = {calc_map[r][c]}, origin_map[{r}][{c}]={origin_map[r][c]}")
		calc_map[r][c] = min(calc_map[r][c], origin_map[r][c] + calc_map[r][c])

	for dr, dc in direction:
		rr, cc = dr + r, dc + c
		if rr < 0 or cc < 0 or rr > count or cc > count: continue
		q.append((rr, cc))

print(calc_map[count-1][count-1])

# for l in calc_map:
# 	print(*l)