a = int(input())
b = int(input())

if a > 3:
    print("Message #1")
elif a > 1 and b <= 10:
    print("Message #2")
    print("Message #3")
elif b == 0:
    print("Message #4")
else:
    print("Message #5")

print("The End!")
