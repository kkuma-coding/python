'''
4 2
Jeon 95
Kim 59
Lee 90
Bae 100

{'Jeon': 95, 'Kim': 59, 'Lee': 90, 'Bae': 100}


4 1
Jeon 95
Kim 59
Lee 90
Bae 100
'''
people, max = input().split()
people, max = int(people), int(max)

MyDict = dict()

for i in range(people):
    name, score = input().split()
    score = int(score)
    MyDict[name] = score

sortedDict = dict(sorted(MyDict.items(), key=lambda item: item[1], reverse=True))
outList = list(sortedDict.keys())
for i in range(max):
    print(outList[i])