string_list = ['Aa','Bb','Cc']
int_list = [1, 2, 3]

zip1 = zip(string_list, int_list)
zip_iter = iter(zip1)
for x, y in zip_iter:
    print(x, y)

print("----------------------------------")
zip_iter = iter(zip1)
for x, y in zip_iter:
    print(y, x)

print("----------------------------------")


dictionary = dict(zip(string_list, int_list))
print(dictionary)
