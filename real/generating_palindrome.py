"""
https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions
"""
a = range(5)
print(list(a))


def infinite_sequence():
    """
    This code block is short and sweet. First, you initialize
    the variable num and start an infinite loop. Then, you
    immediately yield num so that you can capture the initial state.
    This mimics the action of range().
    """
    num = 0
    while True:
        yield num
        num += 1


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


for i in infinite_sequence():
    pal = is_palindrome(i)
    if pal:
        print(i)