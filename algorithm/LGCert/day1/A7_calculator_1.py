'''
첫 줄에 정수의 개수 N이 입력으로 주어진다.
둘째 줄에는 N개의 정수 M과 연산자로 구성 된 수식이 주어진다.
정수와 연산자 사이에는 공백이 하나 주어진다.
(1≤ N ≤20, 1≤ M ≤10 , 연산자 - +, -, *, / )

입력 예시

4
1 - 4 * 9 + 10

--> -25
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	str_exp = readl().split()
	nums = list(map(int,str_exp[0::2]))
	op = str_exp[1::2]
	return N, nums, op

# 입력받는 부분
N, nums, op = Input_Data()

# 여기서부터 작성
# print(N, nums, op)

stack = []
stack.append(nums[0])
for n, o in zip(nums[1:], op):
    if (o == '+'):
        stack.append(n)
    elif(o == '-'):
        stack.append(-n)
    elif(o == '*'):
        stack.append(stack.pop()*n)
    elif(o == '/'):
        stack.append(int(stack.pop()/n)) # ** important

sum = 0
while(len(stack)):  # good
    sum += stack.pop()

# 출력하는 부분
print(sum)