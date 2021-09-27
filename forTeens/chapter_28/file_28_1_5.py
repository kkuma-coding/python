def test_integer(number):
    if number == int(number):
        return True
    else:
        return False

#Main code starts here
total = 0
count = 0
x = float(input())
while test_integer(x) == True:
    if x > 0:
        total += x
        count += 1
    x = float(input())

if count > 0:
    print(total / count)
