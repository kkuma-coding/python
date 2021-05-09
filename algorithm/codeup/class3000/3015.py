'''
4 2
Jeon 95
Kim 59
Lee 90
Bae 100
'''
# https://codeup.kr/problem.php?id=3015
people, max = input().split()
people, max = int(people), int(max)

myDict = dict()

for i in range(people):
    name, score = input().split()
    score = int(score)
    myDict[name] = score

print(myDict)