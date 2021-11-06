from functools import reduce

lmd1 = lambda x, y:x+y
list1 = [1,2,3,4,5]
print(reduce(lmd1, list1))

lmd2 = lambda x,y: x*y
print(reduce(lmd2, list1))

lmd3 = lambda x, y: x if x>y else y
list2 = ["abc", "bcd", "efg"]
print(reduce(lmd3, list2))
print(max(list2))
print(min(list2))