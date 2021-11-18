# https://www.geeksforgeeks.org/python-itertools-chain/
from itertools import chain

odd = [i for i in range(10) if i % 2 == 1]
even = [i for i in range(10) if i % 2 == 0]

print(odd)
print(even)

chained_list = list(chain(odd, even))
chained_list.sort()
print(chained_list)

chained_list.reverse()
print(chained_list)