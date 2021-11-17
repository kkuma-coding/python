import sys

readl = sys.stdin.readline
sanghan = 0

emp_num, total_gibu = map(int, input().split())
pay_list = list(map(int, readl().strip().split()))

pay_list.sort(reverse=True)

pay_min = pay_list[-1]
pay_max = pay_list[0]

pay_mid = (pay_max + pay_min) // 2

guidu_list = [] # * len(pay_list)
pay_mid_idx = 0

for x in pay_list:
    if x > pay_mid:
        guidu_list.append(x-pay_mid)
        pay_mid_idx += 1
    else:
        break

print(sum(guidu_list))
