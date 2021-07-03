# https://codeup.kr/problem.php?id=1271
"""
첫째줄에 정수의 개수 N이 주어진다. (n<=1000)

둘째줄에 N개의 정수가 공백으로 분리되어 주어진다.  ( 0 <= 각각의 데이터 <=1000000 )

N개의 정수 중 최대값을 찾아 출력한다.

<입력예시>
5
3 1 29 31 21

<출력예시>
31
"""
num = int(input())
value = input()

val_list = [int(d) for d in value.split()]
# print(val_list)

# val_list.sort(key=lambda x:x[0])
val_list.sort(key=None)
# print(val_list)

end_of_list = val_list.pop()
print(end_of_list)