"""
https://security-nanglam.tistory.com/427?category=811649
"""
string_list = ['A', 'B', 'C']

print(dict.fromkeys(string_list))

print(dict.fromkeys(string_list, 0))
print(dict.fromkeys(string_list, "hyosun"))

print(dict.fromkeys(string_list,
                    range(len(string_list))))
