"""
5
1 3 5 6 8
"""
# cnt = int(input())
# num_list = input()

abc_stack = [1, 2, 3, 4, 5]

stack = []

# pop: 꺼내다
# push: 밀어 넣다.
# append: 덧붙이다.
for x in abc_stack:
    stack.append(x)  # stack 의 push()는 python list 에서는, append() 입니다.

# while: ~~ 하는 동안.
# len(): () 안에 들어온 것의 크기, 길이를 계산해 줍니다.
# while len(stack) > 0: # 스택(stack)에 뭔가 쌓인게 있을 때!!! 에만, pop() 해서 꺼내보겠다.
while stack:
    print(stack.pop(), end=" ")