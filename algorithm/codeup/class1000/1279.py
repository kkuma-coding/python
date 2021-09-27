a, b = map(int, input().split())
# print(a, b)
number_list = []
for i in range(a, b+1):
    if ( i % 2 != 0 ):
        number_list.append(i)
    else:
        number_list.append(-i)

print(sum(number_list))