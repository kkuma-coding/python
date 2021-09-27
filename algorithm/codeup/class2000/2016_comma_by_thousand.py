"""
https://codeup.kr/problem.php?id=2016

"""
comma_count = len("000")

N = int(input())
val = input()

count = 0
output = ""
for c in val[::-1]:
    output += c
    count += 1
    if count % comma_count == 0:
        output += ","
        count = 0

if output[-1] == ",":
    output = output[:-1]

print(output[::-1])