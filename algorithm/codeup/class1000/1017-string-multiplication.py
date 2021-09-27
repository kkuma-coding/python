print ("abc" * 3)
print ("abc " * 3)

# https://github.com/satwikkansal/wtfpython#-strings-can-be-tricky-sometimes-
# 20 is an existing object but 21 isn't
print('a'*20 is 'a'*20)
print('a'*21 is 'a'*21)

print('a'*20 == 'a'*20)
print('a'*21 == 'a'*21)