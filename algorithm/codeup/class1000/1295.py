"""
https://codeup.kr/problem.php?id=1295&rid=0

주어지는 문장의 대문자를 소문자로, 소문자를 대문자로 변경하는 프로그램을 작성하라.

<<<입력 예시>>>
CodeChallenge2014withMSP

<<<출력 예시>>>
cODEcHALLENGE2014WITHmsp
"""
val = input()
output = ""
for x in val:
    if (x.islower()):
        output += x.upper()
    elif(x.isupper()):
        output += x.lower()
    else:
        output += x

print(output)