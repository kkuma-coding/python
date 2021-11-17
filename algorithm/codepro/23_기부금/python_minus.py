from functools import reduce

lambda_add = lambda x, y: x+y

x=1
data = [3-x, 4-x, 5-x, 6-x]

data2 = reduce(lambda_add, data, 0)

print(data2)


print(all ([1,1,1,1,1,1,1]))
print(all ([1,1,1,1,1,0,1]))
print(all ([]))


my_list = list(range(10))
print(my_list)

filtered_list = [i for i in range(10) if i % 2 == 1]
print(filtered_list)


