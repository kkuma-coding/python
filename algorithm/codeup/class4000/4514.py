stack = []

count = 8
group = 3

def combi_gen(val, dep, cur_dep):
    global count
    global group
    global stack
    if cur_dep > 0 and val > 0:
        for i in range(1, val):
            stack.append(i)
            combi_gen(val-i, cur_dep-1)
            stack.pop()
    elif cur_dep <= 0:
        stack.append(count - sum(stack))
        print (*stack)
        stack.pop()
        return

for i in range(1, count-group+2):
    combi_gen(count, group)

