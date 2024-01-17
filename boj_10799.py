#10799번: 쇠막대기

import sys

str = sys.stdin.readline().rstrip()
stack = []
count = 0

for i in range(0, len(str)-1):
    brk = str[i]  #괄호
    next_brk = str[i+1]

    if brk == '(':
        if next_brk == ')':
            count += len(stack)
        else:
            stack.append(brk)
            count += 1
    else:
        if len(stack) != 0 and str[i-1] != '(':
            stack.pop()

print(count)
