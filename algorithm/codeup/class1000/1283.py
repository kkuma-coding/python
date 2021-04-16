# codeup.kr/problem.php?id=1283
'''
[주식 투자]

gbs라는 개미 투자자가 주식에 투자하려고 합니다.

이 사람이 투자한 돈의 액수와,
그 주식의 하루간의 변동을 퍼센트로 알 때,
이 사람의 순수익과 이득/손해 판단을 출력하세요.
'''
investment = int(input())
origin_investment = investment

invest_days = int(input())

up_and_down_percent = input().split()

dec_up_and_down_percent = [int(a) for a in up_and_down_percent]

for day in range(invest_days):
    change = investment * (dec_up_and_down_percent[day]/100)
    investment = investment + change

invest_result = round(investment)-origin_investment
print(invest_result)

if (invest_result < 0):
    print("bad")
elif (invest_result > 0):
    print("good")
else:
    print("same")