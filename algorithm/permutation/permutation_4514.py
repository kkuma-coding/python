import itertools

nums_str = ""
count = 8

for x in range(count):
    nums_str += str(x)


print(list(itertools.combinations(nums_str, 2)))
