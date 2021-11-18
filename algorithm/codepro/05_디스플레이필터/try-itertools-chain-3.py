from itertools import chain

res = list(chain("ABC", "DEF", "GHI", "JKL"))

print(res)

print(''.join(res))