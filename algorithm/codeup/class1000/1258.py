# https://codeup.kr/problem.php?id=1258
'''
정수 n이 입력으로 들어오면 1부터 n까지의 합을 구하시오.
'''
sum = 0
val = int(input())
for n in range(1, val+1):
    sum += n
print(sum)