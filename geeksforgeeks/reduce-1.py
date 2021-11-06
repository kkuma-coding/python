from functools import reduce

def try1():
    list1 = [2, 4, 7, 9, 1, 3]
    sum_of_list1 = reduce((lambda x, y: x+y), list1)
    print(sum_of_list1)

def try2():
    list2 = ["abc", "xyz", "def"]
    max_of_list2 = reduce((lambda x, y: x if x>y else y), list2)
    print(max_of_list2)

