"""
점수가 가장 높은 학생의 ID 3개를 순서대로 출력한다
만일 점수가 같은 경우는 ID가 작은 학생을 선택한다

입력예시
8
70 30 70 40 60 50 90 80

출력 예시
7 8 1
"""
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	score = map(int,readl().split())
	info = list(enumerate(score, 1))
	return N, info

# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
# print(N, info)
info.sort(key=lambda x:x[1], reverse=True)

out = []
count = 3
for id, score in info:
    if (0 >= count):
        break
    out.append(id)
    count -= 1
# 출력하는 부분
print(*out)