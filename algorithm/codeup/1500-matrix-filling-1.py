# https://codeup.kr/problem.php?id=1500
# 별로 풀어볼 가치가 없는 문제로 보인다.
# 입력
# 2 3
# 1 2 3
# 4 5 6

'''
2 3
1 2 3
4 5 6
'''

m, n = input().split()
m, n = int(m), int(n)

data = [] # python list를 하나 준비한다.
for row in range(0, m):
    data.append(input()) # 리스트에 input() 결과 내용을 한 줄 씩 저장한다. list.append()

for line in data:
    print (line)