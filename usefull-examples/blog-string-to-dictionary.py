"""
https://security-nanglam.tistory.com/427?category=811649
"""
string_list = ['A', 'B', 'C']

dictionary = {st:0 for st in string_list}
print(dictionary)

# with enumerate function
dictionary = {st:idx for idx, st in enumerate(string_list)}
print(dictionary)
