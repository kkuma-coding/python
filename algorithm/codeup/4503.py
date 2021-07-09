"""
https://codeup.kr/problem.php?id=4503
# virus problem

<<<input>>>
7
6
1 2
2 3
1 5
5 2
5 6
4 7

<<<output>>>
4
"""
import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbor = []
    def get_value(self) -> int:
        return self.val
    def get_neighbor(self) -> list:
        return self.neighbor
    def add_neighbor(self, node):
        if not (self.has_neighbor(node)):
            self.neighbor.append(node)
    def has_neighbor(self, node):
        return (node in self.neighbor)

readl = sys.stdin.readline
_N = int(readl())
_P = int(readl())


edge_list = []
for _ in range(_P):
     n1, n2 = map(int, readl().split())
     t1 = tuple((n1, [n2]))
     edge_list.append(t1)

print (edge_list)