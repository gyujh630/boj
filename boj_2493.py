#2493번: 탑

import sys

n = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split(" ")))
stack = [] #아직 닿지 못한 레이저 리스트..
answer = [0 for i in range(n)]

for i in range(n):
    height = top_list[n-1-i]
    if len(stack) > 0:
        while stack:
            stack_top = stack[len(stack) - 1]
            if height >= stack_top[0]:
                answer[stack.pop()[1]] = n - i
            else:
                break
    stack.append([height, n-1-i])

result_string = " ".join(map(str, answer))
print(result_string, " ")