# https://codeup.kr/problem.php?id=1273
'''
약수 구하기
자연수 N이 입력된다.( 1 <= N <= 10,000 )
N의 약수를 오름차순으로 출력한다.
'''
output = "1 "
value = int(input())
for mod in range(2, value+1):
    if (value % mod == 0):
        output += "{} ".format(mod)
print(output)