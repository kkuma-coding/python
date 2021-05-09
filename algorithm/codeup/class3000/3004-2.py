# https://codeup.kr/problem.php?id=3004
'''
5
50 23 54 24 123
-----------------
2 0 3 1 4

https://swblossom.tistory.com/52
첫 번째 int에 입력받은 값이 그대로 기록됩니다.
두 번째 int에 0 1 2 3 4로 입력받은 순서를 기록합니다.

이후 sort함수를 이용하여 올림차순으로 정렬합니다. 정렬이 되었으니
세 번째 int에 차례대로 0 1 2 3 4 재정렬 데이터를 넣습니다.(나중에 출력용)

이후 sort함수를 이용하여 입력받은 순서를 기록한 두 번째 int 값을 올림차순으로 정렬합니다.
순서대로 재정렬데이터를 갖는 세 번째 int 값을 출력합니다.
'''
count = int(input())
data = input().split()

# zip 은 tuple 을 return 함.
zipped = zip ([int(d) for d in data],
              range(len(data)))

mtx = []
for z in zipped:
    mtx.append(list(z))
# print(mtx)

mtx.sort(key=lambda x:x[0])
# print(mtx)

idx = 0
for l in mtx:
    l.append(idx)
    idx+=1
# print(mtx)

mtx.sort(key=lambda x:x[1])
for l in mtx:
    print(l[2], end = " ")


'''
zipped = dict(zip(sorted([int(d) for d in data]), range(len(data))))

sorted_dict = dict(sorted(zipped.items(), key=lambda item: item[0], reverse=False))
for a, b in sorted_dict.items():
    print(a, b)
'''


'''
dec_data_list = [int(d) for d in data]
sorted_dec_data_list = sorted(dec_data_list)

print(sorted_dec_data_list)

for d in dec_data_list:
    print(sorted_dec_data_list.index(d), end=" ")
'''