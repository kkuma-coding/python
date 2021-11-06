"""
https://codeup.kr/problem.php?id=4514

<input>
8 3
5 4 2 6 9 3 8 7
"""
combi = []
stack = []

count, depth = map(int, input().split())
nums = list(map(int, input().split()))


def dfs(val, cur_dep):
    global combi
    global count
    global depth

    if cur_dep <= 0:
        combi.append(list(stack))
        # print(*stack, f"==> sum={sum(stack)}")
        return

    for i in range(1, count+1):
        if sum(stack) + i > count:
            continue

        if len(stack) == depth - 1:
            stack_push_val = count-sum(stack)
            stack.append(stack_push_val)
            dfs(stack_push_val, cur_dep - 1)
            stack.pop()
            break
        else:
            stack_push_val = i
            stack.append(stack_push_val)
            dfs(stack_push_val, cur_dep - 1)
            stack.pop()


dfs(1, depth)

max_list = []
for c in combi:
    ii = 0
    max = 0
    for i in c:
        comp_sum = sum(nums[ii:ii+i])
        if max < comp_sum:
            max = comp_sum
        # print(nums[ii:ii+i], end=", ")
        # print(f"{i}+{ii}={i+ii}")
        ii += i
    max_list.append(max)

print(min(max_list))