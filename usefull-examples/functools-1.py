from functools import reduce

list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = list(map((lambda x : x*2), list1))
print(result1)

result2 = reduce((lambda x, y: x*y), list1)
print(result2)