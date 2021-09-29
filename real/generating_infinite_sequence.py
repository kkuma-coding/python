"""
https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions
"""
import itertools

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


gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print("-----------------------------")

gen2 = itertools.count()
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))