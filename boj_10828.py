import sys
import re
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline().rstrip()
    if 'push' in command:
        command = re.sub(r'[^0-9]', '', command)
        stack.append(command)
    if command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
            stack.pop()
    if command == 'size':
        print(len(stack))
    if command == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)
    if command == 'top':
        if len(stack) == 0:
            print(-1)
        else: print(stack[len(stack)-1])