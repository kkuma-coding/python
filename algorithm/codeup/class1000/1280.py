"""
입력 예시
5 7

출력 예시
+5-6+7=6
"""
a, b = map(int, input().split())
# print(a, b)
number_list = []
for i in range(a, b+1):
    if ( i % 2 != 0 ):
        number_list.append(i)
    else:
        number_list.append(-i)

for x in number_list:
    if (x > 0):
        print("+{}".format(x), end="")
    else:
        print("{}".format(x), end="")
print("=", end="")
print(sum(number_list))
