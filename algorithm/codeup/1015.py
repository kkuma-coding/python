# value = input()
# print (type(value)) # <class 'str'> string
# print (type(float(value))) # <class 'float'>
# print (value)

# 444 --> 444.00
# 123 --> 123.00
# 123.4566 --> 123.46

value = float(input())
print ("{:.2f}".format(value))