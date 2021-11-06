values = [x for x in input() if x.isalpha()]

s, e = ord('a'), ord('z')

alpha_list = [chr(x) for x in range(s, e+1)]
dict1 = dict.fromkeys(alpha_list, 0)

for x in values:
    dict1[x] += 1

for k in dict1.keys():
    print(f'{k}:{dict1[k]}')
