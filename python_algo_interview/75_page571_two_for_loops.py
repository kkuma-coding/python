"""
leetcode time limit exceeded at 2021.9.27
testcase 가 강화되어 pass 하지 못하는 것
57/61 에서 막힌다
"""
from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

q = deque()

maxv = float('-inf')
for i in range(len(nums)-k+1):
    maxv = float('-inf')
    for x in nums[i:i+k]:
        if x > maxv:
            maxv = x
    print(maxv)