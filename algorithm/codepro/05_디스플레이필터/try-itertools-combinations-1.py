from itertools import combinations
from itertools import permutations

# print(list(itertools.combinations([1, 2, 3], 1)))
for iter in combinations([1,2,3],1):
    print(len(iter))

print(list(combinations([0, 1, 2, 3], 2)))

