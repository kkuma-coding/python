from itertools import chain

# some consonants
consonants = ['d', 'f', 'k', 'l', 'n', 'p']

# some vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# resultatnt list
res = list(chain(consonants, vowels))

print(res)

res.sort()
print(res)