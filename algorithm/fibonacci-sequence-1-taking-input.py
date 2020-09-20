# Fibonacci 순서(sequence) 만들어 내기

number = int (input("몇 번째까지의 피보나치 수를 만들어볼까요? "))

def fib (n):
    if (n <= 1):
        return 1
    if (n == 2):
        return 1
    return fib (n-1) + fib (n-2)

print (fib (number))
