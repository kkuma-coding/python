from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import chain

for x in list(combinations_with_replacement([1, 2, 3], 2)):
    print(type(x))

# print(list(itertools.combinations([1, 2, 3], 1)))
# for iter in combinations([1,2,3],1):
#     print(len(iter))

# print(list(combinations([0, 1, 2, 3], 2)))
