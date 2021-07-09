# https://codepro.lge.com/exam/538/sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D-%EC%8B%A4%EC%A0%84-python-_210705/quiz/3
'''
JinYoung Cho - 조진영 님이 모두에게:    오전 9:18
  https://codepro.lge.com/go/assessment/JU5yJ6?sl=true
  여기로 들어가시면 됩니다
  이메일 / 이름 입력하시고..

  for loop 를 중첩해서 사용할 필요가 없다!!
  너무 쓸데 없이 deque 까지 쓰고, list를 두 번, range를 두 번 쓰는 것도 별로다.
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N, S, M = map(int, readl().split())
    return N, S, M

def Solve():
    sol_list = []
    q = deque(list(range(S, N + 1)) + list(range(1, S)))
    for _ in range(N):
        for _ in range(M - 1):
            q.append(q.popleft())
        sol_list.append(q.popleft())
    return sol_list


sol_list = []

# 입력받는 부분
N, S, M = input_data()

# 여기서부터 작성
sol_list = Solve()

# 출력하는 부분
print(*sol_list)