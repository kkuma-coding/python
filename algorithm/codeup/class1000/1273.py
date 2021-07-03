"""
https://codeup.kr/problem.php?id=1273
자연수 N이 주어지면 N의 약수를 오름차순으로 모두 출력하시오.

6
1, 2, 3, 6
"""

n = 6
for i in range(1, n+1): # range: 범위
    if (i == 4):
        continue
    if (i == 5):
        continue
    print(i)