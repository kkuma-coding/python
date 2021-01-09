words = [None] * 20

for i in range(20):
    words[i] = input()

for i in range(19, -1, -1):
    print(words[i])
