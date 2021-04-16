# https://codeup.kr/problem.php?id=1353
# 중첩되는 for loop 가 정보를 전달, 참조과정이 
# 일어나게 된다
# 상위의 loop 가 전달한 값을
# 하위의 loop 가 받아서 동작한다
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()