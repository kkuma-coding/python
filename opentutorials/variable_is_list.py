list1 = [1, 2, 3]
list2 = list1

print("list1 == list2 :", list1 is list2)
print(id(list1))
print(id(list2))

list3 = list1.copy()

print("1 == 3", list1 is list3)
print("2 == 3", list2 is list3)