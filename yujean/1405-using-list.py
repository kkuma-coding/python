my_list = [1,2,3,4,5]

# stack : push, pop
# stack 동작을 python 의 list 로 구현함.
def sol1():
    global my_list
    for x in range(4):
        temp = my_list.pop(0) # pop() 은 지우면서, 지운 그 값을 알려줘요
        my_list.append(temp)
        print(*my_list)

def sol2():
    global my_list
    for x in range(len(my_list)):
        my_list.append(my_list.pop(0)) # 1 줄로 구현한 것.
        print(*my_list)

sol2()