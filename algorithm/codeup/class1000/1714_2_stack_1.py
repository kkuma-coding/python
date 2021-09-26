# pop()   stack 에서 꺼내는 것.
# push()  stack 에 집어 넣는 것.

# list.pop() list 에 집어 넣는 것
# list.append() list 에 집어 넣는 것 = stack에서 push와 같습니다.

val = input()
my_stack = [] # my_stack 은 python 의 list 입니다.
              # 단, stack 처럼 사용할 것입니다

for x in val:
    my_stack.append(x) # push

# while len(my_stack) > 0:
while my_stack:
    print(my_stack.pop(), end="")
print()